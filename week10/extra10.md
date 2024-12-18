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

### P1



### P2



### P3


