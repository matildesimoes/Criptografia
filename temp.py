def prob(s, p, k):
    n = 2 ** k
    return (n // p + (s < (n % p)))/n

def entropy(ss, p, k):
    e = 0
    for s in ss:
        ps = prob(s, p, k)
        if ps > 0:
            e -= ps * log(ps, 2)
    return e

def mink(ss, p, maxk, error):
    maxentropy = entropy(ss, p, maxk)
    for k in range(maxk):
        if maxentropy - entropy(ss, p, k) <= error:
            return k
