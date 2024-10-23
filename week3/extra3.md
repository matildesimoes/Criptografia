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

### Q2

#### 1. Oráculo de Encriptação

O adversário interage com o oráculo de encriptação enviando duas mensagens, *m0* e *m1*, que têm o mesmo comprimento. Estas mensagens são escolhidas cuidadosamente com base nas propriedades da encriptação do modo CBC e no facto de o IV ser fixo. O oráculo de encriptação retorna *C0 = Enc(k, m0)* ou *C1 = Enc(k, m1)* com base no bit aleatório *b*. Também responde a todas as *queries* feitas pelo adversário antes da experiência começar.

#### 2. Construção de *m0* e *m1*

Para montar um ataque bem-sucedido, o adversário explora o facto do IV ser sempre o mesmo. Assim, sabendo com o CBC funciona conseguimos concluir que ao mandar uma mensagem *m* constituída por zeros, o primeiro bloco cifrado será a encriptação do IV, pois E(IV + 0<sup>n</sup>) = E(IV).

Assumindo que o IV é fixo e sabendo a sua encriptação, o adversário pode construir *m0* e *m1* de forma a que os primeiros blocos sejam diferentes de maneira controlada, enquanto os blocos seguintes são idênticos.

 - *m0* = 1<sup>n</sup> || X, onde X é um texto aleatório e n é o tamanho do primeiro bloco.
 - *m1* = 0<sup>n</sup> || X, onde X é um texto aleatório e n é o tamanho do primeiro bloco.

#### 3. Determinar *b*

O adversário envia *m0* e *m1* ao oráculo de encriptação, que retorna *C0 = Enc(k, m0)* ou *C1 = Enc(k, m1)* com base no bit aleatório *b*.

- Se o oráculo de encriptação retornar *C0*, o primeiro bloco do texto cifrado será *E(IV XOR 1<sup>n</sup>)*.
- Se o oráculo de encriptação retornar *C1*, o primeiro bloco do texto cifrado será *E(IV + 0<sup>n</sup>) = E(IV)*.

Assim, o adversário pode diferenciar *C0* de *C1*, porque o primeiro bloco do texto cifrado para *m1* será a encriptação do IV, que consegue comparar com a resposta da *query* feita anteriormente e, assim, adivinhar corretamente *b = 1*.

#### 4. Algoritmo para o Adversário

- **Passo 1:** O adversário submete as mensagens *m0 = 1<sup>n</sup> || X* e *m1 = 0<sup>n</sup> || X* ao oráculo de encriptação.
- **Passo 2:** O oráculo de encriptação retorna o texto cifrado *C = Enc(k, mb)*, onde *b pertence {0,1}.
- **Passo 3:** O adversário verifica o primeiro bloco do texto cifrado. Se o primeiro bloco corresponder à encriptação do IV (ou seja, *E(IV)*), o adversário adivinha que *b = 1*. Se corresponder à outra encriptação (ou seja, *E(IV XOR 1<sup>n</sup>)*), o adversário adivinha que *b = 0*.
- **Passo 4:** O adversário vence se adivinhar corretamente o valor de *b*, o que pode fazer com probabilidade 1.

Explorando o IV fixo, o adversário pode distinguir entre duas encriptações diferentes com probabilidade não negligenciável. Isso viola a garantia de segurança IND-CPA do esquema criptografico, já que o adversário pode sempre determinar qual foi a mensagem encriptada.

### Q3

### Q4

#### P1

Mesmo quando a mensagem já possui um tamanho múltiplo do tamanho do bloco **b**, é necessário adicionar padding no esquema **PKCS#7** para garantir que o recetor possa identificar e remover corretamente o padding durante a desencriptação. Se nenhum padding for adicionado a uma mensagem, em que o seu tamanho já é múltiplo do tamanho do bloco, o recetor não conseguiria distinguir se os últimos bytes são dados reais ou padding.

No **PKCS#7**, é sempre adicionado um bloco de padding, no mínimo. Cada byte de padding contém o valor numérico igual ao número de bytes de padding adicionados. Dessa forma, durante a desencriptação, o recetor lê o valor do último byte para determinar quantos bytes de padding remover. Isso assegura que o padding seja tratado corretamente, independentemente do tamanho original da mensagem.

#### P2


