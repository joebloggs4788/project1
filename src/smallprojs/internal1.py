# You can view the MRO of a class using the __mro__ attribute or the mro() method
from pprint import *

class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B, C):
    pass

d = D()
d.method()
pprint(D.mro())