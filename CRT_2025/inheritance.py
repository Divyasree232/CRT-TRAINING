
#single inheritance
print("single inheritance\n")
class Father():
    def fun1(self):
        print("I can do job")
class Son(Father):
    def fun2(self):
        print("I can play")
ob=Son()
ob.fun1()

#mutli level inheritance
print("\n mutli level inheritance\n")
class GrandFather():
    def fun1(self):
        print("I can do farm")
class Father(GrandFather):
    def fun2(self):
        print("I can do job")
class Son(Father):
    def fun3(self):
        print("I can play")
ob=Son()
ob.fun1()

#multiple inheritance
print("\n multiple inheritance\n")
class Mother():
    def fun1(self):
        print("I can cook")
class Father():
    def fun2(self):
        print("I can cook")
class Son(Mother,Father):
    def fun3(self):
        print("I can play")
ob=Son()
ob.fun3()
ob.fun2()
ob.fun1()
