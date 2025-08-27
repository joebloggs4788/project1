import time

def profiling_decorator(f):
    def wrapped_f(n):
        start_time = time.time()
        result = f(n)
        end_time = time.time()
        print( "[Time elapsed for n = {}] {}".format(n, end_time - start_time))
        return result
    return wrapped_f

@profiling_decorator
def fib(n):
    print("Inside fib")
    if n < 2:
        return
    fibPrev = 1
    fib = 1
    for num in range(2, n): fibPrev, fib = fib, fib + fibPrev
    return fib

if __name__ == "__main__":
    n = 77
    print("Fibonacci number for n = {}: {}".format(n, fib(n)))
