
# polymorphism
# Method over load
print("\nMethod over load\n")
class MethodOverload():
    def fun1(self,a=0,b=0,c=0):
        print(a,b,c)
ob=MethodOverload()
ob.fun1(10,20,30)
ob.fun1(10,20)
ob.fun1(10)
ob.fun1()

# Method over ride
print("\nMethod over ride\n")
class MethodOverride():
    def fun1(self):
        print("Hwy java!!!")
class Hello(MethodOverride):
    def fun1(self):
        print("Hey python!!")
ob= Hello()
ob.fun1()
