import os
import random
from cryptography.hazmat.primitives import hashes

# Internal state of the LFSR
x = 1

# Call the lfsr to update the internal state
def __lfsr():
    global x
    x = (x**5 + x**4 + 1) % 1009

# Use crypto random generation to initialize the LFSR
def gen(): 
    global x
    sysrand = random.SystemRandom()
    x = sysrand.randint(0,1008)

# Bitwise XOR operation.
def enc(m):
    global x
    k = b""
    while (len(k) < len(m)):
        __lfsr()
        digest = hashes.Hash(hashes.SHA256())
        digest.update(x.to_bytes(4, "big"))
        k += digest.finalize()
        print("chave", k)
    return bytearray([a ^ b for a, b in zip(m, k[:len(m)])])

# Reverse operation
def dec(c):
    global x
    k = b""
    while (len(k) < len(c)):
        __lfsr()
        digest = hashes.Hash(hashes.SHA256())
        digest.update(x.to_bytes(4, "big"))
        k += digest.finalize()
    return bytearray([a ^ b for a, b in zip(c, k[:len(c)])])

# Função para obter o estado interno
def get_state():
    global x
    return x

# Função para definir o estado interno
def set_state(state):
    global x
    x = state

def main():

    mensagem = b'\x00' * 64 
    print("Mensagem Original:", mensagem)

    gen()
    estado_inicial = get_state()
    print("Estado Inicial (x):", estado_inicial)

    ciphertext = enc(mensagem)
    print("Ciphertext:", ciphertext.hex())


if __name__ == "__main__":
    main()
