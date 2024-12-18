def mod11(n):
    return n % 11

def calcular_pontos():
    pontos = []
    for x in range(11):
        for y in range(11):
            if mod11(y**2) == mod11(x**3 + x + 6):
                pontos.append((x, y))
    return pontos

pontos = calcular_pontos()
for ponto in pontos:
    print(ponto)
