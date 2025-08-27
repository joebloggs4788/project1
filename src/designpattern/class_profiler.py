import time
from functools import wraps

def profiling_wrapper(f):
    @wraps(f)
    def wrap_f(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("[Time elapsed for n = {}] {}".format(n, elapsed_time))
        return result
    return wrap_f

def profile_all_class_methods(Cls):
    class ProfiledClass(object):
        def __init__(self, *args, **kwargs):
            self.inst = Cls(*args, **kwargs)
            
        def __getattribute__(self, s):
            try:
                x = super(ProfiledClass, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                x = self.inst.__getattribute__(s)
            if type(x) == type(self.__init__):
                return profiling_wrapper(x)
            else:
                return x
    return ProfiledClass


@profile_all_class_methods
class DoMathStuff(object):
    def fib(self):
        pass
    @profiling_wrapper
    def factorial(self):
        pass


