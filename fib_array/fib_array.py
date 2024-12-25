def fib_array(n):
    fib_series = [0, 1]
    for i in range(2, n + 1):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

if __name__ == "__main__":
    n = 8
    result = fib_array(n)
    print(f"Fibonacci series up to {n}: {result}")
