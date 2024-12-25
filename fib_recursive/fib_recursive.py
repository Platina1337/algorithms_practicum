import time

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

if __name__ == "__main__":
    test_values = [5, 10, 15, 20, 24]
    for n in test_values:
        start_time = time.time()
        result = fib_recursive(n)
        end_time = time.time()
        duration = (end_time - start_time) * 1000  # in milliseconds
        print(f"fib({n}) = {result}, executed in {duration:.2f} ms")
