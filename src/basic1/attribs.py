class MyClass:
    class_attr = "I am a class attribute"

    def __init__(self, value):
        self.instance_attr = value

def get_attrs():
    # Accessing class attributes
    class_attributes = MyClass.__dict__
    print("Class Attributes:")
    for attr, value in class_attributes.items():
        print(f"{attr}: {value}")

    # Creating an instance of MyClass
    obj = MyClass("I am an instance attribute")

    # Accessing instance attributes
    instance_attributes = obj.__dict__
    print("\nInstance Attributes:")
    for attr, value in instance_attributes.items():
        print(f"{attr}: {value}")

if __name__ == '__main__':
    get_attrs()