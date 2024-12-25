import time

def fib_loop(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    test_values = [5, 10, 15, 20, 32]
    for n in test_values:
        start_time = time.time()
        result = fib_loop(n)
        end_time = time.time()
        duration = (end_time - start_time) * 1000  # in milliseconds
        print(f"fib({n}) = {result}, executed in {duration:.2f} ms")
