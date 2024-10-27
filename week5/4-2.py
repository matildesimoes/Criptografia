import HashTools
import sys

def read(filename):
    with open(filename, "r") as file:
        content = file.read()
    return content

def generate_new_m_h(m, h, a):
    size = len(h) * 4
    if size == 256:
        return HashTools.new("sha256").extension(secret_length = size, original_data = m.encode(), append_data = a.encode(), signature = h)
    if size == 512:
        return HashTools.new("sha512").extension(secret_length = size, original_data = m.encode(), append_data = a.encode(), signature = h)
    raise ValueError("Output size must be one of the following for SHA-2: {256, 512}")

def save(new_m, new_h):
    with open("new_m", "wb") as file:
        file.write(new_m)
    with open("new_h", "w") as file:
        file.write(new_h)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: 4-2.py <m filename> <h filename> <message to append>")
        sys.exit(1)

    m = read(sys.argv[1])
    h = read(sys.argv[2])
    a = sys.argv[3]

    new_m, new_h = generate_new_m_h(m, h, a)
    save(new_m, new_h)
