# Week #3 Extra

## Q1: *Weak Security*

### P1

O código relevante encontra-se em `q1.py`, devidamente comentado.

A chave gerada pelo ficheiro `ciphersuite_aesnotrand.py` tem, no máximo, 3 *bytes* (24 *bits*).
Então, o espaço de chave é 2<sup>24</sup>, ou seja, existem 2<sup>24</sup> possibilidades para a chave.

Como tal, o código desenvolvido lê o ficheiro com o texto encriptado e tenta desencriptá-lo com todas as possibilidades de chave até obter a mensagem original ("*Attack at Dawn!!*") e, quando conseguir, encontrou a chave.

### P2

Para descobrir chaves com *n bytes*, a nossa máquina demora os tempos expostos na tabela abaixo.

| *n* (*bytes*) | tempo (*s*) |
| ------- | ----------- |
| 1 | 0,005 |
| 2 | 1 |
| 3 | 250 |

Ou seja, o aumento de 1 *byte* no tamanho da chave parece levar a um tempo de execução cerca de 250 vezes superior.

Um espaço de chave de *k* *bits* tem 2<sup>k</sup> possibilidades de chave.

Efetivamente, *n bytes* correspondem a 8*n* *bits*, ou seja, existem 2<sup>8n</sup> possibilidades de chave.
Assim, *n* + 1 *bytes* correspondem a 8(*n* + 1) = 8*n* + 8 *bits*, ou seja, existem 2<sup>8n + 8</sup> possibilidades de chave.

Como tal, o aumento de 1 *byte* no tamanho da chave leva a mais 2<sup>8n + 8</sup>/2<sup>8n</sup> = 2<sup>8</sup> = 256 possibilidades de chave, daí o aumento do tempo de execução.

Assim, o tempo de execução (em segundos) para descobrir uma chave de *n* *bytes* é aproximado pela progressão geométrica de termo inicial 0,005 e razão 256, ou seja, f(n) = 0,005 * 256<sup>n - 1</sup>.

3 horas correspondem a 10800 segundos, pelo que responder à pergunta é resolver a equação f(n) = 10800 <=> 0,005 * 256<sup>n - 1</sup> = 10800 <=> n = 3,6 -> n = 4.

Deste modo, conclui-se que aumentar o tamanho da chave para 4 *bytes* tornaria impossível descobrir a chave em menos de 3 horas.
Na verdade, no pior caso, por força-bruta, uma chave de 4 *bytes* só consegue ser descoberta em cerca de 24 horas.

Note-se que todos estes cálculos assumem o pior caso para a descoberta da chave, isto é, ter de testar por força-bruta todas as possibilidades do espaço de chave, mas, na prática, em média, o tempo de execução seria cerca de metade do pior caso teórico.

## Q2: *Fixed Initialization Vectors*

### 1. *Queries* ao Oráculo de Encriptação

Antes do desafio da experiência, o adversário pode fazer e enviar *queries* ao adversário para que ele responda.

No desafio da experiência, o adversário interage com o oráculo de encriptação enviando duas mensagens, *m0* e *m1*, com o mesmo comprimento.
Estas mensagens são escolhidas cuidadosamente com base nas propriedades da encriptação do modo CBC e no facto de o IV ser fixo.
O oráculo de encriptação retorna *C0 = Enc(k, m0)* ou *C1 = Enc(k, m1)*, com base no bit aleatório *b*.

Para montar um ataque bem-sucedido, o adversário explora o facto do IV ser sempre o mesmo.
Assim, sabendo como o CBC funciona, conclui que, ao mandar uma mensagem *m* constituída por zeros, o primeiro bloco cifrado será a encriptação do IV, pois *E(IV + 0<sup>n</sup>) = E(IV)*.

### 2. Construção de *m0* e *m1*

Assumindo que o IV é fixo e sabendo a sua encriptação (obtida anteriormente), o adversário pode construir *m0* e *m1* de forma a que os primeiros blocos sejam diferentes de maneira controlada, enquanto os blocos seguintes são idênticos.

 - *m0 = 0<sup>n</sup> || X*, onde X é um texto qualquer e *n* é o tamanho do primeiro bloco.
 - *m1 = 1<sup>n</sup> || X*, onde X é um texto qualquer e *n* é o tamanho do primeiro bloco.

### 3. Decisão de *b*

O adversário envia *m0* e *m1* ao oráculo de encriptação, que retorna *C0 = Enc(k, m0)* ou *C1 = Enc(k, m1)*, com base no bit aleatório *b*.

- Se o oráculo de encriptação retornar *C0*, o primeiro bloco do texto cifrado será *E(IV + 0<sup>n</sup>) = E(IV)*.
- Se o oráculo de encriptação retornar *C1*, o primeiro bloco do texto cifrado será *E(IV + 1<sup>n</sup>)*.

Assim, o adversário pode diferenciar *C0* de *C1* porque o primeiro bloco do texto cifrado para *m0* será a encriptação do IV, que consegue comparar com a resposta da *query* feita anteriormente e, assim, adivinhar corretamente que *b = 0*.
Caso contrário, se o primeiro bloco da resposta for diferente da encriptação do IV, o adversário adivinha corretamente que *b = 1*.

### Algoritmo para o Adversário

Antes do desafio, o adversário enviou a mensagem *m = 0<sup>n</sup>* e, assim, conseguiu obter a encriptação do IV (*E(IV)*).

