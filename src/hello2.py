def fun1():
    x = "Hello world"
    y = {1:"x", 2:"y"}

    print("H" in x)
    print(2 in y)
    print(not "H" in x)
    print("x" in y)

def fun2():
    x1 = 10
    y1 = 10
    x2 = "Hello"
    y2 = "Hello"
    x3 = [1, 2, 3]
    y3 = [1, 2, 3]

    print("=====reference equality=======")
    print (x1 is not y1)
    print (x2 is y2)
    print (x3 is y3)
    print("=====value equality=======")
    print (not x1 == y1)
    print (x2 == y2)
    print (x3 == y3)

def typeoperator():
    x = 7.0
    print (x, "is of type", type(x).__name__)
    z = 1+2j
    print ("is", z, "a complex number?", isinstance(1+2j,complex))

    del x,z
    print(x,z)

def typeconversion():
    x, y, z = 5.7, 10, "3.5j"
    print(F'before corce, x type is {type(x)}. y type is {type(y)}. z type is {type(z)} x is {x},y is {y},z is {z}')
    x = int(x); y = float(y); z=complex(z)
    print(F'after corce, x type is {type(x)}. y type is {type(y)}. z type is {type(z)} x is {x},y is {y},z is {z}')

def mathfuns():
    import math as m
    print(max(1.5, -3, 0.23, 10, 12, 7))
    print(round(-7.685, 2))
    print(m.modf(-5.24))

def stringfuns1():
    greeting = "Hello World!"
    print (greeting)
    greeting1 = greeting[:6] + "JohnnyJohnny."

    # TypeError: 'str' object does not support item assignment
    # greeting[6] = '8'
    # greeting[:6] = "JohnnyJohnny."
    print (greeting1)

def stringfuns2():
    greeting = "Hello!"
    name1 = "John"
    name2 = "World"
    message = ("It's me "
    "again")
    print (greeting + " " + name1)
    print (greeting, name2)
    print (greeting * 3, message)

    # escape special characters
    print ("He asked, \"What’s that doing here?\"")
    print ('He asked, "What\’s that doing here?"')

    # String formatting with %
    print ("My name is %s and I am %d years old!" %("John", 21))

    # formatting using format()
    #Using default order
    students1 = "{}, {} and {}".format("John","Mary","Bill")
    print ("\nStudents by Default Order")
    print (students1)
    #Using positional argument
    students2 = "{1}, {0} and {2}".format("John","Mary","Bill")
    print ("\nStudents by Positional Order")
    print (students2)
    #Using keyword argument
    students3 = "{m}, {b} and {j}".format(j="John", m="Mary", b="Bill")
    print ("\nStudents by Keyword Order")
    print (students3)

    # replace(),split(),find(),lower(),join(),format(),

def formatstring():
    name = 'john'; age = 30
    print("I'm {} year old programmer named {}".format(age, name))
    print("I'm {1} year old programmer named {0}".format(name, age))
    print("I'm {age} year old programmer named {name}".format(age=30, name="john"))

def listtupledict():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
        "Oct", "Nov", "Dec"]
    
    print("last half of the months descending", months[-1:-6-1:-1])
    # not working
    # print("last half of the months ascending", months[-1-6+1:-1+1])
    print("last half of the months descending", months[6:])

    subjects = ["Math", "Physics", "Chemistry", "Biology", "History"]
    print("subjects are",subjects)
    subjects.append("computer")
    subjects.remove("Biology")
    del subjects[1]
    print("subjects are",subjects)

    #cmp(l1,l2),len(l),max(l),list(seq:tuple)
    #list.append(x),list.count(),list.extend(l1)
    #list.index(x),list.insert(index,x),list.remove(x),list.pop(x=list[-1]),list.reverse(),list.sort([func])

    #empty_tuple = ()
    #tup = ("year",)
    continents = ("Asia", "Africa", "Americas", "Europe", "Australia")
    print ("continents[0]:", continents[0])
    print ("continents[2:]", continents[2:])
    print ("continents[:-3]", continents[:-3])

    empty_dict = {}
    integerkey_dict = {1: "Mango", 2: "Apple", 3: "Orange"}
    mixedkey_dict = {"name": "John", 0: [2, 4, 3]}
    print (integerkey_dict)
    print (mixedkey_dict)
    print(mixedkey_dict[0])
    print(mixedkey_dict.get('name'))

    student = {"name": "John Doe", "age": 25, "grade": "B+"}
    student['sex'] = 'male'
    student['age'] = 35
    del student['grade']
    #cmp(d1,d2),len(d),str(d)
    #dict.clear(),dict.copy(),dict.fromkeys(seq),dict.get(x,default=None),dict.has_key(x)
    #dict.items(),dict.keys(),dict.values(),dict.setdefault(x,default=None),dict.update(d1)

