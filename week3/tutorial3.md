# Tutorial #3

## 1

O *script Python* que encripta um ficheiro no modo CBC e o desencripta encontra-se no ficheiro `1.py`.

As funções relevantes `CBC_PKCS7`, `encrypt` e `decrypt` encontram-se abaixo.

```python
def CBC_PKCS7(filename, key, iv):
    algorithm = algorithms.AES(key)
    mode = modes.CBC(iv)
    cipher = Cipher(algorithm, mode)

    block_size = len(iv) * 8
    padding = PKCS7(block_size)

    encrypt(filename, cipher, padding)
    decrypt(filename, cipher, padding)

def encrypt(filename, cipher, padding):
    with open(filename, 'rb') as file:
        data = file.read()

    padder = padding.padder()
    padded_data = padder.update(data) + padder.finalize()

    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    with open("enc_" + filename, 'wb') as file:
        file.write(ciphertext)

    print("The encrypted file was saved to: 'enc_", filename, "'", sep = "")

def decrypt(filename, cipher, padding):
    with open("enc_" + filename, 'rb') as file:
        ciphertext = file.read()

    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()

    with open("dec_" + filename, 'wb') as file:
        file.write(plaintext)

    print("The decrypted file was saved to: 'dec_", filename, "'", sep = "")
```

![1](/week3/images/1.png)

## 2

Para encriptar um ficheiro no modo CBC com OpenSSL, corre-se o seguinte comando.

```bash
openssl enc -aes-256-cbc -e -in file.txt -out enc_file.txt -pass pass:password -pbkdf2
```

Este comando recebe como *input* o ficheiro `file.txt`, encripta-o usando o algoritmo AES no modo CBC (usando uma chave de 256 *bits*) e armazena o resultado no ficheiro `enc_file.txt`. A chave e o vetor de inicialização são derivados da palavra-passe (`password`) usando a função de derivação de chave `PBKDF2` (*Password-Based Key Derivation Function 2*).

Para desencriptar o ficheiro encriptado, corre-se o seguinte comando.

```bash
openssl enc -aes-256-cbc -d -in enc_file.txt -out dec_file.txt -pass pass:password -pbkdf2
```

Este comando recebe como *input* o ficheiro `enc_file.txt`, desencripta-o usando o algoritmo AES no modo CBC (usando uma chave de 256 *bits*) e armazena o resultado no ficheiro `dec_file.txt`. A chave e o vetor de inicialização são derivados da palavra-passe (`password`) usando a função de derivação de chave `PBKDF2` (*Password-Based Key Derivation Function 2*).

![2](/week3/images/2.png)

## 3

Criou-se um novo ficheiro `file3.txt`, encriptou-se para o ficheiro `enc_file3.txt` e alterou-se um único *byte* deste ficheiro encriptado.
Posteriormente, tentou-se desencriptar o ficheiro `enc_file3.txt` para o ficheiro `dec_file3.txt`.

![3](/week3/images/3.png)

**Para as alíneas 3.1, 3.2, 3.3 e 3.4, considere-se o seguinte:**

Sejam:
- P<sub>n</sub> - o bloco índice-n do texto original (*plaintext*)
- C<sub>n</sub> - o bloco índice-n do texto cifrado (*ciphertext*)
- E(K, C) - o resultado da função de encriptação do bloco C, usando a chave K
- D(K, C) - o resultado da função de desencriptação do bloco C, usando a chave K
- `+` - a operação XOR (ou-exclusivo)
- IV - o vetor de inicialização

Então:
- C<sub>0</sub> = E(K, P<sub>0</sub> + IV)
- C<sub>n</sub> = E(K, P<sub>n</sub> + C<sub>n - 1</sub>), n > 0
- P<sub>0</sub> = D(K, C<sub>0</sub>) + IV
- P<sub>n</sub> = D(K, C<sub>n</sub>) + C<sub>n - 1</sub>, n > 0

### 3.1

Tal como é possível verificar, a desencriptação está correta para quase todo o ficheiro, com exceção de uma pequena parte, sensivelmente a meio do texto, que está incorreta, por estar diferente da parte correspondente no ficheiro original  (`do seu conteúdo`).