No desafio:
- **Passo 1:** O adversário submete as mensagens *m0 = 0<sup>n</sup> || X* e *m1 = 1<sup>n</sup> || X* ao oráculo de encriptação.
- **Passo 2:** O oráculo de encriptação retorna o texto cifrado *C = Enc(k, mb)*, onde *b* pertence a {0, 1}.
- **Passo 3:** O adversário verifica o primeiro bloco do texto cifrado. Se o primeiro bloco corresponder à encriptação do IV (ou seja, *E(IV)*), o adversário adivinha que *b = 0*. Se corresponder à outra encriptação (ou seja, *E(IV + 1<sup>n</sup>)*), o adversário adivinha que *b = 1*.
- **Passo 4:** O adversário vence se adivinhar corretamente o valor de *b*, o que pode fazer com probabilidade 1.

Explorando o IV fixo, o adversário pode distinguir entre duas encriptações diferentes com probabilidade não negligenciável.
Isto viola a garantia de segurança IND-CPA do esquema criptográfico, já que o adversário pode sempre determinar qual foi a mensagem encriptada.

## Q3: *Predictable Initialization Vectors*

...TODO

Tal como provado, é possível obter o valor do IV a partir do *nonce*.

Assim, antes do desafio, o adversário envia uma mensagem 0<sup>n</sup>, que é cifrada com o IV<sup>A</sup>.

No desafio, o adversário envia:
1. m<sub>0</sub> = IV<sub>0</sub> XOR IV<sub>A</sub>, que resulta na mensagem cifrada c<sub>0</sub> = E(k, IV<sub>0</sub> XOR IV<sub>0</sub> XOR IV<sub>A</sub>) = E(k, IV<sub>A</sub>)
2. m<sub>1</sub>, diferente de m<sub>0</sub>

Se a resposta do oráculo for igual a E(k, IV<sub>A</sub>), obtido antes da experiência, o adversário consegue adivinhar com certeza que *b = 0*. Se a resposta for diferente, o adversário adivinha com certeza que *b = 1*.

## Q4: *Padding Attacks*

### P1

Mesmo quando a mensagem já possui um tamanho múltiplo do tamanho do bloco **b**, é necessário adicionar padding no esquema **PKCS#7** para garantir que o recetor possa identificar e remover corretamente o padding durante a desencriptação. Se nenhum padding for adicionado a uma mensagem, em que o seu tamanho já é múltiplo do tamanho do bloco, o recetor não conseguiria distinguir se os últimos bytes são dados reais ou padding.

No **PKCS#7**, é sempre adicionado um bloco de padding, no mínimo. Cada byte de padding contém o valor numérico igual ao número de bytes de padding adicionados. Dessa forma, durante a desencriptação, o recetor lê o valor do último byte para determinar quantos bytes de padding remover. Isso assegura que o padding seja tratado corretamente, independentemente do tamanho original da mensagem.

### P2

Se no processo de desencriptação se tiver sido alterado um byte de padding, o oráculo de encriptação dará um erro. Assim, ao tenta forçar erros de padding, o atacante consegue descobrir quais são os bytes de padding e consequentemente o tamanho da mensagem. Para isso, basta começar do final da mensagem para o início a fazer alterações byte a byte até deixarem de resultar em erros de padding.

Para além disto, é possível, a partir dos erros de padding descobrir a mensagem original.

**Extrair informação quando não há erro de *padding***

No modo CBC, cada mensagem original obtém-se fazendo a operação XOR entre o bloco anterior da mensagem cifrada e a desencriptação do bloco correspondente da mensagem cifrada.

1. Tendo em conta o *byte* que se quer recuperar, define-se o *padding* esperado: para o *byte* índice-*i* a contar do final do bloco, define-se *padding* com valor *i*.
2. Altera-se, sistematicamente, o *byte* correspondente do bloco anterior e todos os seguintes dentro desse bloco para um valor de `0x00` até `0xFF`. Cada tentativa é enviada para o oráculo de desencriptação.
3. Se essa tentativa de desencriptação retornar *padding* válido, obtém-se:

    **D(k, C<sub>n</sub>[i]) = C<sub>n-1</sub>[i] XOR P<sub>n</sub>[i]**

    - **D(k, C<sub>n</sub>[i]):** parte da mensagem original que se pretende obter
    - **C<sub>n-1</sub>[i]:** alteração enviada ao oráculo de encriptação
    - **P<sub>n</sub>[i]:** *padding* foi obtido pelo oráculo de encriptação 

Assim, é possível obter **D(k, C<sub>n</sub>[i])**.

**Exemplo**

1. Para recuperar o último *byte* do bloco *n* (P<sub>n</sub>[16]), define-se o *padding* esperado como `0x01`.
2. Altera-se C<sub>n</sub>[16], sistematicamente, para um valor entre `0x00` e `0xFF` até se obter *padding* válido.
3. Quando se obtiver *padding* válido, deduz-se: 

    **D(k, C<sub>n</sub>[16]) = C<sub>n-1</sub>[16] XOR P<sub>n</sub>[16] = C<sub>n-1</sub>[16] XOR `0x01`**

Este processo é repetido iterativamente para cada *byte* do bloco *n*, ajustando o *padding* conforme necessário e manipulando os *bytes* correspondentes de C<sub>n - 1</sub>.

Depois de recuperar o bloco *n*, aplica-se o mesmo método para o bloco *n - 1* e assim sucessivamente, até recuperar todo a mensagem original.
