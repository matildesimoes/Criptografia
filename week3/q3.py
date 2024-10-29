from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher
import random
import os
import sys

def CBC(key, nonce, message):
    print(f"\nNonce: {nonce}\nMessage: {message}")

    algorithm = algorithms.AES(key)

    ecb = modes.ECB()
    cipher = Cipher(algorithm, ecb)
    iv = encrypt(nonce, cipher)
    print("\nIV:", iv)

    cbc = modes.CBC(iv)
    cipher = Cipher(algorithm, cbc)
    ciphertext = encrypt(message, cipher)

    print("\nEncrypted Message:", ciphertext, end = "\n\n")
    for i in range(0, len(ciphertext), len(key)):
        print("Encrypted Block:", ciphertext[i : i + len(key)])
    return ciphertext

def encrypt(message, cipher):
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message) + encryptor.finalize()
    return ciphertext

def challenge(ciphertext, bytes):
    print("\n------------------------------ CHALLENGE ------------------------------\n")

    nonce = ciphertext[0 : bytes]
    m0 = b"\x00" * bytes
    m1 = b"\x01" * bytes
    b = random.randint(0, 1)
    print(f"m0: {m0}\nm1: {m1}\n\nBit: {b}")

    if b == 0:
        m = CBC(key, nonce, m0)
    elif b == 1:
        m = CBC(key, nonce, m1)
    else:
        raise ValueError("b not in {0, 1}")

    guess = int(m != ciphertext[2 * bytes : ])
    print("\nAttacker guesses b =", guess)

    if guess == b:
        print("Attacker wins!")
    else:
        print("Attacker loses...")

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: q3.py")
        sys.exit(1)

    bits = 128
    bytes = int(bits / 8)
    key = os.urandom(bytes)

    nonce = b"\x00" * bytes
    message = b"\x00" * bytes * 3
    ciphertext = CBC(key, nonce, message)

    challenge(ciphertext, bytes)
