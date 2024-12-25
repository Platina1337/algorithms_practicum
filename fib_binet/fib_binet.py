import math

def fib_binet(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    fib_n = (phi**n - psi**n) / sqrt_5
    return round(fib_n)

if __name__ == "__main__":
    n = 32
    print(f"fib({n}) using Binet's formula: {fib_binet(n)}")
