str1 = """This is a \u03A9 string with the Greek letter α."""
str2 = "--\u2580--"
str3 = '--\u2580--'

def byte_data():
    # Creating a bytes object
    byte_data = b"Hello World"

    # Accessing individual bytes
    print(byte_data[0])  # Output: 72 (ASCII value of 'H')
    print(byte_data)

    # Converting bytes to string
    string_data = byte_data.decode('utf-8')
    print(string_data)  # Output: Hello World

    # Converting string to bytes
    unicode_string = "Hello You"
    byte_data = unicode_string.encode('utf-8')
    print(byte_data)  # Output: b'Hello World'

    # Converting each byte to hexadecimal
    hex_values = [f"{byte:02x}" for byte in byte_data]
    hex_string = ' '.join(hex_values)
    print(hex_string)  # Output: 48 65 6c 6c 6f 20 57 6f 72 6c 6

def main() -> None:
    print(f"{str3}") 

def loop1():
    dict1 = {'1':'black', '2':'white', '3':'red', '4':'green', '5':'cyan'}
    list1 = ['black', 'white', 'red', 'green', 'cyan']
    for x in dict1:
        print(f"{x} --> {dict1[x]}")
    
    list1.reverse()
    for x in list1:
        print(f'{x} --> {list1.index(x)}')
    
def packing_unpacking():
    # Function Call: func(*arg) → Unpacking (passing elements of arg as separate arguments)
    #   arg: tuple to individual vars, so vars are added to func() call one after one
    # Function Definition: def func(*args) → Packing (collecting all positional arguments into a tuple)
    #   arg: individual vars to tuple, so tuple is passed in
    pass

def unpacking():
    def func(a, b, c):
        print(a, b, c)

    args = (1, 2, 3)
    func(*args)
    func(args,args,args)

def packing():
    def func1(*args):
        print(args)

    def func2(*args):
        print(*args)

    func1(1, 2, 3)
    func2(1,2,3)

def packing1():
    def fun1(arg1,arg2,*args):
        a,b,*c = arg1,arg2,args
        print(a,b,c, sep=";")
        a,b,c = arg1,arg2,args
        print(a,b,c, sep=";")
        a,b,*c = arg1,arg2,*args
        print(a,b,c, sep=";")
        print(a,b,*c, sep=";")
        a,b,c = arg1,arg2,*args

    fun1(12,23,'a','c',44)

def list1():
    time = "17:36"
    hour_minute = time.split(":")
    # print(type(hour_minute))
    # print(type(hour_minute[0]))

    hour, minute = [ int(x) for x in time.split(":") ]
    print(hour,minute,sep='--')

    for i in range(1, 7):
        print(i)

def conditional1():
    a = None

    if a is not None:
        print("a is not None")
    else:
        print("a is not None")

def range1():
    import random
    

if __name__ == "__main__":
    list1()

