import random
from scipy.interpolate import lagrange

def generate_polynomial(secret, degree):
    coefficients = [secret] + [random.randint(1, 100) for _ in range(degree)]
    return coefficients

def evaluate_polynomial(coefficients, x):
    result = 0
    for power, coeff in enumerate(coefficients):
        result += coeff * (x ** power)
    return result

def secret_sharing(secret, num_shares, threshold):
    degree = threshold - 1
    coefficients = generate_polynomial(secret, degree)
    
    shares = []
    for i in range(1, num_shares + 1):
        x = i
        y = evaluate_polynomial(coefficients, x)
        shares.append((x, y))
    
    return coefficients, shares

def recover_polynomial_with_lagrange(shares):
    """
    Reconstrói o segredo usando a função lagrange do scipy.
    """
    x_coords, y_coords = zip(*shares)  # Extrai os x e y 
    polynomial = lagrange(x_coords, y_coords)
    return polynomial

num_shares = 4
threshold = 3

# 1: Gerar o polinómio f para o segredo 100 e com as partes x1, x2, x3, x4
secret_f = 100
coefficients_f, shares_f = secret_sharing(secret_f, num_shares, threshold)
print("Os coeficientes do polinómio f:", coefficients_f)
print("Partes f:", shares_f)
print("-------------------------------------")

# 2: Gerar o polinómio g para o segredo 550 e com as partes y1, y2, y3, y4
secret_g = 550
coefficients_g, shares_g = secret_sharing(secret_g, num_shares, threshold)
print("Os coeficientes do polinómio g:", coefficients_g)
print("Partes g:", shares_g)
print("-------------------------------------")

# 3: Carcular z1 = x1 + y1, z2 = x2 + y2, z3 = x3 + y3
z_shares = [(x[0], x[1] + y[1]) for x, y in zip(shares_f[:3], shares_g[:3])]
print("Partes z (soma de f e g):", z_shares)

# 4: Reconstruir o segredo usando z1, z2, z3
reconstructed_polynomial = recover_polynomial_with_lagrange(z_shares)
reconstructed_secret = reconstructed_polynomial(0)
print("Segredo reconstruído a partir de z:", reconstructed_secret)
