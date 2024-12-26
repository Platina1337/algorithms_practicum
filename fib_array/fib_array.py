def fib_array(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
        
    fib_series = [0, 1]
    for i in range(2, n + 1):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

if __name__ == "__main__":
    n = 8
    result = fib_array(n)
    print(result)
