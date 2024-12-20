def mod_inverse(a, p):
    return pow(a, p - 2, p)

def point_addition(P, Q, a, p):
    x_p, y_p = P
    x_q, y_q = Q

    if P == Q:
        m = (3 * x_p ** 2 + a) * mod_inverse(2 * y_p, p) % p
    else:
        m = (y_q - y_p) * mod_inverse(x_q - x_p, p) % p
    
    x_r = (m ** 2 - x_p - x_q) % p
    y_r = (m * (x_p - x_r) - y_p) % p
    
    return (x_r, y_r)

def compute_multiples(G, a, p, n):
    multiples = [G]
    current = G
    for _ in range(n):
        current = point_addition(current, G, a, p)
        multiples.append(current)
    return multiples

a, p = 1, 11
G = (2, 7)

multiples = compute_multiples(G, a, p, 12)
for i, point in enumerate(multiples, start = 1):
    print(f"{i}G = {point}")
