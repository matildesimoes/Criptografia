# Python Module ciphersuite
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
	x = sysrand.randint(0, 1008)

# Bitwise XOR operation.
def enc(m):
	global x
	k = b""
	while (len(k) < len(m)):
		__lfsr()
		digest = hashes.Hash(hashes.SHA256())
		digest.update(x.to_bytes(4, "big"))
		k += digest.finalize()
	return bytearray([a ^ b for a, b in zip(m, k[:len(m)])])

# Reverse operation
def dec(c):
	global x
	k = b""
	while (len(k) < len(c)):
		digest = hashes.Hash(hashes.SHA256())
		digest.update(x.to_bytes(4, "big"))
		k += digest.finalize()
	return bytearray([a ^ b for a, b in zip(c, k[:len(c)])])

gen()

cs = list()
ks = list()
for i in range(75):
	m = i.to_bytes(4, "big")
	c = enc(m)
	cs.append(c)
	k = bytearray([a ^ b for a, b in zip(m, c)])
	ks.append(k)

m0 = (100).to_bytes(4, "big")
m1 = (111).to_bytes(4, "big")
b = random.randint(0, 1)
print(f"m0: {m0}\nm1: {m1}\n\nBit: {b}")

if b == 0:
	c = enc(m0)
elif b == 1:
	c = enc(m1)
else:
	raise ValueError("b not in {0, 1}")

for k in ks:
	m = bytearray([a ^ b for a, b in zip(c, k)])
	if m == m0:
		guess = 0
		break
	elif m == m1:
		guess = 1
		break

print("\nAttacker guesses b =", guess)

if guess == b:
	print("Attacker wins!")
else:
	print("Attacker loses...")
