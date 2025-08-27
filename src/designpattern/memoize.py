import functools
import inspect

def fib(n):
    if n < 2:
        return 1
    return fib(n - 2) + fib(n - 1)


def memoize(fn):
    __cache = {}

    @functools.wraps(fn)
    def memoized(*args):
        key = (fn.__name__, args)
        if key in __cache:
            return __cache[key]
        __cache[key] = fn(*args)
        return __cache[key]
    
    memoized.__signature__ = inspect.signature(fn)
    return memoized

def simple():
    obj = memoize(fib)
    print(obj(20))

def keep_meta_data():
    # Create a memoized version of the Fibonacci function
    memoized_fib = memoize(fib)
    signature = inspect.signature(memoized_fib)
    print(signature)

    for param in signature.parameters.values():
        print(f"Name: {param.name}, Default: {param.default}, Annotation: {param.annotation}")


    # Check the signature and docstring
    print(memoized_fib)  # Output: <function fib at 0x...>
    print(memoized_fib.__name__)  # Output: fib
    print(memoized_fib.__doc__)   # Output: (will show the docstring of fib if it exists)
    print(memoized_fib.__signature__)

if __name__ == '__main__':
    keep_meta_data()