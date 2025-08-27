class Calculator(object):
    def __init__(self):
        self.cache = {}

    def fib(self,n):        
        if n < 2:
            return 1
        try:
            result = self.cache[n]
        except:
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
            result = self.cache[n]
        return result
    
def fib_calc():
    calc = Calculator()
    print("fib({}) = {}".format(10, calc.fib(10)))
    print(calc.cache)

if __name__ == '__main__':
    fib_calc()
