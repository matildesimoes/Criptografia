# Tutorial #6

### 1 

- C = 20
- e = 13
- n = 77

Qual é a mensagem original?

Se n = 77, então p = 7 e q = 11.

$\phi$(n) = (p-1)(q-1) = 6 * 10 = 60

D = e^-1 mod phi(n) => ed = 1 mod phi(n) => D = 37

M = C^D mod n = 20^37 mod 77 = 48

### 2

- e = 65
- n = 2881

Qual é o d?

Se n = 2881, então p = 43 e q = 67.

$\phi$(n) = (p-1)(q-1) = 42 * 66 = 2772

D = e^-1 mod phi(n) => ed = 1 mod phi(n) => D = 725

### 3

Mudando só o *e* e o *d* quando a chave privada for revelada, não é suficiente para garantir a segurança do RSA, porque o atacante pode usar o antigo *e* e *d* para reduzir o conjunto de procura de valores possíveis para o $\phi$(n).

### 4

Não é seguro porque o atacante pode fazer um ataque de dicionário para descobrir a mensagem original, ou seja, ele pode tentar todos os números possíveis cifrados e comparar com a mensagem cifrada, conseguindo encontrar o número original quando as mensagens cifradas forem iguais.

### 5






