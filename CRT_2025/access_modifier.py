class GrandFather():
    def __init__(self):
        self._a = 10
        self.__b = 20

    def _fun1(self):  # protected method ( 1. Protected (_single_underscore)It's a convention (not enforced by Python).
        #It means: “this should not be accessed outside the class or its subclasses”.Python allows access, but you should treat it as internal)
        print("This is our house")

    def __fun2(self):  # private method Private (__double_underscore)Python uses name mangling to make it harder to access from outside.It prevents accidental access — not true security.
        #Cannot be accessed directly from outside the class.
        print("This is my farmhouse")

class Father(GrandFather):
    def fun3(self):
        print("I have 50 cr")

ob = Father()
ob._GrandFather__fun2()   
