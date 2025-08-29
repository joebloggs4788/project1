def map(func, *iterables):
    # func: function to apply
    # *iterables: any number of iterable arguments
    min_length = min(len(it) for it in iterables)
    return [func(*args) for args in zip(*(it[:min_length] for it in iterables))]

from typing import Iterable, Callable, Any, Iterator
from unittest import result
def my_map(func: Callable[..., Any], *iterables: Iterable[Any]) -> Iterator[Any]:
    """Applies a function to the items of one or more iterables."""
    min_length = min(len(it) for it in iterables)
    return (func(*args) for args in zip(*(it[:min_length] for it in iterables)))

def list_comprehension():
    import pprint
    numbers = range(1,100)
    result = [ (x,x*2) if x%2 == 0 else (x,x**2) for x in numbers]
    pprint.pprint(result)

def fibonacci(n: int) -> int:   
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a+b
        return b
    
def main() -> None:
    for index in range(1, 11):
        outputfmt = "fibonacci({index}) = {result}"
        print (outputfmt.format(index=index, result=fibonacci(index)))

def ran1():

    for _ in range(2, 11, 1):
        print (_)


  # Example usage of fibonacci function

if __name__ == "__main__":
    # main()

    list_comprehension()

    # f = fibonacci(100)
    # print(f'fib(100) = {f}')
    # print("the 100th Fibonacci number is {n}".format(n=f))

    # # Example usage of my_map
    # result = my_map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
    # print(list(result))  # Output: [5, 7, 9]