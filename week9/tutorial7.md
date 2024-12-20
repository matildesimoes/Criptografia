# Tutorial #7

## 1

O código que computa os logaritmos discretos é o seguinte.

```python
def discrete_logarithm(base, a, mod):
    group = IntegerModRing(mod)
    
    base = group(base)
    a = group(a)
    
    x0 = discrete_log(a, base)
    
    ord_base = base.multiplicative_order()
    
    solutions = [(x0 + k * ord_base) % (mod - 1) for k in range((mod - 1) // ord_base)]
    
    return solutions

discrete_logarithm(2, 13, 23)
discrete_logarithm(10, 22, 47)
discrete_logarithm(627, 608, 941)
```

O resultado obtido no `Sage` é o seguinte.

```python
[7, 18]
[11]
[18]
```

### a

$\{x: x \in \mathbb{Z_{23}} \wedge x = log_{2}(13)\} = \{x: 2^x \equiv 13 \pmod{23}\} = \{7, 18\}$

### b

$\{x: x \in \mathbb{Z_{47}} \wedge x = log_{10}(22)\} = \{x: 10^x \equiv 22 \pmod{47}\} = \{11\}$

### c

$\{x: x \in \mathbb{Z_{941}} \wedge x = log_{627}(608)\} = \{x: 627^x \equiv 608 \pmod{941}\} = \{18\}$

## 2

- $p = 1373$
- $g = 2$
- $A = 974$
- $b = 871$

### Qual é o valor $B$ que o Bob deve enviar para a Alice?

$$B \equiv g^b \pmod{p}$$
$$B \equiv 2^{871} \pmod{1373}$$
$$B \equiv 805 \pmod{1373}$$

O valor que o Bob deve enviar para a Alice é $B = 805$.

### Qual é o valor secreto partilhado?

$$g^{ab} \equiv A^b \pmod{p}$$
$$g^{ab} \equiv 974^{871} \pmod{1373}$$
$$g^{ab} \equiv 397 \pmod{1373}$$

O valor secreto partilhado é $g^{ab} = 397$.

### Qual é o expoente secreto usado pela Alice?

$$B^a \equiv g^{ab} \pmod{p}$$
$$805^a \equiv 397 \pmod{1373}$$
$$a \equiv 587 \pmod{1373}$$

O expoente secreto usado pela Alice é $a = 587$.

### Verificação

$$A^b \equiv B^a \equiv g^{ab} \pmod{p}$$
$$974^{871} \equiv 805^{587} \equiv 2^{587 \times 871} \pmod{1373}$$
$$974^{871} \equiv 805^{587} \equiv 2^{511277} \pmod{1373}$$
$$397 \equiv 397 \equiv 397 \pmod{1373}$$

A congruência é verdadeira, portanto os resultados estão corretos.

## 3

- $p$ primo
- $g \in \mathbb{Z_p}$

Se os participantes enviassem um ao outro $x^g \mod{p}$ em vez de $g^x \mod{p}$, então:
- A Alice escolheria $a$ e enviaria ao Bob $A = a^g \mod{p}$
- O Bob escolheria $b$ e enviaria à Alice $B = b^g \mod{p}$

Assim, os participantes **não** poderiam concordar numa chave de forma idêntica à do protocolo Diffie-Hellman, porque:
- $A^b \equiv (a^g)^b \equiv a^{gb} \pmod{p}$
- $B^a \equiv (b^g)^a \equiv b^{ga} \pmod{p}$
- $a^{gb} \not\equiv b^{ga} \pmod{p}$

Contudo, a Alice e o Bob poderiam concordar numa chave através da aplicação de uma função previamente estabelecida aos valores partilhados, como, por exemplo, $f(A, B) = A^B$ ou $f(A, B) = B^A$ ou $f(A, B) = A \times B$, entre inúmeras possibilidades.

No entanto, esta função não resultaria, evidentemente, num chave secreta segura, dado que a computação da chave se poderia realizar por qualquer atacante passivo que estivesse à escuta no canal de comunicação aberto/partilhado.

Deste modo, a Eve conseguiria quebrar o sistema sem encontrar os números secretos, porque a chave secreta só dependeria dos valores públicos.

Todavia, mesmo que a chave secreta não dependesse exclusivamente dos valores públicos, mas também dos valores privados, a Eve conseguiria sempre quebrar o sistema, porque conseguiria encontrar os números secretos.

Efetivamente, a Eve conseguiria encontrar os números secretos através da aplicação da raiz índice-g aos valores partilhados, isto é:
- $\sqrt[g]{A} \equiv \sqrt[g]{a^g} \equiv a \pmod{p}$
- $\sqrt[g]{B} \equiv \sqrt[g]{b^g} \equiv b \pmod{p}$

Como este problema não é tão difícil como o problema do logaritmo discreto, a Eve conseguiria encontrar os números secretos.

Para além disto, considerando as dimensões/magnitudes e ordens de grandeza dos valores típicos para os parâmetros públicos do protocolo Diffie-Hellman, tenderá a ser muito mais fácil computar $x^g \mod{p}$ do que $g^x \mod{p}$, dado que, para o caso típico em que $x >> g$, então $x^g << g^x$, o que diminui substancialmente o tempo de processamento computacional necessário.

Em suma, este sistema não pode ser considerado seguro, porque não existe um método de estabelecimento da chave de forma segura.
