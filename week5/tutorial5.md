# Tutorial #5

## 1

Para usar OpenSSL para calcular o valor SHA256 dos *slides pdf* da aula desta semana, é necessário correr o comando `openssl dgst -sha256 slides.pdf`.

![1](/week5/images/1.png)

Assim, obtém-se `d51b15eeed16158b0a2d0d50c92e3b34f62140b7627b88dca62d4a27e8f0f569`, o que corresponde ao valor presente no enunciado.

### 1.1

Como o valor SHA256 dos *slides pdf* da aula desta semana calculado pelo OpenSSL é igual ao valor dado no enunciado, conclui-se que a integridade do ficheiro foi preservada, isto é, que o ficheiro a que o enunciado se refere é exatamente o mesmo ficheiro cujo valor SHA256 foi calculado pelo OpenSSL.

Isto é verdade porque a função SHA256, enquanto função de *hash*, é resistente a colisões, isto é, dados x<sub>1</sub> e x<sub>2</sub> tais que x<sub>1</sub> é diferente de x<sub>2</sub>, então é extremamente improvável que f(x<sub>1</sub>) = f(x<sub>2</sub>).
Assim, como f(x<sub>1</sub>) = f(x<sub>2</sub>), conclui-se (quase garantidamente) que x<sub>1</sub> = x<sub>2</sub>, ou seja, que os ficheiros são iguais.

### 1.2

Alterando os primeiros 4 *bytes* do ficheiro *pdf* original e re-computando o valor SHA256 deste ficheiro alterado, o esperado/expectável é obter-se um valor completamente diferente, isto é, com todos os *bytes* alterados em relação ao valor anterior.

Isto acontece porque a função SHA256, enquanto função de *hash*, é imprevisível, isto é, produz *outputs* imprevisíveis, pelo que não é possível prever qual será a alteração no *output* a partir do conhecimento da alteração feita no *input*.

Efetivamente, é possível verificar experimentalmente isto mesmo, computando o valor SHA256 do ficheiro *pdf* original (antes da alteração) e o valor SHA256 do ficheiro após a alteração dos seus primeiros 4 *bytes*, tal como é visível na imagem abaixo.
Tal como esperado, os valores SHA256 são completamente diferentes.

![1-2](/week5/images/1-2.png)

## 2

O código para *crackar* a segurança de palavras-passe previsíveis encontra-se em `crack_hash.py`.

O excerto relevante para *crackar* *hashes* sem sal (exercício 1) é o seguinte.

```python
cracked_pwds = []
for h in mixed_hlist:
	for pwd in hex_passwds:
		digest = hashes.Hash(hashes.SHA256())
		digest.update(pwd)
		if hexlify(digest.finalize()) == h:
			cracked_pwds.append(pwd)
			break
```

As *hashes* sem sal são *crackadas* com um ataque de força-bruta, que se limita a, para cada *hash* (`h`) da lista de *hashes* sem sal (`mixed_hlist`), verificar se corresponde à *hash* de cada palavra-passe (`pwd`) da lista das vinte palavras-passes mais comuns de 2019 (`hex_passwds`).
Como a função de *hash* é determinística e não é aplicado sal, quando a *hash* de uma palavra-passe for igual à *hash* da lista de *hashes* sem sal, está encontrada a palavra-passe correspondente a essa *hash* e, assim, *crackada* a segurança dessa palavra-passe.

O excerto relevante para *crackar* *hashes* com sal (exercício 2) é o seguinte.

```python
cracked_spwds = []
cracked_salt = None
sh = mixed_shlist[0]
for pwd in hex_passwds:
	for s in range(256):
		tentative_salt = bytes([s])
		salted_pwd = tentative_salt + pwd
		digest = hashes.Hash(hashes.SHA256())
		digest.update(salted_pwd)
		if hexlify(digest.finalize()) == sh:
			cracked_spwds.append(salted_pwd)
			cracked_salt = tentative_salt
			break

print("The salt is", cracked_salt)

for sh in mixed_shlist[1:]:
	for pwd in hex_passwds:
		salted_pwd = cracked_salt + pwd
		digest = hashes.Hash(hashes.SHA256())
		digest.update(salted_pwd)
		if hexlify(digest.finalize()) == sh:
			cracked_spwds.append(salted_pwd)
			break
```

Este ataque é dividido em duas fases: (1) *crackar* o sal e (2) *crackar* as *hashes* com sal.

