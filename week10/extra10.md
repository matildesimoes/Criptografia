# Week #10 Extra

## Q1: *Man-in-the-Middle*

O ficheiro `mitm.py` implementa um protótipo que demonstra como um ataque *Man-in-the-Middle* pode ocorrer numa troca de chaves usando o protocolo Diffie-Hellman não autenticado, contendo o código para o adversário.
O código convence a Alice e o Bob a falarem com o adversário - em vez de falarem um com outro - e a realizarem uma troca de chaves com ele.

O fluxo de execução do código que realiza o ataque expõe-se abaixo.

O adversário:
1. Recebe $B = g^y$ do Bob;
2. Escolhe um expoente aleatório $c$;
3. Envia $C = g^c$ para a Alice;
4. Recebe $A = g^x$ da Alice;
5. Escolhe um expoente aleatório $d$;
6. Envia $D = g^d$ para o Bob;
7. Computa o segredo partilhado com a Alice: $A^c = (g^x)^c = g^{xc} = g^{cx} = (g^c)^x = C^x$;
8. Computa o segredo partilhado com o Bob: $B^d = (g^y)^d = g^{yd} = g^{dy} = (g^d)^y = D^y$.

Abaixo, apresenta-se um exemplo de execução.

![alice.py](images/q1-1.png)

A Alice concorda com o segredo $2475459418$.

![bob.py](images/q1-2.png)

O Bob concorda com o segredo $5646322207$.

Efetivamente, a Alice e o Bob não concordam no mesmo segredo, porque $2475459418 \neq 5646322207$.

![mitm.py](images/q1-3.png)

O adversário conhece o segredo partilhado com a Alice ($2475459418$) e o segredo partilhado com o Bob ($5646322207$).

Portanto, ambos os segredos concordados são conhecidos pelo adversário.

Assim, como a Alice e o Bob não concordam no mesmo segredo e ambos os segredos concordados são conhecidos pelo adversário, realizou-se um ataque *Man-in-the-Middle* com sucesso.

## Q2: *ECC*

Considere-se a seguinte construção para um esquema de assinatura com curvas elípticas:

- **Gerar a Chave Pública:** computar $pk_A \leftarrow sk_A \cdot G$, sendo $G$ um gerador
- **Assinar:** computar $\sigma \leftarrow m - k \cdot sk_A \cdot G$, sendo $k$ um valor aleatório
- **Verificar:** computar $m' = \sigma + k \cdot pk_A$ e aceitar se $m = m'$

### P1

Pretende-se mostrar que este esquema funciona, isto é, que para mensagens corretamente assinadas, o algoritmo de verificação funciona corretamente.

Seja $m$ uma mensagem corretamente assinada.

Seja $m'$ a tentativa de verificação da mensagem $m$:
$$m' = \sigma + k \cdot pk_A$$
Como $\sigma \leftarrow m - k \cdot sk_A \cdot G$:
$$m' = m - k \cdot sk_A \cdot G + k \cdot pk_A$$
Como $pk_A \leftarrow sk_A \cdot G$:
$$m' = m - k \cdot sk_A \cdot G + k \cdot sk_A \cdot G$$
Como $k \cdot sk_A \cdot G - k \cdot sk_A \cdot G = 0$:
$$m' = m$$

Portanto, a verificação é bem-sucedida.

Assim, está provado que este esquema funciona, isto é, que para mensagens corretamente assinadas, o algoritmo de verificação funciona corretamente.

### P2

Pretende-se mostrar que este esquema é vulnerável, ao descrever uma técnica simples para forjar uma assinatura numa mensagem arbitrária, sem conhecimento da chave secreta $sk_A$.

Seja $m$ uma mensagem arbitrária.

Um atacante, conhecendo a chave pública da vítima ($pk_A$), pode computar o valor $\sigma \leftarrow m - k \cdot pk_A$ e enviá-lo como uma assinatura para a mensagem $m$.

