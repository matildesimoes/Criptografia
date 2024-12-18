import random

def miller_rabin(n, m = 10):
    """
    Algoritmo Miller-Rabin
    n: número a ser testado
    m: número de iterações para aumentar a precisão
    Retorna True se n é provavelmente primo, False se é composto
    """
    if n <= 1:
        return False
    if n <= 3:
        return True

    d = n - 1
    k = 0
    while d % 2 == 0:
        d //= 2
        k += 1

    for _ in range(m):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(k - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# primos grandes
primos_grandes = [
    15485867,
    32416190071, 
    982451653,
    43142746595714191,
]

for primo in primos_grandes:
    resultado = miller_rabin(primo)
    print(f"{primo} é {'provavelmente primo' if resultado else 'composto'}.")

# produto de 2 primos grandes
compostos_grandes = [
    15485867 * 15485869, 
    32416190071 * 32416187567,  
]

for composto in compostos_grandes:
    resultado = miller_rabin(composto)
    print(f"{composto} é {'provavelmente primo' if resultado else 'composto'}.")