1. O sal é *crackado* com um ataque de força-bruta, que se limita a, para cada palavra-passe (`pwd`) da lista das vinte palavras-passes mais comuns de 2019 (`hex_passwds`), testar se, adicionando um *byte* de sal (`tentative_salt`), isto é, um valor entre 0 e 255, a *hash* obtida corresponde à primeira *hash* (`sh`) da lista de *hashes* com sal (`mixed_shlist`).
Como a função de *hash* é determinística e são testados todos os valores possíveis para um *byte* de sal, quando a *hash* de uma palavra-passe com sal for igual à primeira *hash* da lista de *hashes* com sal, está encontrado o sal e a palavra-passe correspondente a essa *hash*.

2. De forma análoga ao exercício anterior, depois de estar *crackado* o sal, as *hashes* com sal (a partir da primeira, já anteriormente *crackada*) são *crackadas* com um ataque de força-bruta, que se limita a, para cada *hash* (`sh`) da lista de *hashes* com sal (`mixed_shlist`), verificar se corresponde à *hash* de cada palavra-passe (`pwd`) da lista das vinte palavras-passes mais comuns de 2019 (`hex_passwds`), adicionando-lhe o sal previamente *crackado*.
Como a função de *hash* é determinística e é aplicado o valor correto do sal (igual para todas as palavras-passe), quando a *hash* de uma palavra-passe com sal for igual à *hash* da lista de *hashes* com sal, está encontrada a palavra-passe (com sal) correspondente a essa *hash* e, assim, *crackada* a segurança dessa palavra-passe.

Note-se que este ataque parte do conhecimento que é utilizado o mesmo sal para computar a *hash* de todas as palavras-passe, o que permite realizar a otimização de *crackar*, em primeiro lugar, o sal e, só depois, *crackar* as palavras-passe com sal.
Caso fosse utilizado um valor de sal diferente para cada palavra-passe, o ataque teria de *crackar* o sal para cada palavra-passe, ou seja, teria de aninhar o ciclo para *crackar* o sal dentro do ciclo para *crackar* cada palavra-passe, o que tornaria o ataque *k* vezes mais demorado, sendo *k* o número de valores possíveis para cada sal (neste caso, como o sal é um *byte*, *k* = 256).

Efetivamente, é mais rápido atacar *hashes* sem sal do que *hashes* com sal, porque o ataque a *hashes* com sal obriga à computação prévia do sal (no melhor caso, o mesmo sal para todas as palavra-passe, mas, no pior caso, sais diferentes para palavras-passe diferentes), o que torna este segundo ataque mais demorado, tal como é possível verificar através de um exemplo de execução.

![2](/week5/images/2.png)

O tempo que estes ataques demoram a ser realizados é *N* vezes o tempo que demora a *crackar* cada *hash*, sendo *N* o número de *hashes*.
Assim, dada uma *hash* para *crackar* e uma lista de palavras-passe (como as vinte palavras-passe mais comuns de 2019), o ataque de força-bruta limita-se a comparar a *hash* a *crackar* com a *hash* de cada palavra-passe da lista de palavras-passe até obter uma correspondência.
Como tal, dada uma lista pequena de palavras-passe, sendo garantido que alguma das palavras-passe corresponde à *hash* a *crackar*, este ataque é extremamente rápido.

Na verdade, a adição de sal, sendo utilizado o mesmo sal para todas as palavras-passe, não acrescenta muita complexidade ao ataque, dado que, depois de *crackado* o sal, o ataque é exatamente o mesmo, pelo que o tempo de execução total não é muito maior do que no caso anterior.
Contudo, se forem utilizados sais diferentes para palavras-passe diferentes, o ataque ao sal passa a fazer parte do ataque a cada *hash*/palavra-passe, pelo que o ataque se torna mais complexo e o tempo de execução aumentará de forma mais substancial.

De facto, sendo *n* o número de palavras-passe e de *hashes* a *crackar* (neste caso, *n* = 20) e *k* o número de valores possíveis para o sal (neste caso, *k* = 256), o ataque a *hashes* sem sal tem complexidade temporal *O(n<sup>2</sup>)* e o ataque a *hashes* com sal, utilizando o mesmo sal para todas as palavras-passe, tem complexidade temporal *O(256k + n<sup>2</sup>)* = *O(n<sup>2</sup>)*.
Contudo, se fossem utilizados sais diferentes para palavras-passe diferentes, a complexidade temporal do ataque já seria *O(kn<sup>2</sup>)* = *O(n<sup>2</sup>)*.

