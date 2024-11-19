# Tutorial #6

### 1 

- C = 20
- e = 13
- n = 77

Qual é a mensagem original?

Se n = 77, então p = 7 e q = 11.

$\phi$(n) = (p - 1)(q - 1) = 6 * 10 = 60

D = e<sup>-1</sup> mod $\phi$(n) => e * d = 1 mod $\phi$(n) => D = 37

M = C<sup>D</sup> mod n = 20<sup>37</sup> mod 77 = 48

### 2

- e = 65
- n = 2881

Qual é o d?

Se n = 2881, então p = 43 e q = 67.

$\phi$(n) = (p - 1)(q - 1) = 42 * 66 = 2772

D = e<sup>-1</sup> mod $\phi$(n) => e * d = 1 mod $\phi$(n) => D = 725

### 3

Não, não é seguro gerar apenas um novo **e** e um novo **d** mantendo o mesmo módulo **n**. Se a chave privada **d** original for comprometida, o atacante que conhece os valores antigos **e** e **d** pode calcular **$\phi$(n)**, pois **e * d ≡ 1 mod $\phi$(n)**. Tendo **$\phi$(n)** e **n**, é mais provável conseguir fatorizar **n** para encontrar os primos **p** e **q**.

Uma vez que o atacante tem **p** e **q**, pode calcular **$\phi$(n)** novamente e derivar qualquer novo par de chaves **e'** e **d'**. Portanto, para restabelecer a segurança, o Bob deve gerar um novo módulo **n** com novos primos **p** e **q** e novas chaves **e** e **d**.

### 4

Não, não é seguro que a Alice envie uma mensagem cifrada contendo apenas o número de telemóvel dela utilizando RSA, mesmo com um módulo **n** muito grande e seguro contra fatorização. O problema está no facto de que o número de telemóvel é um valor relativamente pequeno e previsível, o que torna o espaço de mensagens possíveis bastante limitado.

Um atacante pode explorar essa limitação realizando um ataque de força bruta ou um ataque de dicionário. Pode, assim, gerar uma lista de todos os possíveis números de telemóvel válidos (o que é viável, dado que números de telemóvel seguem formatos específicos e têm um comprimento limitado), cifrar cada um usando a chave pública do Bob e comparar o resultado com a mensagem. Quando encontrar uma correspondência, o atacante irá descobrir o número de telemóvel da Alice.

### 5

O algoritmo **Miller-Rabin** é poderoso para verificar se números grandes são primos de forma eficiente e com alta confiança. Embora seja probabilístico, a chance de um número composto ser identificado como primo pode se tornar negligenciável ao aumentar o número de iterações. 

O código está implementado no ficheiro **miller_rabin.py** e abaixo encontra-se um exemplo de utilização:

![Miller-Rabin](miller_rabin_example.png)




