# Week #1 Extra

## Q1: Semantically secure schemes

### Q1

Um esquema de encriptação é considerado correto se, partindo de E'(k, m), se consegue chegar a E(k, m). (->será E, D e recuperar a mensagem)

1. **reverse(E(k, m)):** reverse(reverse(E(k, m))) = E(k, m), reverse(reverse(x)) = x
2. **E(0<sup>n</sup>, m):** E(k, m), k = 0<sup>n</sup>, é um caso particular de E(k, m) em que a chave é k = 0<sup>n</sup> (VER)
3. **E(k, m) || 0:** basta remover o 0 concatenado no final para se obter E(k, m)
4. **E(k, m) XOR 1<sup>n</sup>:** E(k, m) XOR 1<sup>n</sup> XOR 1<sup>n</sup> = E(k, m), porque x XOR x = 0
5. **E(k, 0<sup>n</sup>):** é impossível voltar a obter a mensagem inicial, porque foi substituída por 0<sup>n</sup>
6. **E(k, m) || m:** como |E(k, m)| = |m| = n e |E(k, m) || m| = 2n, basta dividir E(k, m) || m a meio, obtendo-se E(k, m) do lado esquerdo e m do lado direito
7. **E(k, m) || E(k', m'):** como não há informação sobre o tamanho de m e m', é impossível saber onde dividir E(k, m) || E(k', m') para se voltar a obter as mensagens iniciais

Os esquemas de encriptação corretos são: 1, 2, 3, 4 e 6.

### Q2

Considerando que o esquema de encriptação (E, D) é semanticamente seguro, partindo do princípio que não se usa a mesma chave mais do que uma vez, são seguros os esquemas de encriptação que permitam a utilização de chaves diferentes em encriptações diferentes, não obrigando a utilização da mesma chave sempre.

1.**reverse(E(k, m)):** é seguro porque a chave é k

2.**E(0<sup>n</sup>, m):** não é seguro porque a chave é obrigatoriamente 0<sup>n</sup>

3.**E(k, m) || 0:** é seguro porque a chave é k

4.**E(k, m) XOR 1<sup>n</sup>:** é seguro porque a chave é k

6.**E(k, m) || m:** é seguro porque a chave é k (VER)

Os esquemas de encriptação corretos e semanticamente seguros são: 1, 3, 4 e 6.

### Q3

2. **E(0<sup>n</sup>, m)** 

O atacante sabe o esquema de encriptação que vai ser utilizado e envia duas mensagens de comprimento n. A partir desse momento, como sabe o esquema de encriptaçáo, o atacante fica a saber também que a chave utilizada pelo *challenger* será 0<sup>n</sup>, sendo n conhecido, porque foi definido pelo atacante. Assim, quando o atacante receber a mensagem cifrada c, conseguirá decifrá-la porque sabe a chave e o esquema de encriptaçao (E, D). Deste modo, o atacante consegue saber a mensagem que foi encriptada com probabilidade 1, quebrando o modelo de segurança.

## Q2: Shifting the alphabet

Pretende-se provar que o esquema de encriptação E é perfeitamente seguro.

Considere-se que o tamanho das mensagens é 1 (uma letra do alfabeto inglês).

Seja m a mensagem que será encriptada pelo *challenger*. Então, c ou é m *shift* 0, ou m *shift* 1, ou m *shift* 2, ... E assim sucessivamente, até m *shift* 25.

Como a chave é aleatoriamente amostrada (segue uma distribuição uniformemente aleatória com valores entre 0 e 25), então qualquer uma das possibilidades anteriores é igualmente provável.

Efetivamente, este facto verifica-se para qualquer tamanho de mensagem, porque uma mensagem de tamanho n é apenas uma concatenação de n mensagens de tamanho 1.

Assim, observa-se que, sem conhecimento da chave, a mensagem cifrada c segue uma distribuição uniforme, pelo que não é possível o atacente prevê-la com probabilidade superior a 1/2.

Na verdade, como a distrubuição aleatória é uniforme, a probabilidade de o atacante adivinhar corretamente a mensagem (sem conhecimento da chave) é (1/26)<sup>n</sup>.

Por isso, está provado que o esquema de encriptação E é perfeitamente seguro.

## Q3: Secret Sharing

### P1

Pretende-se identificar as alterativas tais que "nenhuns dois participantes conseguem recuperar a mensagem, mas todos os três participantes conseguem recuperar a mensagem".

- P<sub>1</sub> e P<sub>2</sub> têm m<sub>1</sub>, m<sub>2</sub>, m<sub>3</sub>, m<sub>4</sub>, logo nunca conseguem recuperar a mensagem (falta m<sub>5</sub> e m<sub>6</sub>)

