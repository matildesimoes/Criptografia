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
    
    print(f"Os coeficientes do polinómio são: {coefficients}")
    shares = []
    for i in range(1, num_shares + 1):
        x = i 
        y = evaluate_polynomial(coefficients, x)
        shares.append((x, y))
    
    return shares

def recover_secret_with_lagrange(shares):
    """
    Reconstrói o segredo usando a função lagrange do scipy.
    """
    x_coords, y_coords = zip(*shares)  # Extrai os x e y 
    polynomial = lagrange(x_coords, y_coords)
    return round(polynomial(0)) 

# Inputs
secret = 12345
num_shares = 4
threshold = 3

shares = secret_sharing(secret, num_shares, threshold)
print("Partes:", shares)

# Seleciona 3 partes
selected_shares = shares[:3]

# Reconstrói o segredo
reconstructed_secret = recover_secret_with_lagrange(selected_shares)
print("Segredo reconstruído:", reconstructed_secret)
