class MyClass:

    # The __new__ method is responsible for creating a new instance of a class. It is called before __init__ and is the method that actually allocates memory for the new object.
    # Return Value: __new__ must return a new instance of the class (usually by calling super().__new__(cls)).
    # Usage: It is typically used in scenarios where you need to control the creation of a new instance, such as when implementing singletons or when subclassing immutable types like tuples or strings.
    def __new__(cls):
        print("Creating instance of", cls)
        # The expression super(MyClass, cls) does not return a new class; rather, it returns a temporary object of the superclass of MyClass that allows you to call methods from the superclass. This is particularly useful in the context of inheritance
        # MyClass is the class for which you want to access the superclass, and cls is a reference to the class that is being instantiated or the class method that is being called.
        instance = super(MyClass, cls).__new__(cls)  # Create a new instance
        return instance

    def __init__(self):
        print("Initializing instance...")

    #class method
    class_variable = 0
    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1
        print("Class variable:", cls.class_variable)

class Class1():
    def __init__(self):
        pass

    def bling(self):
        print("Class1.bling() invoked ")

class Class2():
    def __new__(cls):
        #invalid return Class2
        instance = super(Class2, cls).__new__(cls)
        return instance  # Return the new instanc

    def bling(self):
        print("Class2.bling() invoked ")


def obj1():
    obj = MyClass()
    MyClass.increment_class_variable()

def obj2():
    obj = MyClass()
    print("{0!r}".format(obj))
    print(obj)

def obj3():
    obj = Class2()
    obj.bling()

if __name__ == "__main__":
    obj3()