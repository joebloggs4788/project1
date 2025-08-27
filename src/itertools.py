import itertools

def fun1():
    print(list(itertools.chain([1, 2, 3, 4], range(5,9), "the quick and the slow")))

    cycler = itertools.cycle([10,20,33])
    for i in range(30):
        print(f"{i} -- {cycler.__next__()}")

    list1 = [1,2,3,4]
    list2 = ['a','b','c','d','e']
    result = itertools.zip_longest(list1,list2)
    print(f"{type(result)} -- {list(result)}")

if __name__ == '__main__':
    fun1()