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

Editou-se o ficheiro `file.txt` - alterando o último *byte* (`0x0a`) para `0x33` - e guardou-se o *output* no ficheiro `file3.txt`.

![3](/week3/images/3.png)

### 3.1

### 3.2

### 3.3

### 3.4

## 4

Editou-se o ficheiro `file.txt` - alterando o último *byte* (`0x0a`) para `0x44` - e guardou-se o *output* no ficheiro `file4.txt`.

![4](/week3/images/4.png)

### 4.1

### 4.2

### 4.3

### 4.4
