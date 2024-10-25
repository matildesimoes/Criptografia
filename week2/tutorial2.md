# Tutorial #2 

## 1 

A probabilidade de cada valor em S ser produzido por D não é igual para todos os valores.

Tendo em conta que C é o conjunto todas as *bit strings* de comprimento 8, ou seja, de 0 até 2<sup>8</sup> - 1 = 255 e que S é o conjunto dos valores inteiros de 0 até 250, então os números 0, 1, 2, 3 e 4 (correspondentes a `251 (mod 251) = 0` até `255 (mod 251) = 4`) vão ser reproduzidos 2 vezes, o que aumenta a probabilidade de serem gerados por D, porque D calcula o resto da divisão dos números de 0 a 255 por 251.

Assim, a probabilidade de D gerar os números inteiros de 0 a 4 é 2/256, enquanto a probabilidade de D gerar os números inteiros de 5 a 250 é 1/256.

### Considere-se que o conjunto C é o conjunto de todas as *bit strings* de comprimento 64.

2<sup>64</sup> mod 251 = 69, o que significa que cada um dos números inteiros de 0 a 68 vai ser reproduzido 2<sup>64</sup> // 251 + 1 vezes, enquanto cada um dos números inteiros de 69 a 250 vai ser reproduzido 2<sup>64</sup> // 251 vezes, sendo `//` a divisão inteira.

