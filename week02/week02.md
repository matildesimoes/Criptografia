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

import math

def compute_entropy(probabilities):
    """
    Compute the entropy given a list of probabilities.
    
    :param probabilities: List of probabilities for each event S'.
    :return: Entropy value.
    """
    entropy = 0.0
    for prob in probabilities:
        if prob > 0:  # To avoid log(0) which is undefined
            entropy -= prob * math.log2(prob)
    return entropy

# Example usage:
probabilities = []  # Example probabilities
entropy_value = compute_entropy(probabilities)
print(f"Entropy: {entropy_value}")




