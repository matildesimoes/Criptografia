import hashlib
import sys

def read_bytes(filename):
    with open(filename, "rb") as file:
        content = file.read()
    return content

def read(filename):
    with open(filename, "r") as file:
        content = file.read()
    return content

def compute_h(k, new_m):
    size = len(k)
    if size == 256:
        return hashlib.sha256(k + new_m).hexdigest()
    if size == 512:
        return hashlib.sha512(k + new_m).hexdigest()
    raise ValueError("Output size must be one of the following for SHA-2: {256, 512}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: 4-3.py <m filename> <new_m filename> <k filename> <new_h filename>")
        sys.exit(1)

    m = read_bytes(sys.argv[1])
    new_m = read_bytes(sys.argv[2])

    print("m  =", m)
    print("m' =", new_m)
    print("\nm =/= m'?", m != new_m)

    k = read_bytes(sys.argv[3])
    h = compute_h(k, new_m)
    new_h = read(sys.argv[4])

    print("\nSHA2(k || m') =", h)
    print("h'            =", new_h)
    print("\nSHA2(k || m') = h'?", h == new_h)
