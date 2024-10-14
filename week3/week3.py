import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = os.urandom(32)
iv = os.urandom(16)

algorithm = algorithms.AES(key)
mode = modes.CBC(iv)
cipher = Cipher(algorithm, mode)

encryptor = cipher.encryptor()
ciphertext = encryptor.update(b"a secret message") + encryptor.finalize()

decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

print(ciphertext)
print(plaintext)
