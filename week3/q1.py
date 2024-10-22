import ciphersuite_aesnotrand as ciphersuite
from binascii import hexlify, unhexlify

key = ciphersuite.gen()
msg = 'Attack at dawn!!'
cph = ciphersuite.enc(key, bytearray(msg, 'ascii'))

f = open("weak_ciphertext", "wb")
f.write(cph)
f.close()

# 1 - Read ciphertext
file = open("weak_ciphertext", "rb")
ciphertext = file.read()
file.close()
print("Ciphertext:", ciphertext)

# 2 - Guess the key used
for i in range(2 ** 24):
	key = i.to_bytes(16, "big")
	plaintext = ciphersuite.dec(key, ciphertext)
	if plaintext == b"Attack at dawn!!":
		print("Key:", key)
		print("Decryption:", plaintext) # 3 - Test the decryption
		break
