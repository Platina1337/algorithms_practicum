def fib_big_even_odd(n):
    if n <= 0:
        return "even"
    

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10
    
    return "even" if b % 2 == 0 else "odd"

if __name__ == "__main__":
    n = 841645
    result = fib_big_even_odd(n)
    print(result)  