Isto acontece porque o modo *Cipher Block Chaining* (CBC) faz com que cada P<sub>n</sub> dependa apenas de C<sub>n</sub> e de C<sub>n - 1</sub>.
Isto é, a desencriptação de cada bloco (P<sub>n</sub>) depende apenas do bloco cifrado correspondente (C<sub>n</sub>) e do bloco cifrado imediatamente anterior (C<sub>n - 1</sub>).

Como tal, os únicos blocos afetados pela alteração de um *byte* no texto cifrado são o bloco que contém esse *byte* e o bloco imediatamente seguinte, por serem os únicos que dependem do bloco que contém o *byte* alterado.
Por isso, apesar de um *byte* ter sido editado, todo o texto anterior ao bloco que contém esse *byte* é recuperável, bem como todo o texto posterior ao bloco seguinte ao bloco que contém esse *byte*.

### 3.2

Se o IV e o primeiro bloco do texto cifrado (C<sub>0</sub>) de um ficheiro encriptado com CBC fossem corrompidos ou perdidos, então seria possível recuperar parcialmente o ficheiro.
Isto é, seria possível recuperar o texto presente em todos os blocos a partir do terceiro bloco (bloco de índice 2), inclusive.

Isto acontece porque, seguindo uma estrutura semelhante a uma prova por indução:

1. P<sub>0</sub> é irrecuperável, porque P<sub>0</sub> = D(K, C<sub>0</sub>) + IV e não existe IV nem C<sub>0</sub>.
2. P<sub>1</sub> é irrecuperável, porque P<sub>1</sub> = D(K, C<sub>1</sub>) + C<sub>0</sub> e não existe C<sub>0</sub>.
3. **Caso-Base:** P<sub>2</sub> é recuperável, porque P<sub>2</sub> = D(K, C<sub>2</sub>) + C<sub>1</sub> e existem C<sub>1</sub> e C<sub>2</sub>.
4. **Caso Recursivo:** Para n > 2, P<sub>n</sub> é recuperável, porque P<sub>n</sub> = D(K, C<sub>n</sub>) + C<sub>n - 1</sub> e existem C<sub>n</sub> e C<sub>n - 1</sub>.

### 3.3

Se um *bit* do texto cifrado não for entregue, então é possível recuperar parcialmente o ficheiro.
Isto é, é possível recuperar o texto presente em todos os blocos até ao bloco ao qual pertence o *bit* que não foi entregue.

Seja C<sub>m</sub> o bloco ao qual pertence o *bit* que não foi entregue.

A desencriptação de qualquer bloco anterior a C<sub>m</sub> não depende de C<sub>m</sub>, pelo que todos os blocos anteriores a C<sub>m</sub> podem ser recuperados corretamente.

Se se souber que bloco é C<sub>m</sub>, isto é, se se conhecer qual é o valor de m, então é possível recuperar todos os blocos posteriores a C<sub>m + 1</sub>, pela razão exposta anteriormente.
Ou seja, admitindo que se sabe que houve um *bit* perdido em C<sub>m</sub>, então nem P<sub>m</sub> nem P<sub>m + 1</sub> são recuperáveis, por ambos dependerem de C<sub>m</sub>, mas todos os blocos P<sub>n</sub>, sendo n > m + 1, são recuperáveis, por não dependerem de C<sub>m</sub>, mas sim de C<sub>n</sub> e de C<sub>n - 1</sub>, que não foram corrompidos (n - 1 > m).

Contudo, se não se souber que bloco é C<sub>m</sub>, isto é, se não se conhecer qual é o valor de m (o que parece mais plausível no caso de uma transmissão satélite - não saber a que bloco pertence o *bit* perdido), então não é possível recuperar C<sub>m</sub> nem nenhum dos blocos posteriores a C<sub>m</sub>, porque a perda de um *bit* em C<sub>k</sub> faz com que C<sub>k</sub> passe a incluir, como último *bit*, o primeiro *bit* de C<sub>k + 1</sub>, e assim sucessivamente, levando a que os blocos C<sub>k</sub>, sendo k >= m, sejam transmitidos incorretamente, tendo um *bit* que, na verdade, deveria pertencer ao bloco seguinte, o que impossibilita a desencriptação de todos os blocos C<sub>k</sub>, ou seja, de todos os blocos desde C<sub>m</sub> (inclusive) até ao fim do ficheiro.