Efetivamente, ao verificar a assinatura $\sigma \leftarrow m - k \cdot pk_A$ para a mensagem $m$, obtém-se:
$$m' = \sigma + k \cdot pk_A$$
$$m' = m - k \cdot pk_A + k \cdot pk_A$$
$$m' = m$$

Portanto, a verificação é bem-sucedida.

Assim, está provado que este esquema é vulnerável, porque o atacante conseguiu forjar uma assinatura válida para uma mensagem arbitrária, sem conhecimento da chave secreta $sk_A$.

Efetivamente, a vulnerabilidade surge porque o processo de computar a assinatura $\sigma \leftarrow m - k \cdot sk_A \cdot G$ é equivalente a computar $\sigma \leftarrow m - k \cdot pk_A$, dado que $pk_A \leftarrow sk_A \cdot G$, pelo processo de geração da chave pública.

Como tal, o valor $k \cdot sk_A \cdot G$ é igual a $k \cdot pk_A$, pelo que pode ser computado apenas com o conhecimento da chave pública $pk_A$, sem ser necessário o conhecimento da chave secreta $sk_A$.

Deste modo, qualquer atacante consegue forjar assinaturas válidas sem o conhecimento da chave secreta $sk_A$, mas apenas com o conhecimento a chave pública $pk_A$, tornando este esquema vulnerável.

## Q3: *ElGamal*

Considere-se o esquema de encriptação com chave pública *ElGamal*, isto é:

**Geração de Chaves:** $Gen()$
- $x \leftarrow_\$ \{1, ..., (q - 1)\}$
- $X \leftarrow g^x$
- *Return* $(X, x)$

**Encriptação:** $Enc(X, m)$
- $y \leftarrow_\$ \{1, ..., (q - 1)\}$
- $s \leftarrow X^y$
- $Y \leftarrow g^y$
- $c \leftarrow m \cdot s$
- *Return* $(Y, c)$

**Desencriptação:** $Dec(x, (Y, c))$
- $s \leftarrow Y^x$
- $m \leftarrow c \cdot s^{-1}$
- *Return* $m$

Considerem-se todas as operações no grupo $\mathbb{Z}_q$ e sejam:
- $g$ um parâmetro público (gerador);
- $s$ o segredo partilhado estabelecido;
- $x$ a chave privada do recetor;
- $X$ a chave pública do recetor;
- $y$ um valor amostrado aleatoriamente pelo emissor a partir do conjunto $\mathbb{Z}_ q$.

### P1

O esquema de encriptação *ElGamal* funciona através do estabelecimento de um segredo partilhado ($s$) que é utilizado para encriptar e desencriptar a mensagem, de forma semelhante a um *one-time pad*.

A desencriptação funciona ao computar o produto do criptograma $c$ com o inverso multiplicativo do segredo partilhado $s$.

Ora, como o criptograma $c$ corresponde ao produto da mensagem original $m$ com o segredo partilhado $s$, o produto de $s$ pelo seu inverso multiplicativo (no grupo $\mathbb{Z}_ q$) resulta no elemento neutro para a multiplicação (a identidade), pelo que se obtém a mensagem original.

Assim, a prova de que a desencriptação recupera a mensagem original $m$ é a seguinte:

$$Dec(x, (Y, c))$$
$$m' \leftarrow c \cdot s^{-1}$$
$$m' \leftarrow (m \cdot s) \cdot s^{-1}$$
$$m' \leftarrow m \cdot s \cdot s^{-1}$$
$$m' \leftarrow m$$

Ou, equivalentemente:

$$Dec(x, (Y, c))$$
$$m' \leftarrow c \cdot s^{-1}$$
$$m' \leftarrow (m \cdot s) \cdot (Y^x)^{-1}$$
$$m' \leftarrow m \cdot X^y \cdot ((g^y)^x)^{-1}$$
$$m' \leftarrow m \cdot (g^x)^y \cdot (g^{xy})^{-1}$$
$$m' \leftarrow m \cdot g^{xy} \cdot g^{-xy}$$
$$m' \leftarrow m$$

