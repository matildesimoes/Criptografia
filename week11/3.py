from sage.all import *
import sys

def genPrivate(sz):
    ubound = pow(2, sz) - 1
    lbound = pow(2, sz - 1)

    p = random_prime(ubound, lbound = lbound)
    q = random_prime(ubound, lbound = lbound)
    n = p * q

    return (n, p, q)

def vote(fileName, n, v):
    group = Integers(n).unit_group()
    r = Integer(group.random_element().value())

    n2 = n ** 2
    c = (pow(1 + n, v, n2) * pow(r, n, n2)) % n2

    with open(fileName, "a") as f:
        f.write(f"{c}\n")

def voteYes(fileName, n):
    vote(fileName, n, 1)

def voteNo(fileName, n):
    vote(fileName, n, 0)

def getResults(fileName, n, phi):
    with open(fileName, "r") as f:
        cs = f.read().split()
    
    n2 = pow(n, 2)

    c_total = 1
    for c in cs:
        c_total = (c_total * int(c)) % n2

    c = Integer(pow(c_total, phi, n2))
    m = (c - 1) / n
    i = Integer(pow(phi, -1, n))
    v_total = (m * i) % n

    print(f"The result of the polling written in '{fileName}' being {n} the public key used and {phi} the Euler's totient value corresponding to the public key is the vote total {v_total}.")
    return v_total

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: 3.py <sz> <fileName> <'Yes' votes> <'No' votes>")
        sys.exit(1)

    sz = int(sys.argv[1])
    fileName = sys.argv[2]
    yes = int(sys.argv[3])
    no = int(sys.argv[4])

    (n, p, q) = genPrivate(sz)
    phi = (p - 1) * (q - 1)

    for i in range(yes):
        voteYes(fileName, n)
    for i in range(no):
        voteNo(fileName, n)

    getResults(fileName, n, (p - 1) * (q - 1))