Assim, a probabilidade de D gerar os números inteiros de 0 a 68 é (2<sup>64</sup> // 251 + 1) / 2<sup>64</sup>, enquanto a probabilidade de D gerar os números inteiros de 69 a 250 é (2<sup>64</sup> // 251) / 2<sup>64</sup>.

### Estas distribuições são uniformes?

Estas distribuições não são uniformes, porque, em ambos os casos, há números diferentes que têm probabilidades diferentes de serem gerados. Por exemplo, em ambos os casos, o número 0 é mais provável de ser gerado do que o número 100.

Uma forma de quantificar quão distantes estão as distribuições de serem uniformes é calcular a entropia de cada distribuição.
A entropia de uma distribuição uniforme é máxima, mas a entropia de uma distribuição não uniforme é menor.
O valor da entropia para a primeira distribuição é 7,96 *bits*, enquanto o valor da entropia para a segunda distribuição é 7,97 *bits*.

## 2

A probabilidade de cada valor em S ser produzido por D é igual para todos os valores.

Tendo em conta que C é o conjunto todas as *bit strings* de comprimento 8, ou seja, de 0 até 2<sup>8</sup> - 1 = 255, o resto da divisão de qualquer um desses valores por p = 2<sup>8</sup> = 256 é o próprio valor (porque 255 < 256), isto é, a operação `mod` não altera o valor de entrada.

Contudo, S é o conjunto dos valores inteiros de 0 até 250, o que implica que os valores que sejam gerados por D e sejam superiores a 250 (de 251 até 255) são descartados, por não fazerem parte desse conjunto.

Como os valores descartados gerados por D levam à repetição do processo de geração até ao resultado estar entre 0 e 250, então a probabilidade de cada valor em S ser gerado por D é 1/251.

### Considere-se que o conjunto C é o conjunto de todas as *bit strings* de comprimento 64.

2<sup>64</sup> mod 2<sup>8</sup> = 0 (são potências de base 2 e, por isso, divisíveis), o que significa que, como anteriormente, qualquer valor inteiro tem a mesma probabilidade de ser produzido por D, sendo que os valores superiores a 250 são descartados, por não fazerem parte do conjunto S.

Tal como anteriormente, como os valores descartados gerados por D implicam a repetição do processo de geração até ao resultado estar entre 0 e 250, então a probabilidade de cada valor em S ser gerado por D é 1/251.

### Estas distribuições são uniformes?

Estas distribuições são uniformes, porque a probabilidade de cada número ser gerado é a mesma.

## 3

O código utilizado para computar a entropia das distribuições é o seguinte.

```python	
def compute_entropy(prob_dict):
    entropy = 0.0
    
    for prob, count in prob_dict.items():
        for _ in range(count):
            if prob > 0:
                entropy -= prob * log(prob, 2)
    
    return entropy

# Distribuição 1 (k = 8)
prob1 = 2/256
prob2 = 1/256
prob_dict1 = {prob1: 5, prob2: 246}

# Distribuição 2 (k = 64)
prob3 = int(2**64 / 251 + 1) / 2**64
prob4 = int(2**64 / 251) / 2**64
prob_dict2 = {prob3: 69, prob4: 182}

# Distribuição Uniforme sobre S
prob5 = 1 / 251
prob_dict3 = {prob5: 251}

entropy1 = compute_entropy(prob_dict1).n()
entropy2 = compute_entropy(prob_dict2).n()
entropy3 = compute_entropy(prob_dict3).n()

print("Entropia da Distribuição 1 (k = 8):", entropy1)
print("Entropia da Distribuição 2 (k = 64):", entropy2)
print("Entropia da Distribuição Uniforme sobre S:", entropy3)
```

O resultado obtido no `Sage` é o seguinte.

```
Entropia da Distribuição 1 (k = 8): 7.96093750000000
Entropia da Distribuição 2 (k = 64): 7.97154355395077
Entropia da Distribuição Uniforme sobre S: 7.97154355395077
```

## 4

Generalizando o código anterior para computar a entropia da distribuição D quando C é o conjunto das *bit strings* de comprimento `k`, obtém-se o seguinte código.

```python
def prob(s, p, k):
    n = 2 ** k
    return (n // p + (s < (n % p)))/n

def entropy(ss, p, k):
    e = 0
    for s in ss:
        ps = prob(s, p, k)
        if ps > 0:
            e -= ps * log(ps, 2)
    return e

ss = range(251)
p = 251
k1 = 8
k2 = 64

entropy1 = entropy(ss, p, k1).n()
entropy2 = entropy(ss, p, k2).n()

print("Entropia da Distribuição 1 (k = 8):", entropy1)
print("Entropia da Distribuição 2 (k = 64):", entropy2)
```

O resultado obtido no `Sage` é o seguinte.

```
Entropia da Distribuição 1 (k = 8): 7.96093750000000
Entropia da Distribuição 2 (k = 64): 7.97154355395077
```

Para verificar qual é o `k` mais pequeno para o qual a entropia computada no `Sage` corresponde à entropia da distribuição uniforme sobre S, utiliza-se o seguinte código.

```python
def mink(ss, p, maxk, maxentropy, error):
    for k in range(maxk):
        if maxentropy - entropy(ss, p, k) <= error:
            return k

print("k =", mink(range(251), 251, 64, 7.97154355395077, 0.01))
print("k =", mink(range(251), 251, 64, 7.97154355395077, 0.001))
print("k =", mink(range(251), 251, 64, 7.97154355395077, 0.0001))
```

O resultado obtido no `Sage` é o seguinte.

```
k = 9
k = 12
k = 14
```

## 5

O comando `hexdump -n 32 -e '1/4 "%0X" 1 "\n"' /dev/urandom` extrai, formata e mostra em hexadecimal valores provenientes do ficheiro `/dev/urandom`, que é o gerador pseudo-aleatório dos sistemas Unix/Linux.

![hexdump -n 32 -e '1/4 "%0X" 1 "\n"' /dev/urandom](/week2/images/5-1.png)

`-n 32` **-** Esta opção limita o número de *bytes* a ler do ficheiro a 32. Sem esta opção, o comando iria extrair e mostrar continuamente valores do ficheiro `/dev/urandom`.

`-e '1/4 "%0X" 1 "\n"'` **-** Esta opção especifica a *string* de formatação para o *output*, ou seja, define o formato com que os dados são mostrados. A *string* de formatação `1/4 "%0X" 1 "\n"` significa que o comando deve tratar cada conjunto de 4 *bytes* como uma unidade (`1/4`), formatá-los/mostrá-los em hexadecimal, em letras maiúsculas e, se necessário, com zeros à esquerda, para cada valor ocupar 8 caracteres (`"%0X"`), e separar unidades com um nova linha entre elas, para que cada conjunto de 4 *bytes* fique numa linha separada (`"\n"`).

`/dev/urandom` **-** Este é o ficheiro do qual são extraídos os valores pelo comando. O ficheiro `/dev/urandom` é o gerador pseudo-aleatório de *bytes* dos sistemas Unix/Linux, normalmente utilizado para fins criptográficos.

Assim, o comando `hexdump -n 32 -e '1/4 "%0X" 1 "\n"' /dev/urandom`:
1. Lê 32 *bytes* do ficheiro `/dev/urandom`, que os gera de forma pseudo-aleatória;
2. Interpreta esses 32 *bytes* como 8 conjuntos/uidades de 4 *bytes*;
3. Formata cada conjunto/unidade de 4 *bytes* como uma *string* hexadecimal de 8 caracteres maiúsculos;
4. Mostra cada uma das 8 *strings* hexadecimais numa linha separada das restantes.

Um comando alternativo que usa `/dev/urandom` para criar um ficheiro com *bytes* aleatórios é `dd if=/dev/urandom bs=1 count=32 | xxd -u -p -c 4 > file.txt`.

Este comando executa dois comandos e envia o *output* do primeiro para o *input* do segundo. O primeiro comando copia 32 *bytes* do ficheiro `/dev/urandom` e o segundo comando formata esses 32 *bytes* como valores hexadecimais em caracteres maiúsculos e com 4 *bytes* por linha, guardando o *output* no ficheiro `file.txt`.

![dd if=/dev/urandom bs=1 count=32 | xxd -u -p -c 4 > file.txt](/week2/images/5-2.png)

Outro comando alternativo que faz exatamente o mesmo, usando OpenSSL, é `openssl rand -hex 32 | fold -w 8 | tr 'a-f' 'A-F' > file.txt`.

De forma semelhante ao anterior, este comando executa três comandos e envia o *output* de cada um para o *input* do seguinte. O primeiro comando gera 32 *bytes* usando um gerador pseudo-aleatório e criptograficamente seguro de números, mostrando o *output* numa *string* hexadecimal, enquanto o segundo comando recebe esses 32 *bytes* e coloca uma nova linha entre cada conjunto de 8 *bytes* consecutivos. Finalmente, o terceiro comando apenas converte os caracteres hexadecimais minúsculos em maiúsculos, guardando o *output* no ficheiro `file.txt`.

![openssl rand -hex 32 | fold -w 8 | tr 'a-f' 'A-F' > file.txt](/week2/images/5-3.png)

## 6

O comando `openssl genrsa 4096` gera uma chave privada RSA com 4096 *bits*.

![openssl genrsa 4096](/week2/images/6-1.png)

Para gerar um par de chaves em que a chave privada está protegida com uma palavra-passe, é necessário correr dois comandos:

**1.** `openssl genrsa -aes256 -passout pass:password -out privatekey.pem -verbose 4096` 

Este comando gera uma chave privada RSA com 4096 *bits*, encriptada com o algoritmo AES (usando uma chave de 256 *bits*) e protegida com a palavra-passe `password`, armazenando-a no ficheiro `privatekey.pem`.

![openssl genrsa -aes256 -passout pass:password -out privatekey.pem -verbose 4096](/week2/images/6-2.png)

Ao contrário do comando corrido anteriormente, este já encriptou a chave privada e protegeu-a com uma palavra-passe, como é visível através do texto `BEGIN/END ENCRYPTED PRIVATE KEY` em vez de `BEGIN/END PRIVATE KEY`.

**2.** `openssl rsa -in privatekey.pem -out publickey.pem -passin pass:password -pubout`

Este comando extrai a chave pública RSA correspondente à chave privada presente no ficheiro `privatekey.pem` e protegido com a palavra-passe `password`, armazenando-a no ficheiro `publickey.pem`.

![openssl rsa -in privatekey.pem -out publickey.pem -passin pass:password -pubout](/week2/images/6-3.png)

Agrupando os dois comandos num único comando que os executa sequencialmente e medindo o tempo de execução de cada um, é possível verificar o que sucede quando se aumenta/diminui o tamanho da chave.

Assim, correu-se o comando `time openssl genrsa -aes256 -passout pass:password -out privatekey.pem -verbose <k> && time openssl rsa -in privatekey.pem -out publickey.pem -passin pass:password -pubout` (substituindo `<k>` pelo tamanho da chave, em *bits*). Expõem-se os resultados na tabela abaixo.

| Tamanho da Chave (*bits*) | Tempo de Execução do Comando 1 (*s*) | Tempo de Execução do Comando 2 (*s*) |
| - | - | - |
| 512 | 0.014 | 0.007 |
| 1024 | 0.019 | 0.006 |
| 2048 | 0.317 | 0.005 |
| 4096 | 1.479 | 0.005 |
| 8192 | 16.421 | 0.005 |
| 16384 | 179.052 | 0.005 |

Ao analisar os valores presentes na tabela, conclui-se que o tempo de execução para a geração da chave privada (Comando 1) aumenta - aparentemente de forma polinominal - com o aumento do tamanho da chave, mas o tempo de execução para a extração da chave pública a partir da chave privada (Comando 2) permanece constante, sendo independente do tamanho da chave.

O OpenSSL converte a palavra-passe numa chave criptográfica usando uma função de derivação de chave, de modo a garantir que a chave criptográfica resultante da palavra-passe pode ser utilizada para encriptação/embrulho da chave privada.

Assim, a função de derivação de chave recebe a palavra-passe, um sal aleatório e o comprimento pretendido para a chave, retornando uma chave criptográfica simétrica, usada para encriptar ou embrulhar a chave privada. A função de derivação de chave recorre a uma função de *hash* criptográfica para cumprir o seu propósito.

Atualmente, em versões modernas do OpenSSL, a função de derivação de chave mais utilizada para este efeito é a `PBKDF2` (*Password-Based Key Derivation Function 2*), que costuma recorrer à função de *hash* `HMAC-SHA256`.

## 7

O comando `openssl dhparam 2048` gera parâmetros aleatórios Diffie-Hellman.

![openssl dhparam 2048](/week2/images/7.png)

Para verificar o que sucede quando se aumenta/diminui o tamanho da chave, correu-se o comando `time openssl dhparam -out dhparam.pem <k>` (substituindo `<k>` pelo tamanho dos parâmetros, em *bits*). Expõem-se os resultados na tabela abaixo.

| Tamanho dos Parâmetros (*bits*) | Tempo de Execução (*s*) |
| - | - | 
| 512 | 0.141 |
| 1024 | 4.019 |
| 2048 | 34.720 |
| 4096 | 403.477 |

Ao analisar os valores presentes na tabela, conclui-se que o tempo de execução para a geração dos parâmetros aumenta - aparentemente de forma polinomial - com o aumento do tamanho dos parâmetros.

Comparando este caso com o caso anterior, conclui-se que a geração de parâmetros aleatórios Diffie-Hellman é muito mais demorada do que a geração de um par de chaves (em que a chave privada está protegida com uma palavra-passe). Isto poderá dever-se ao facto de ser necessário computar números primos de maior dimensão/magnitude para a geração de parâmetros aleatórios Diffie-Hellman do que aqueles que são necessários para a geração de um par de chaves RSA.