### 3.4

Sim, é possível modificar um *byte* no meio de um ficheiro encriptado com CBC sem ter de o voltar a encriptar completamente.
Isto é, para permitir uma desencriptação correta, apenas é necessário voltar a encriptar os blocos a partir daquele a que pertence o *byte* modificado (inclusive).

Seja C<sub>m</sub> o bloco ao qual pertence o *byte* modificado.

Nenhum dos blocos anteriores a C<sub>m</sub> depende de C<sub>m</sub>, pelo que uma alteração em C<sub>m</sub> não afeta nenhum dos blocos anteriores, não sendo, por isso, necessário voltar a encriptá-los.
Efetivamente, uma alteração em C<sub>m</sub> não é visível até tentar desencriptar C<sub>m</sub>, pelo que a desencriptação dos blocos anteriores mantém-se inalterada e, por isso, correta.

Como o valor de P<sub>m + 1</sub> depende de C<sub>m + 1</sub> e de C<sub>m</sub>, então, para manter o valor correto de P<sub>m + 1</sub>, tendo alterado o valor de C<sub>m</sub>, seria necessário alterar também o valor de C<sub>m + 1</sub>.
Alterando o valor de C<sub>m + 1</sub>, pela razão anterior, seria necessário alterar o valor de C<sub>m + 2</sub> para obter o valor correto de P<sub>m + 2</sub>.
E assim sucessivamente, pelo que todos os blocos posteriores a C<sub>m</sub> são afetados, tendo de ser encriptados novamente.

Como tal, a modificação de C<sub>m</sub> só obriga a encriptar novamente os blocos posteriores a P<sub>m</sub> (inclusive) para se conseguir desencriptar corretamente o ficheiro.

## 4

Criou-se um novo ficheiro `file4.txt`, encriptou-se (com o modo CTR) para o ficheiro `enc_file4.txt` e alterou-se um único *byte* deste ficheiro encriptado.
Posteriormente, tentou-se desencriptar o ficheiro `enc_file4.txt` para o ficheiro `dec_file4.txt`.

![4](/week3/images/4.png)

**Para as alíneas 4.1, 4.2, 4.3 e 4.4, considere-se o seguinte:**

Sejam:
- P<sub>n</sub> - o bloco índice-n do texto original (*plaintext*)
- C<sub>n</sub> - o bloco índice-n do texto cifrado (*ciphertext*)
- E<sub>n</sub> - o resultado da encriptação do *nonce* índice-n concatenado com n, usando a chave K
- D<sub>n</sub> - o resultado da desencriptação do *nonce* índice-n concatenado com n, usando a chave K
- `+` - a operação XOR (ou-exclusivo)

Então:
- C<sub>n</sub> = E<sub>n</sub> + P<sub>n</sub>, n >= 0
- P<sub>n</sub> = E<sub>n</sub> + C<sub>n</sub>, n >= 0

### 4.1

Tal como é possível verificar, a desencriptação está correta para quase todo o ficheiro, com exceção de uma pequena parte, sensivelmente a meio do texto, que está incorreta, por estar diferente da parte correspondente no ficheiro original (`conteúdo`).
Esta parte incorreta está aproximadamente na mesma posição que a do exercício anterior, porque a posição do *byte* alterado foi a mesma, mas o comprimento da parte incorreta do ficheiro é muito menor do que no caso anterior.

Isto acontece porque o modo *Counter Block Mode* (CTR) faz com que cada P<sub>n</sub> dependa apenas de C<sub>n</sub> (e de E<sub>n</sub>).
Isto é, a desencriptação de cada bloco (P<sub>n</sub>) depende apenas do bloco cifrado correspondente (C<sub>n</sub>).

