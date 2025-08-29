
# multiple inheritance and super();Method Resolution Order (MRO)
class Base1:
    def __init__(self):
        print("Initializing Base1")
    
    def greet(self):
        print("Hello from Base1")

class Base2:
    def __init__(self):
        print("Initializing Base2")
    
    def greet(self):
        print("Hello from Base2")

class Derived(Base1, Base2):
    def __init__(self):
        super().__init__()  # Calls the __init__ method of Base1
        print("Initializing Derived")
    
    def greet(self):
        super().greet()  # Calls the greet method of Base1
        print("Hello from Derived")

class Base:
    def __new__(cls):
        print(f"Creating instance of {cls.__name__}")
        print("in Base")
        return super(Base, cls).__new__(cls)

class Class2(Base):
    def __new__(cls):
        print(f"Creating instance of {cls.__name__}")
        print("in Class2")
        return super(Class2, cls).__new__(cls)


def obj1():
    # Creating an instance of Derived
    obj = Derived()
    obj.greet()

def obj2():
    obj = Class2()

if __name__ == '__main__':
    obj2()