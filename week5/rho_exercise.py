from cryptography.hazmat.primitives import hashes
import os
import time

L = 5 # output length in bytes

# Something to make calling hash functions more succint
def H(X):
	digest = hashes.Hash(hashes.SHA256())
	digest.update(X)
	return (digest.finalize()[0:L])

# Write a function that finds the collision and presents the values in which it occurred
def rho(h1):
    print(f"Hash é de {8 * L} bits\n")
    
    

	print("\nEntradas que colidiram:")
    print(f"Entrada 1: {entrada1.hex()}")
    print(f"Entrada 2: {entrada2.hex()}")
	print(f"Tempo: {end_time - initial_time:.6f} segundos")
    print(f"Iterações: {iterations}")

    return entrada1, entrada2

start = os.urandom(L)
h0, h1 = rho(start)
