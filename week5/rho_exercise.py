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
    print(f"Hash is {8 * L} bits")

    tortoise = h1
    hare = h1
    iterations = 0

    initial_time = time.time()

    while True:
        tortoise = H(tortoise)
        hare = H(H(hare))
        iterations += 1

        if tortoise == hare:
            tortoise = h1

            while True:
                h = tortoise
                h_ = hare
                iterations += 1

                tortoise = H(h)
                hare = H(h_)

                if tortoise == hare:
                    end_time = time.time()
                    print(f"Time: {end_time - initial_time} seconds")
                    print(f"Iterations: {iterations}")
                    return h, h_
                
h1 = os.urandom(L)
h, h_ = rho(h1)
print(f"H({h}) = {H(h)}")
print(f"H({h_}) = {H(h_)}")
