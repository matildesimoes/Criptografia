# Week #2 

### 1 

A probabilidade de cada valor de S ser produzido por D não igual para todos os valores.
Tendo em conta que C é um conjunto dos valores de 0 até 255 e S é um conjunto dos valores de 0 até 250 números, então o número 0,1,2,3 e 4 vão ser reproduzidos 2 vezes, o que aumenta a probabilidade de serem gerados por D, sabendo que D calcula o resto da divisão dos números de 0 a 255 por 251. Assim, a probabilidade de gerar os números de 0 a 4 é 2/256, enquanto que a probabilidade de gerar os números de 5 a 250 é 1/256.

O conjunto C é um conjunto de todos as bit strings de 64 bits.
2<sup>64</sup> mod 251 = 69, o que significa que o conjunto de números de 0 a 68 vai ser reproduzido 2<sup>64</sup> // 251 + 1 vezes, enquanto que o conjunto de números de 69 a 250 vai ser reproduzido 2<sup>64</sup> // 251 vezes. A probabilidade de gerar os números de 0 a 68 é (2<sup>64</sup> // 251 + 1) // 2<sup>64</sup>, enquanto que a probabilidade de gerar os números de 69 a 250 é (2<sup>64</sup> // 251) // 2<sup>64</sup>.

Estas distribuições são uniforme?
Estas distribuições não são uniformes, porque há números com probabilidades diferentes de serem gerados. Uma forma de quantificar quão distantes estão as distribuições de serem uniformes é calcular a entropia de cada distribuição. A entropia de uma distribuição uniforme é máxima, enquanto que a entropia de uma distribuição não uniforme é menor. O valor da entropia para a primeira distribuição é 7,96 bits, enquanto que o valor da entropia para a segunda distribuição é 7,97 bits.

### 2

A probabilidade de cada valor de S ser produzido por D é igual para todos os valores.
Tendo em conta que C é um conjunto dos valores de 0 até 255, o resto da divisão de qualquer um desses valor por p=256 é o próprio valor, isto a operação mod não altera o valor de entrada. Contudo, S é um conjunto dos valores de 0 até 250 números, o que implica que os valores que saiam de D superiores a 250 (251 a 255) serão descartados e haverá uma repetição do processo até o número estar entre 0 e 250. Portanto, a probabilidade de cada valor de S ser gerado por D é 1/251. 

O conjunto C é um conjunto de todos as bit strings de 64 bits.
2<sup>64</sup> mod 2<sup>8</sup> = 0 (são pontências de base 2 e por isso divisíveis), o que significa que, como anteriormente, qualquer valor tem a mesma probabilidade de ser produzido por D sendo que os valores superiores a 250 são descartados, implicando o repetição do processo. Assim, a probabilidade de cada valor de S ser gerado por D é 1/251.

Estas distribuições são uniforme?
Estas distribuições são uniformes, porque a probabilidade de cada número ser gerado é a mesma.

### 3

```python	
def compute_entropy_from_prob_and_counts(prob_dict):
   
    entropy = 0.0
    
    for prob, count in prob_dict.items():
        for _ in range(count):
            if prob > 0:
                entropy -= prob * math.log2(prob)
    
    return entropy

# exercício 1
result1 = 2/256
result2 = 1/256
prob_dict1 = {result1: 5, result2: 246}

# exercício 2
result3 = int(2**64 / 251 + 1) / 2**64
result4 = int(2**64 / 251) / 2**64
prob_dict2 = {result3: 69, result4: 182}

entropy_value1 = compute_entropy_from_prob_and_counts(prob_dict1)
entropy_value2 = compute_entropy_from_prob_and_counts(prob_dict2)

print(f"Entropia da distribuição 1: {entropy_value1}")
print(f"Entropia distribuição 2: {entropy_value2}")
```
Entropia da distribuição 1: 7.96093750000000
Entropia da distribuição 2: 7.97154355395077

```python	
def compute_entropy_from_prob_and_counts(prob_dict):
   
    entropy = 0.0
    
    for prob, count in prob_dict.items():
        for _ in range(count):
            if prob > 0:
                entropy -= prob * math.log2(prob)
    
    return entropy

# uniforme distribuição de S
result1 = 1 / 2
prob_dict2 = {result1: 2}

entropy_value1 = compute_entropy_from_prob_and_counts(prob_dict2)

print(f"Entropia da distribuição 1: {entropy_value1}")
```
Entropia da distribuição 1: 7.96093750000000

### 4

```python	
def compute_entropy_uniform(prob_dict):
   
    entropy = 0.0
    
    for prob, count in prob_dict.items():
        for _ in range(count):
            if prob > 0:
                entropy -= prob * math.log2(prob)
    
    return entropy

for k in range(1, 100):

    result1 = 2**k mod 251
    result2 = 2**k - result1
    prob_dict2 = {result1: 2**k // 251 + 1, result2: (2**k // 251) // 2**k}

    entropy = compute_entropy_uniform(prob_dict2)

    print(f"Entropia uniforme para k={k}: {entropy:.5f}")
```
k=8

### 5

O comando usa o hexdump para extrair e formatar dados aleatórios do dispositivo /dev/urandom, que é uma fonte de dados pseudo-aleatórios em sistemas Unix.

```bash
$ hexdump -n 32 -e '1/4 "%0X" 1 "\n"' /dev/urandom
```

**-n 32**:

Este parâmetro limita em 32 bytes o número de bytes que o hexdump lê do /dev/urandom. Sem esta opção, o hexdump iria continuar a ler do /dev/urandom.

**-e '1/4 "%0X" 1 "\n"'**:

A opção -e específica a string de formatação para o output, ou seja, dita a forma como ao hexdump vai mostrar os dados. Isso significa que o hexdump deve processar 4 bytes (32 bits) de cada vezes.

**"%0X"**: 

Especifica como formatar os 4 bytes. O formato "%0X" imprime o pedaço como um número hexadecimal em maiúsculas, sem espaços à frente. 0X garante o preenchimento com zeros, de modo que cada pedaço seja impresso como 8 caracteres hexadecimais (32 bits).
1 "\n": Isso especifica que, após processar cada objeto, uma nova linha (\n) deve ser impressa. Isso garante que cada valor hexadecimal de 4 bytes seja impresso em uma nova linha.

**/dev/urandom**:

O /dev/urandom é um arquivo especial que fornece um fluxo infinito de bytes pseudo-aleatórios. Ele é normalmente usado para fins criptográficos, embora seja considerado menos seguro que o /dev/random quando a entropia é baixa.
Saída:
O comando irá:

Ler 32 bytes de dados aleatórios do /dev/urandom.
Interpretar esses bytes como oito pedaços de 4 bytes (32 bytes / 4 bytes por pedaço = 8 pedaços).
Converter cada pedaço de 4 bytes em uma string hexadecimal de 8 caracteres.
Imprimir cada string hexadecimal em uma nova linha.