Como tal, o único bloco afetado pela alteração de um *byte* no texto cifrado é o bloco que contém esse *byte*.
Por isso, apesar de um *byte* ter sido editado, todo o texto anterior ao bloco que contém esse *byte* é recuperável, bem como todo o texto posterior ao bloco que contém esse *byte*, ou seja, todo o ficheiro é recuperável, exceto o bloco que contém o *byte* que foi alterado.

### 4.2

Se o primeiro bloco do texto cifrado (C<sub>0</sub>) de um ficheiro encriptado com CTR fosse corrompido ou perdido, então seria possível recuperar parcialmente o ficheiro.
Isto é, seria possível recuperar o texto presente em todos os blocos, exceto o primeiro bloco.

Isto acontece porque cada P<sub>n</sub> só depende do C<sub>n</sub> (e de E<sub>n</sub>), pelo que perder ou corromper um bloco de texto cifrado apenas afeta a desencriptação desse mesmo bloco e não do resto do ficheiro. Os blocos são independentes entre si.

Não se coloca a questão de o IV ser perdido ou corrompido para o caso do modo CTR, porque este modo não utiliza IV.

### 4.3

Se um *bit* do texto cifrado não for entregue, então é possível recuperar parcialmente o ficheiro.

Seja C<sub>m</sub> o bloco ao qual pertence o *bit* que não foi entregue.

Se se souber que bloco é C<sub>m</sub>, isto é, se se conhecer qual é o valor de m, então é possível recuperar todos os blocos exceto C<sub>m</sub>, pela razão exposta anteriormente.
Ou seja, admitindo que se sabe que houve um *bit* perdido em C<sub>m</sub>, então todos os blocos P<sub>n</sub>, sendo n diferente de m, são recuperáveis, por não dependerem de C<sub>m</sub>, mas sim de C<sub>n</sub>, que não foi corrompido.

Contudo, se não se souber que bloco é C<sub>m</sub>, isto é, se não se conhecer qual é o valor de m (o que parece mais plausível no caso de uma transmissão satélite - não saber a que bloco pertence o *bit* perdido), então não é possível recuperar C<sub>m</sub> nem nenhum dos blocos posteriores a C<sub>m</sub>, porque a perda de um *bit* em C<sub>k</sub> faz com que C<sub>k</sub> passe a incluir, como último *bit*, o primeiro *bit* de C<sub>k + 1</sub>, e assim sucessivamente, levando a que os blocos C<sub>k</sub>, sendo k >= m, sejam transmitidos incorretamente, tendo um *bit* que, na verdade, deveria pertencer ao bloco seguinte, o que impossibilita a desencriptação de todos os blocos C<sub>k</sub>, ou seja, de todos os blocos desde C<sub>m</sub> (inclusive) até ao fim do ficheiro.

### 4.4

Sim, é possível modificar um *byte* no meio de um ficheiro encriptado com CTR sem ter de o voltar a encriptar completamente.
Isto é, para permitir uma desencriptação correta, apenas é necessário voltar a encriptar o bloco ao qual pertence o *byte* modificado.

Seja C<sub>m</sub> o bloco ao qual pertence o *byte* modificado.

Como o valor de P<sub>n</sub> só depende de C<sub>n</sub>, então, para qualquer n diferente de m, P<sub>n</sub> não depende de C<sub>m</sub>.
Por isso, nenhum dos blocos diferentes de C<sub>m</sub> tem de ser encriptado novamente.

Como tal, a modificação de C<sub>m</sub> só obriga a encriptar novamente P<sub>m</sub> para se conseguir desencriptar corretamente o ficheiro.

### Diferenças

A principal diferença entre o modo CBC e o modo CTR é que, no modo CBC, os blocos dependem uns dos outros, enquanto, no modo CTR, os blocos são independentes entre si.

Assim sendo, no modo CBC, um erro em C<sub>m</sub> afeta sempre P<sub>m</sub> e P<sub>m + 1</sub>, enquanto, no modo CTR, um erro em C<sub>m</sub> afeta apenas P<sub>m</sub>.

Por isso, o modo CBC não pode ser paralelizável, mas o modo CTR pode.