Note-se que o inverso multiplicativo de $s$ (no grupo $\mathbb{Z}_ q$) pode ser computado de múltiplas formas, nomeadamente através da utilização do algoritmo de Euclides estendido.

A desencriptação funciona porque o valor de $y$ só é computado/conhecido pelo emissor e o valor de $x$ só é computado/conhecido pelo recetor, mas, pelas propriedades da aritmética, $X^y = (g^x)^y = g^{xy} = g^{yx} = (g^y)^x = Y^x$, sendo os valores de $g$, $X$ e $Y$ públicos e conhecidos por ambas as partes.

### P2

A dificuldade do logaritmo discreto garante confidencialidade porque, ainda que um atacante à escuta no canal de comunicação aberto/partilhado consiga intersetar $Y$ e $c$ e conheça $X$ (por ser a chave pública do recetor) e $g$ (por ser um parâmetro público), não consegue, em tempo útil/viável, obter a mensagem original $m$, admitindo que o problema do logaritmo discreto é computacionalmente difícil.

Isto sucede porque:
1. Mesmo que o atacante intersete $Y$ e conheça $g$, computar o valor de $y$ tal que $g^y \equiv Y \pmod{q}$ corresponde a resolver o problema do logaritmo discreto.
2. Mesmo que o atacante conheça $X$ e conheça $g$, computar o valor de $x$ tal que $g^x \equiv X \pmod{q}$ corresponde a resolver o problema do logaritmo discreto.

Como tal, a não ser que resolva o problema do logaritmo discreto, o atacante não consegue computar o valor de $y$ nem o valor de $x$.

Sem o valor de $y$ e sem o valor de $x$, o atacante não consegue obter a mensagem original $m$ a partir do criptograma $c$, dado que não consegue computar o segredo partilhado $s$, necessário para a desencriptação.

Efetivamente, se o atacante conseguisse obter o valor de $y$ e sendo $X$ público, portanto, conhecido, poderia calcular $X^y = (g^x)^y = g^{xy} = s$, pelo que, calculando trivialmente $s^{-1}$ e efetuando $m = c \cdot s^{-1}$, conseguiria obter a mensagem original, quebrando a confidencialidade da comunicação.

Analogamente, se o atacante conseguisse obter o valor de $x$ e tendo intersetado $Y$, poderia calcular $Y^x = (g^y)^x = g^{yx} = g^{xy} = s$, pelo que, calculando trivialmente $s^{-1}$ e efetuando $m = c \cdot s^{-1}$, conseguiria obter a mensagem original, quebrando a confidencialidade da comunicação.

Deste modo, a dificuldade do problema do logaritmo discreto garante a confidencialidade do esquema de encriptação *ElGamal*.

### P3

Pretende-se mostrar que o esquema de encriptação *ElGamal* é maleável, considerando um adversário que pode pedir a encriptação da mensagem $m$, recebendo o criptograma $c$.

1. O adversário pede a encriptação da mensagem $m$, obtendo o criptograma $c = m \cdot s$ e o valor de $Y$;
2. O adversário computa $c' = \alpha c$, para um qualquer valor de $\alpha$;
3. A desencriptação de $c'$ é $Dec(x, (Y, c')) = c' \cdot s^{-1} = \alpha c \cdot s^{-1} = \alpha (c \cdot s^{-1}) = \alpha Dec(x, (Y, c)) = \alpha m$.

Deste modo, o adversário consegue obter uma desencriptação de $c'$ diretamente relacionada com a desencriptação de $c$, sendo $c' = \alpha c$.

Como tal, sem pedir diretamente a desencriptação do criptograma $c = m \cdot s$ correspondente à mensagem original $m$, o adversário consegue pedir a desencriptação do criptograma $c' = \alpha c$ para obter $\alpha m$ e deduzir a mensagem original $m$, aproveitando a maleabilidade do esquema de encriptação *ElGamal*.

Assim, está provado que o esquema de encriptação *ElGamal* é maleável.
