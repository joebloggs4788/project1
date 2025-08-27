class RawCalculator(object):
    def fib(self, n):
        if n < 2:
            return 1
        return self.fib(n - 2) + self.fib(n - 1)
    
class CalculatorProxy(object):
    def __init__(self, target):
        self.target = target
        fib = getattr(self.target, 'fib')
        obj = memoize(fib)
        setattr(self.target, 'fib', memoize(fib))
    def __getattr__(self, name):
        return getattr(self.target, name)

# alternative, same effect
# class CalculatorProxy(object):
    # def __init__(self, target):
    #     self.target = target
    #     # Memoize the fib method and bind it to the target instance
    #     self.target.fib = memoize(self.target.fib)

    # def __getattr__(self, name):
    #     return getattr(self.target, name)
    
    
def memoize(fn):
    __cache = {}
    def memoized(*args):
        key = (fn.__name__, args)
        if key in __cache:
            return __cache[key]
        __cache[key] = fn(*args)
        return __cache[key]
    return memoized



