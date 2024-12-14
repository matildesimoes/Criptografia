import os

FILE = "pw"

encryption_key = os.urandom(16)         # AES-128-CTR - 16 bytes
authentication_key = os.urandom(32)     # HMAC-SHA256 - 32 bytes

print(f"Generated encryption key of {len(encryption_key)} bytes: {encryption_key}")
print(f"Generated authentication key of {len(authentication_key)} bytes: {authentication_key}")

with open(FILE, "wb") as f:
    f.write(encryption_key + authentication_key)

print(f"Produced a file '{FILE}' with two symmetric keys")
