
# recursion exzmple

def fun1(x):
    if(x==0):
        return
    print(x)
    fun1(x-1)
x=4
fun1(x)

#first it goes to function definition ,then it checks outside the def function.
#next it takes first line as x=4
#next it takes function call , then it goes to th funcyio  definition.
#checks whether x is equal to zero or not , if not it prints x values as 4
#next fun1(x-1) means 4-1 now 3 next 2 next 1
# returns the output now when x becomes 0
