# Week #3 Extra

### Q1

#### P1

#### P2

### Q2

#### 1. Oráculo de Encriptação

O adversário interage com o oráculo de encriptação enviando duas mensagens, *m0* e *m1*, que têm o mesmo comprimento. Estas mensagens são escolhidas cuidadosamente com base nas propriedades da encriptação do modo CBC e no facto de o IV ser fixo. O oráculo de encriptação retorna *C0 = Enc(k, m0)* ou *C1 = Enc(k, m1)* com base no bit aleatório *b*.

#### 2. Construção de *m0* e *m1*

Para montar um ataque bem-sucedido, o adversário explora o facto do IV ser sempre o mesmo. No AES-CBC, o primeiro bloco de texto cifrado depende da operação XOR entre o primeiro bloco do texto original e do IV, seguido da encriptação com a chave *k*. Assumindo que o IV é fixo, o adversário pode construir *m0* e *m1* de forma a que os primeiros blocos sejam diferentes de maneira controlada, enquanto os blocos seguintes são idênticos.

 - *m0* = IV || X, onde X é um texto original.
 - *m1* = 0<sup>n</sup> || X, onde 0<sup>n</sup> é um bloco de zeros do mesmo comprimento que o IV.

Como o segundo bloco de *m0* e *m1* é idêntico, o segundo bloco cifrado também será idêntico.

#### 3. Determinar *b*

O adversário envia *m0* e *m1* ao oráculo de encriptação, que retorna *C0 = Enc(k, m0)* ou *C1 = Enc(k, m1)* com base no bit aleatório *b*.

No AES-CBC:
- Se o oráculo de encriptação retornar *C0*, o primeiro bloco do texto cifrado será *E(IV + IV) = E(0)*.
- Se o oráculo de encriptação retornar *C1*, o primeiro bloco do texto cifrado será *E(IV + 0<sup>n</sup>) = E(IV)*.

Assim, o adversário pode diferenciar *C0* de *C1*, porque o primeiro bloco do texto cifrado para *m0* será a encriptação de zero, enquanto para *m1* será a encriptação do IV fixo. Comparando o primeiro bloco do texto cifrado, o adversário pode adivinhar corretamente se *b = 0* ou *b = 1*.

#### 4. Algoritmo para o Adversário

- **Passo 1:** O adversário submete as mensagens *m0 = IV || X* e *m1 = 0<sup>n</sup> || X* ao oráculo de encriptação.
- **Passo 2:** O oráculo de encriptação retorna o texto cifrado *C = Enc(k, mb)*, onde *b pertence \{0,1\}.
- **Passo 3:** O adversário verifica o primeiro bloco do texto cifrado. Se o primeiro bloco corresponder à encriptação de zero (ou seja, *E(0)*), o adversário adivinha que *b = 0*. Se corresponder à encriptação do IV fixo (ou seja, *E(IV)*), o adversário adivinha que *b = 1*.
- **Passo 4:** O adversário vence se adivinhar corretamente o valor de *b*, o que pode fazer com probabilidade 1.

Explorando o IV fixo, o adversário pode distinguir entre duas encriptações diferentes com probabilidade não negligenciável. Isso viola a garantia de segurança IND-CPA do esquema criptografico, já que o adversário pode sempre determinar qual foi a mensagem encriptada. A principal vulnerabilidade aqui é o uso de um IV fixo, que leva a textos cifrados previsíveis permitindo ataques.

### Q3