Apesar de todos os ataques terem a mesma ordem de grandeza, ***n<sup>2</sup> < kn + n<sup>2</sup> < kn<sup>2</sup>***, pelo que o ataque mais rápido é a *hashes* sem sal, seguido pelo ataque a *hashes* com sal, mas o mesmo sal para todas as *hashes*, sendo o ataque a *hashes* com sal, utilizando sais diferentes para *hashes* diferentes, o mais demorado.

Assim, tal como é possível verificar, conclui-se que a adição de sal aumenta a complexidade temporal do ataque e, consequentemente, o tempo de execução do mesmo, mas não têm uma influência preponderante nem inviabiliza o ataque por força-bruta para valores pequenos de *n* e de *k*, como é o caso.

Neste caso concreto, sendo *n* = 20 e *k* = 256, a razão entre os tempos de execução dos dois ataques (0,03888/0,00157 = 24,8) coincide com a ordem de grandeza da razão teórica ((256 * 20 + 20<sup>2</sup>)/20<sup>2</sup> = 5520/400 = 13,8) e permite estimar que o ataque a *hashes* que utilizassem sais diferentes para cada palavra-passe seria cerca de (256 * 20<sup>2</sup>)/(256 * 20 + 20<sup>2</sup>) = 102400/5520 = 18,6 vezes mais demorado do que o segundo ataque e 256 vezes mais demorado do que o primeiro, o que, ainda assim, resultaria num tempo de execução inferior a 1 segundo (entre cerca de 0,4 e 0,7 segundos).

## 3

Tal como é possível verificar, os valores SHA-1 dos ficheiros `3-1.jpeg` e `3-2.jpeg` são diferentes, mas, depois de utilizar a ferramenta disponibilizada, obtêm-se os ficheiros `3-1.pdf` e `3-2.pdf` com o mesmo valor SHA-1, apesar de serem ficheiros diferentes, o que contraria a propriedade de resistência a colisões da função de *hash* SHA-1.

![3](/week5/images/3.png)

O ataque à função de *hash* SHA-1 utiliza técnicas de criptoanálise diferencial para conseguir gerar uma colisão.

Resumidamente, o ataque consiste em criar pequenas diferenças nos blocos de cada mensagem/ficheiro, de maneira a que essas diferenças se anulem no processo de construção da *hash*, conseguindo, assim, gerar *hashes* iguais para mensagens/ficheiros diferentes.
Assim, através da seleção de um vetor de distúrbio e da criação de um caminho diferencial não-linear, são determinadas as condições do ataque, que pode ser acelerado através do aproveitamento de *bits* neutros - cuja alteração quase não afeta as condições de colisão - e de *bits boomerang* - cuja alteração provoca um efeito em cadeia que leva à propagação das alterações -, e é possível gerar uma colisão.

Ainda assim, o ataque exige bastante poder computacional e processamento paralelo para conseguir passar de uma "quase-colisão" para uma colisão efetiva, mas é substancialmente mais rápido do que um ataque por força-bruta, sendo executado com sucesso em tempo útil/viável para mensagens/ficheiros de tamanho reduzido.

## 4

O programa em *Python* que gera uma chave secreta *k* e computa *h = SHA2(k || m)* para qualquer mensagem *m*, guardando *k*, *m* e *h* em ficheiros diferentes, encontra-se no ficheiro `4-1.py`.
O programa funciona para SHA256 e SHA512 e utiliza as funções da biblioteca `hashlib` para a geração da *hash*.

![4-1](/week5/images/4-1.png)

O programa em *Python* que lê *m* e *h* (mas não *k*) e gera *m'* e *h'*, guardando-os em ficheiros diferentes, encontra-se no ficheiro `4-2.py`.
O programa utiliza as funções da biblioteca `HashTools` para realizar um ataque de extensão de comprimento.

![4-2](/week5/images/4-2.png)

O programa em *Python* que se encontra no ficheiro `4-3.py` verifica se o ataque de extensão de comprimento foi bem-sucedido, isto é, se *m =/= m'* e se *SHA2(k || m') = h'*.

![4-3](/week5/images/4-3.png)

Tal como é possível verificar, o ataque de extensão de comprimento foi bem-sucedido porque foi possível computar uma *hash* correta/válida para uma mensagem e uma chave secreta sem conhecer essa chave, mas apenas a partir da extensão de comprimento de uma mensagem já existente.
