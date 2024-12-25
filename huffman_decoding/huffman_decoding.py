def fib_big_even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == "__main__":
    n = 841645
    result = fib_big_even_odd(n)
    print(f"fib({n}) is {result}")
