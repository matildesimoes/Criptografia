# Week #2 

### 1 

A probabilidade de cada valor de S ser produzido por D não igual para todos os valores.
Tendo em conta que C é um conjunto dos valores de 0 até 255 e S é um conjunto dos valores de 0 até 250 números, então o número 0,1,2,3 e 4 vão ser reproduzidos 2 vezes, o que aumenta a probabilidade de serem gerados por D, sabendo que D calcula o resto da divisão dos números de 0 a 255 por 251. Assim, a probabilidade de gerar os números de 0 a 4 é 2/256, enquanto que a probabilidade de gerar os números de 5 a 250 é 1/256.

O conjunto C é um conjunto de todos as bit strings de 64 bits.
2<sup>64</sup> mod 251 = 69, o que significa que o conjunto de números de 0 a 68 vai ser reproduzido 2<sup>64</sup> / 251 vezes, enquanto que o conjunto de números de 69 a 250 vai ser reproduzido 2<sup>64</sup> / 251 - 1 vezes.

Estas distribuições são uniforme?
Estas distribuições não são uniformes, porque a probabilidade de gerar cada número é diferente.


