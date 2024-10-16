from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher
from cryptography.hazmat.primitives.padding import PKCS7
import os
import sys

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

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: 1.py <filename> <key size (bits)> <IV size (bits)>")
        sys.exit(1)
    
    filename = sys.argv[1]
    key_size = int(sys.argv[2])
    iv_size = int(sys.argv[3])

    key = os.urandom(int(key_size / 8))
    iv = os.urandom(int(iv_size / 8))

    print(f"key = {key}\nIV = {iv}\n")

    CBC_PKCS7(filename, key, iv)