1. **(m<sub>5</sub>, m<sub>6</sub>):** é válida porque

- P<sub>1</sub> e P<sub>3</sub> têm m<sub>1</sub>, m<sub>2</sub>, m<sub>5</sub>, m<sub>6</sub>, logo não conseguem recuperar a mensagem (falta m<sub>3</sub> e m<sub>4</sub>)
- P<sub>2</sub> e P<sub>3</sub> têm m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, m<sub>6</sub>, logo não conseguem recuperar a mensagem (falta m<sub>1</sub> e m<sub>2</sub>)
- P<sub>1</sub>, P<sub>2</sub> e P<sub>3</sub> têm m<sub>1</sub>, m<sub>2</sub>, m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, m<sub>6</sub>, logo conseguem recuperar a mensagem

2. **(m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, m<sub>6</sub>):** não é válida porque P<sub>1</sub> e P<sub>3</sub> conseguem recuperar a mensagem

- P<sub>1</sub> e P<sub>3</sub> têm m<sub>1</sub>, m<sub>2</sub>, m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, m<sub>6</sub>, logo conseguem recuperar a mensagem
- P<sub>2</sub> e P<sub>3</sub> têm m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, m<sub>6</sub>, logo não conseguem recuperar a mensagem (falta m<sub>1</sub> e m<sub>2</sub>)
- P<sub>1</sub>, P<sub>2</sub> e P<sub>3</sub> têm m<sub>1</sub>, m<sub>2</sub>, m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, m<sub>6</sub>, logo conseguem recuperar a mensagem

3. **(m<sub>2</sub>, m<sub>3</sub>, m<sub>5</sub>, m<sub>6</sub>):** é válida porque

- P<sub>1</sub> e P<sub>3</sub> têm m<sub>1</sub>, m<sub>2</sub>, m<sub>3</sub>, m<sub>5</sub>, m<sub>6</sub>, logo não conseguem recuperar a mensagem (falta m<sub>4</sub>)
- P<sub>2</sub> e P<sub>3</sub> têm m<sub>2</sub>, m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, m<sub>6</sub>, logo não conseguem recuperar a mensagem (falta m<sub>1</sub>)
- P<sub>1</sub>, P<sub>2</sub> e P<sub>3</sub> têm m<sub>1</sub>, m<sub>2</sub>, m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, m<sub>6</sub>, logo conseguem recuperar a mensagem

4. **(m<sub>1</sub>, m<sub>4</sub>, m<sub>5</sub>):** não é válida porque nenhum participante tem m<sub>6</sub>

- P<sub>1</sub> e P<sub>3</sub> têm m<sub>1</sub>, m<sub>2</sub>, m<sub>4</sub>, m<sub>5</sub>, logo não conseguem recuperar a mensagem (falta m<sub>3</sub> e m<sub>6</sub>)
- P<sub>2</sub> e P<sub>3</sub> têm m<sub>1</sub>, m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, logo não conseguem recuperar a mensagem (falta m<sub>2</sub> e m<sub>6</sub>)
- P<sub>1</sub>, P<sub>2</sub> e P<sub>3</sub> têm m<sub>1</sub>, m<sub>2</sub>, m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, logo não conseguem recuperar a mensagem (falta m<sub>6</sub>)

As alternativas válidas são: 1 e 3.

### P2

Uma alternativa possível é:
- P<sub>1</sub> tem m<sub>1</sub>, m<sub>2</sub>, m<sub>3</sub>, m<sub>4</sub>
- P<sub>2</sub> tem m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, m<sub>6</sub>
- P<sub>3</sub> tem m<sub>1</sub>, m<sub>2</sub>, m<sub>5</sub>, m<sub>6</sub>

Tendo em conta que nenhum dos participantes, sozinho, tem os 6 segredos da mensagem, conclui-se que nenhum dos participantes consegue, sozinho, recuperar a mensagem.

A alternativa é válida porque:
- P<sub>1</sub> e P<sub>2</sub> têm m<sub>1</sub>, m<sub>2</sub>, m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, m<sub>6</sub>, logo conseguem recuperar a mensagem
- P<sub>1</sub> e P<sub>3</sub> têm m<sub>1</sub>, m<sub>2</sub>, m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, m<sub>6</sub>, logo conseguem recuperar a mensagem
- P<sub>2</sub> e P<sub>3</sub> têm m<sub>1</sub>, m<sub>2</sub>, m<sub>3</sub>, m<sub>4</sub>, m<sub>5</sub>, m<sub>6</sub>, logo conseguem recuperar a mensagem

Assim, conclui-se que todos os pares de participantes conseguem recuperar a mensagem (o que implica que os três participantes juntos também a conseguem recuperar).
