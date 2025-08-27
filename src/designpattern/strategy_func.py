class StrategyExecutor(object):
    def __init__(self, func=None):
        if func is not None:
            self.execute = func
    def execute(self, *args):
        print("Strategy not implemented...")


def strategy_addition(arg1, arg2):
    print(arg1 + arg2)
def strategy_subtraction(arg1, arg2):
    print(arg1 - arg2)

def executor(arg1, arg2, func=None):
    if not func:
        print(f"{__name__} executor not implemented")
    else:
        return func(arg1,arg2)
def strategy_add(arg1,arg2):
    return arg1 + arg2
def strategy_subtract(arg1,arg2):
    return arg1 - arg2


def test1():
    no_strategy = StrategyExecutor()
    addition_strategy = StrategyExecutor(strategy_addition)
    subtraction_strategy = StrategyExecutor(strategy_subtraction)
    no_strategy.execute(4, 6)
    addition_strategy.execute(4, 6)
    subtraction_strategy.execute(4, 6)

def test2():
    print(executor(4,6))
    print(executor(4,6,strategy_add))
    print(executor(4,6,strategy_subtract))

if __name__ == "__main__":
    test2()

