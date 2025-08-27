import time

def fib_cached1(n, cache):
    if n < 2:
        return 1
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib_cached1(n-1,cache) + fib_cached1(n-2,cache)

if __name__ == "__main__":
    cache = {}
    start = time.time()
    for x in range(1,80):
        fib_cached1(x, cache)
    end = time.time()
    print(cache)

    print("=================")
    cache.clear()
    start = time.time()
    fib_seq = [fib_cached1(n,cache) for n in range(0,80)]
    end = time.time()

    print("Calculating the list of {} Fibonacci numbers took {} seconds".format(
        len(fib_seq),
        end - start
        )
    )