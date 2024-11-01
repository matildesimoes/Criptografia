# Week #5 Extra

## Q1: *Collision resistant Hash Functions*

Para determinar que construções de *hash H'* também são **resistentes a colisões**, precisamos de analisar cada uma delas com base nas propriedades da função de *hash H*.
*H* é uma função de *hash* **resistente a colisões** que produz *outputs* de 64 *bits*.

**Resistência a Colisões:** É computacionalmente inviável encontrar dois *inputs* distintos *m* e *m'* tais que *H(m) = H(m')*.

1. **H' = H(m) || H(m) || H(m)**
   - Concatena *H(m)* três vezes, resultando num *output* de 192 *bits*.
   - *H'(m) = H'(m')* se e só se *H(m) = H(m')*. Como *H* é resistente a colisões, então *H'* também é resistente a colisões.

2. **H' = H(m || m || m)**
   - Faz *hash* da concatenação de *m* três vezes.
   - Uma colisão *H(m || m || m) = H(m' || m' || m')* é equivalente a uma colisão *H(M) = H(M')*, sendo *M = m || m || m* e *M' = m' || m' || m'*. Assim, é resistente a colisões como *H*.

3. **H' = H(64)**
   - Uma função de *hash* constante que retorna sempre *H(64)*.
   - Todos os *inputs* mapeiam para o mesmo valor de *hash*, havendo colisões para quaisquer dois *inputs*, logo, não é resistente a colisões.
   - Por exemplo, *H'(0) = H(64)* e *H'(1) = H(64)*, sendo esta uma possível colisão.

4. **H' = H(m || 64)**
   - Concatena *m* com *64* antes de aplicar a função de *hash*.
   - Se *H* é resistente a colisões, então *H(m || 64)* também é resistente a colisões, porque encontrar *H(m || 64) = H(m' || 64)* é equivalente a encontrar *H(M) = H(M')*, sendo *M = m || 64* e *M' = m' || 64*. Como *H* é resistente a colisões, então *H'* também é resistente a colisões.

5. **H' = H(m)[0...10]**
   - Trunca a saída de 64 *bits* de *H(m)* para 11 *bits*.
   - Com apenas 11 *bits*, existem 2<sup>11</sup> = 2048 possíveis *outputs*, tornando fácil encontrar colisões, logo, não é resistente a colisões.

6. **H' = H(m[0...|m|-2])**
   - Faz *hash* de *m* após remover o último *bit*.
   - Dois *inputs* que difiram apenas no último *bit* vão gerar *hashes* iguais, o que torna a procura de colisões muito mais fácil, logo, não é resistente a colisões.
   - Por exemplo, *H'(00) = H(0)* e *H'(01) = H(0)*, sendo esta uma possível colisão.

7. **H' = H(m) || H(m XOR 1<sup>|m|</sup>)**
   - Concatena *H(m)* com *H(m XOR 1<sup>|m|</sup>)*.
   - Encontrar uma colisão requer encontrar *m* e *m'* distintos tais que *H(m) = H(m')* e *H(m XOR 1<sup>|m|</sup>)* = *H(m' XOR 1<sup>|m'|</sup>)*, o que é tão difícil quanto encontrar colisões em *H*, logo, é resistente a colisões.

8. **H' = H(m) se m = 0<sup>64</sup> ∧ m = 1<sup>64</sup>, H(m XOR 1<sup>|m|</sup>) caso contrário**
   - É sempre necessário computar *H(m XOR 1<sup>|m|</sup>)*, pois *m* não pode ser, simultaneamente, 0<sup>64</sup> e 1<sup>64</sup>.
   - Similar à alínea 7, depende da resistência a colisões de *H*, logo, é resistente a colisões.

**Construções Resistentes a Colisões:** 1, 2, 4, 7, 8

**Construções Não Resistentes a Colisões:** 3, 5, 6

## Q2: *Rho method to find Hash collisions*

### Verificação da Prova

