# Week #3 Extra

### Q1

#### P1

#### P2

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


