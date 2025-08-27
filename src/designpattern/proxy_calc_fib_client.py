import time
import proxy_calc_fib as proxy_lib

if __name__ == "__main__":

    calc = proxy_lib.CalculatorProxy(proxy_lib.RawCalculator())

    start = time.time()
    fib_seq = [calc.fib(x) for x in range(0, 80)]
    end = time.time()

    print("Calculating the list of {} Fibonacci numbers took {} seconds".format(
        len(fib_seq),
        end - start
        )
    )
