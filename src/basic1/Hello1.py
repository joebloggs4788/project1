import random
import pprint
def lottery():
    for i in range(6):
        yield random.randint(1,40)
    yield random.randint(1,15)

def run_lottery():
    for rand_number in lottery():
        print("The next number is %d."  %rand_number)

def formatting():
    a = 5
    b = 'webhook'

    print("This is a formatted string: {0} {1}".format('Hello', 'World'))
    print(f"This is an f-string: {'Hello'} {'World'}, {a}, {b}")

    txt = "For only {price:.2f} dollars! {s1},{s2}"
    print (txt.format(price = 49.1234, s1=a, s2=b))

def docstr_fun1(par1, par2, *, parameter3) -> str:
    """
    A simple demo for docstr manipulation

    Args:
        par1(str) : first parameter
        par2(str) : second parameter
        parameter3(str) : keyword argument

    Returns: 
        str: concatenation of the arguments

    Raises:
        None
    """

    return str(par1) + str(par2) + str(parameter3)

def args_fun1(a, b, *args, **kwargs):
    print (f"{a}, {b}")
    for v in args:
        print(f"{v}")
    for k,v in kwargs.items():
        print(f"{k} : {v}")

    print("==========")
    print(args)
    print(kwargs)
    # standard def
    # def func(positional, /, standard, *, keyword_only, **kwargs):

def global1():
    pprint.pprint(globals())

def dict1():
    my_dict = {"name":"young", "age":24, "state":"ohio"}
    print(my_dict.keys())
    print(list(my_dict.keys()))
    print(list(my_dict.items()))

def eggs():
    import this
    import antigravity

def divide(a, b):
    assert b != 0, "divisor can't be zero"
    return a/b

def try_divide():
    try:
        print(divide(19,0))
    except AssertionError as e:
        print(f'Error : {e}')


# Default arguments are stored in the function’s __defaults__ attribute.
# Mutable objects (like lists, dicts, sets) persist across calls if used as defaults.

def append_lst(item, lst=[]):
    lst.append(item)
    return lst

def append_lst_single(item, lst=None):
    if lst == None:
        lst = []
    lst.append(item)
    return lst

def try_append_lst():
    print(append_lst_single(1))
    print(append_lst_single(2))

def objsimple():
    print("" or 15 )
    print(() or [])
    print([] or ())

def logic1():
    obj1 = [1,2,3]
    obj2 = [1,2,3]

    if obj1 is not obj2:
        print(f"{obj1} is not {obj2}")

def map1():
    names = ['alice','bob','charlie','david','eve']
    longnames = filter(lambda x:len(x)>4, names)
    print(f"longname type is {type(longnames)}")
    print(list(longnames))

def main() -> None:
    print(f"my name is {__name__}") 
    print('\u2586')


if __name__ == "__main__":
    # print(docstr_fun1.__doc__)
    # print(docstr_fun1('please', 'go', parameter3='ahead'))
    
    # args_fun1('some', 22, 'days', 'come', name='alice', age=19, role='receptionist')

    main()