Após detetar que *h'<sub>i+1</sub> = h<sub>i+1</sub>*, o próximo passo é encontrar a colisão. 

A ideia principal é que, ao encontrar um ponto onde as duas sequências se encontram, podem encontrar-se os dois *inputs* distintos que levam a este ponto de encontro, isto é, que resultam no mesmo *output* da função de *hash*.

Para encontrar estes dois *inputs*, basta iterar a partir do valor inicial *h<sub>1</sub>* e do ponto de encontro *h<sub>i</sub>* em que *h'<sub>i</sub> = h<sub>i</sub>*, sendo cada passo da iteração a aplicação única de *H*, isto é, *h<sub>i + 1</sub> = H(h<sub>i</sub>)* e *h'<sub>i + 1</sub> = H(h'<sub>i</sub>)*.

O ponto de encontro destas duas sequências distintas será a colisão da função de *hash*, isto é, *i* e *i'* tais que *H(h<sub>i</sub>) = H(h<sub>i'</sub>)* e *i* é diferente de *i'*.

O método Rho baseia-se no ***Pigeonhole Principle*** - que afirma que, dada uma função que mapeia *n* elementos em *m* elementos, com *n > m*, inevitavelmente ocorrerá pelo menos um caso em que dois elementos diferentes são mapeados no mesmo elemento, ou seja, uma colisão - e no **Algoritmo de Deteção de Ciclos de Floyd** ou **Algoritmo da Lebre e da Tartaruga** - que permite detetar esta colisão de forma eficiente.

- Como há um número finito de possíveis valores de *hash* 2<sup>n</sup> para uma função de *hash H* de *n bits*, ao iterar a aplicação da função de *hash* repetidamente, inevitavelmente existirá um ciclo.

- O método Rho utiliza duas sequências de iteração: a aplicação única de *H* e a aplicação dupla de *H*.

- Devido ao *Pigeonhole Principle*, essas duas sequências vão, inevitavelmente, encontrar-se dentro de um ciclo.

- Uma vez detetado o ciclo, é possível encontrar dois *inputs* distintos que levam ao mesmo valor de *hash*, ou seja, uma colisão, aplicando o Algoritmo de Deteção de Ciclos de Floyd ou Algoritmo da Lebre e da Tartaruga.

### Implementação do Código

O código implementado encontra-se no ficheiro `rho_exercise.py` e abaixo observa-se uma execução.

![2](images/q2.png)

- **Número Total de Valores de *Hash*:** *N = 2<sup>8 x L</sup>*.
  
- **Iterações Esperadas:** É esperado encontrar uma colisão depois de realizar $\sqrt{2^{8 \times L}}$ iterações.
Se *L* aumentar, tornando a *hash* maior e dificultando a procura por colisões, então o número de iterações necessárias para encontrar uma colisão aumenta exponencialmente.

   - Aproximadamente $\sqrt{2^{8 \times 5}} = \sqrt{2^{40}} = 2^{20} = 1.048.576$ iterações esperadas para *L = 5*.
  
- **Iterações Observadas:** O número de iterações observadas está próximo da expectativa teórica (iterações esperadas), tendo a mesma ordem de grandeza.
É normal existirem variações devido à natureza probabilística do programa, isto é, à aleatoriedade do valor inicial *h<sub>1</sub>*.

   - Aproximadamente $2.094.156$ iterações observadas para *L = 5*.
  
- **Tempo Gasto:** O tempo gasto é proporcional ao número de iterações realizadas, logo, se existir um aumento de L, o número de iterações aumenta e, consequentemente, o tempo gasto também.

   - Aproximadamente $20,04$ segundos para *L = 5*.

- **Tempo Esperado:** Como o número de iterações por segundo (para *L = 5*) é $2.094.156/20,04$ = $104.500$ *iterações/segundo* e são necessárias cerca de $\sqrt{2^{8 \times L}}$ iterações para encontrar uma colisão, então, o tempo esperado para encontrar uma colisão é cerca de $\sqrt{2^{8 \times L}}/104.500$ segundos.

   - Aproximadamente $10,04$ segundos para *L = 5*.

