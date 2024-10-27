import hashlib
import os
import sys

def generate_k(size):
    return os.urandom(size)

def compute_h(k, m):
    size = len(k)
    if size == 256:
        return hashlib.sha256(k + m.encode()).hexdigest()
    if size == 512:
        return hashlib.sha512(k + m.encode()).hexdigest()
    raise ValueError("Output size must be one of the following for SHA-2: {256, 512}")

def save(k, m, h):
    with open("k", "wb") as file:
        file.write(k)
    with open("m", "w") as file:
        file.write(m)
    with open("h", "w") as file:
        file.write(h)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: 4-1.py <output size (bits)> <message>")
        sys.exit(1)
    
    size = int(sys.argv[1])
    if size not in {256, 512}:
        raise ValueError("Output size be one of the following for SHA-2: {256, 512}")
    
    k = generate_k(size)
    m = sys.argv[2]
    h = compute_h(k, m)
    save(k, m, h)