def loopfuncs1():
    # total = 0
    # for x in range(10,20,2):
    #     print(x)
    #     total += x
    # print(total)

    # numbers = [1,3,5,8,12,4,7,-2]
    # for i in numbers:
    #     print(i)
    # else:
    #     print("no more numbers in the list")

    # #break;continue;pass;
    # for ch in "Hello World":
    #     if ch == 'a':
    #         break
    # else:
    #     print("a not found")
    # print("a found")

    for val in "Hello World!":
        if val == "r":
            continue
        print (val)

    print("====================")
    for val in "Hello World!":
        if val == "r":
            break
        print (val)

def filefuncs1():
    # Print (*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
    with open("poem1.txt", "w+") as file:
        file.write('''The purple cow poem is a short nonsense poem first published in 
                    1895 written by American writer Gelett Burgess''')
    
    with open("poem1.txt", "r") as file:
        text = file.read(100)
        print(text)

    # file.tell() #This returns the position of the current file.
    # File.seek(0) #This method brings the cursor to the start of the file
    # writelines(lines), readlines()
    # readline(max_bytes=-1), readlines(max_bytes=-1)

def example_function(param1, param2, *, keyword_param1, keyword_param2):
    print(f"Positional Parameter 1: {param1}")
    print(f"Positional Parameter 2: {param2}")
    print(f"Keyword Parameter 1: {keyword_param1}")
    print(f"Keyword Parameter 2: {keyword_param2}")

    # Calling the function
    # example_function(10, 20, keyword_param1="Hello", keyword_param2="World")

    # def func1(pos1,pos2,/,pos_or_kw1,pos_or_kw2,*,kw1,kw2):
    # maybe def example_function(param1, param2, /, *args, keyword_param1, keyword_param2, **kwargs):
    # correct def example_function(param1, param2, *args, *, keyword_param1, keyword_param2, **kwargs):


# class NewClass:
#     """This is our first class. What it does
#     is display a string text and a value of
#     variable name"""
#     name = str(input("Enter your name: "))

#     def __init__(self):
#         pass
#     def __eq__(self, value):
#         pass
#     def __hash__(self):
#         pass
#     def __str__(self):
#         pass
#     def __repr__(self):
#         pass


#     def greeting (name):
#         print ("Hello", name)

# def useNewClass():
#     MyObject = NewClass() #Creates a new NewClass object
#     print (NewClass.greeting)
#     print (MyObject.greeting)
#     NewClass.greeting('zha')
#     MyObject.greeting()

def sysfuncs():
    import sys
    print(sys.path)
    
def shallow_deep_copy1():
    print("====reference copy====")
    a = list(range(1,6))
    print("[a] {}".format(a))
    b = a
    print("[b] {}".format(b))
    b.append(6)
    print("[a] {}".format(a))
    print("[b] {}".format(b))

    print("====value copy====")
    a = list(range(1,6))
    print("[a] {}".format(a))
    b = a[:]
    print("[b] {}".format(b))
    b.append(6)
    print("[a] {}".format(a))
    print("[b] {}".format(b))

def shallow_deep_copy2():
    lst1 = ['a', 'b', ['ab', 'ba']]
    lst2 = lst1[:]
    lst2[0] = 'c'
    lst2[2][1] = 'c'
    print("[lst1] {}".format(lst1))
    print("[lst2] {}".format(lst2))

def deep_copy1():
    from copy import deepcopy

    list1 = ['a', 'b', ['ab', 'ba']]
    list2 = deepcopy(list1)
    list2[0] = 'c'
    list2[2][0] = 'c'
    print('list1, {}'.format(list1))
    print('list2: {0}'.format(list2))

def greet():
    return "Hello!"
def square(x):
    return x ** 2

def apply_func(func, val):
    return func(val)
def make_multiplier(factor):
    def multiplier(x):
        return x*factor
    return multiplier


def first_citizen():
    print(apply_func(square, 10))

    triple = make_multiplier(3)
    print(triple(10))

    functions = [greet, square]
    for func in functions:
        print(func(5) if func == square else func())


if __name__ == "__main__":
    first_citizen()