## Q3: *Weak ciphers*

A cifra por fluxo implementada no ficheiro `ciphersuite_fsr.py` utiliza um polinómio de grau 5 (x<sup>5</sup> + x<sup>4</sup> + 1) como LFSR, módulo 1009.

O processo de encriptação consiste em, dado um estado inicial aleatório, gerar uma chave que corresponde à concatenação sucessiva do *output* da aplicação da função de *hash* SHA256 ao *output* LFSR.
Depois, é efetuada a operação XOR da chave com a mensagem, resultando no texto cifrado.

O processo de desencriptação é o simétrico do processo de encriptação.

### 1

O polinómio x<sup>5</sup> + x<sup>4</sup> + 1 não é irredutível, pelo que não é primitivo.

Como tal, o período do LFSR vai ser menor do que o período máximo possível que, como o universo de valores possível é módulo 1009, seria 1009.

O código abaixo identifica o período máximo real do polinómio do LFSR, considerando todos os valores possíveis para o estado inicial (de 0 a 1008).

```python
F.<x> = GF(1009)[]
p = x^5 + x^4 + 1

def max_period(p, mod):
    periods = set()
    for x in range(mod):
        values = set()
        while True:
            values.add(x)
            x = p(x)
            if x in values:
                break
        periods.add(len(values))
    return max(periods)

period = max_period(p, 1009)
print("Período:", period)
```

```
Período: 75
```

Como o período é 75, o LFSR só pode tomar, no máximo, 75 estados diferentes.

Como tal, para um dado estado inicial *x* gerado pela função `gen()`, aleatoriamente entre 0 e 1008, o LFSR só percorre, no máximo, 75 estados até voltar ao estado inicial, pelo que, no máximo são geradas 75 chaves diferentes.

Se o atacante enviar para o oráculo de encriptação uma mensagem qualquer, o atacante vai receber essa mesma mensagem encriptada.
A encriptação é a operação XOR entre os *bits* da mensagem e da chave.

Assim, se o atacante mandar 75 mensagens *m*, vai obter 75 criptogramas *c* diferentes, a partir dos quais consegue obter a chave *k* usada para a encriptação, fazendo ***k = m XOR c***.

Deste modo, ao fazer 75 chamadas ao oráculo de encriptação, o atacante consegue obter as 75 chaves possíveis (correspondentes aos 75 estados do LFSR) e, assim, no desafio, testar cada uma das chaves para decifrar o criptograma recebido até obter uma decifração que, certamente, será a correta.

### 2

Para o ataque ser bem sucedido, é necessário fazer os seguintes passos:

1. Pedir a encriptação de 75 mensagens diferentes para obter as 75 chaves possíveis, fazendo a operação ***k = m XOR c***, tal como descrito anteriormente.

2. Enviar duas mensagens *m<sub>0</sub>* e *m<sub>1</sub>* ao oráculo de encriptação e receber uma delas encriptada *c<sub>b</sub>*, conforme o *bit b* amostrado aleatoriamente no início da experiência.

3. Adivinhar *b*, fazendo a operação *c<sub>b</sub> XOR k* com todas chaves obtidas anteriormente.
Se o resultado for igual a *m<sub>0</sub>* ou m<sub>1</sub>, então adivinha-se corretamente o *bit b*.

Com base nestas operações, o atacante pode determinar corretamente que mensagem foi encriptada, aumentando a probabilidade de acertar para 100% em vez de apenas 50% (acertar de forma uniformemente aleatória).

O ficheiro `ciphesuite_fsr.py` foi estendido para incluir a exemplificação deste algoritmo de ataque a esta experiência em código, de maneira a demonstrar o exposto, apresentando-se abaixo um exemplo de execução.

![2](/week5/images/q3.png)
