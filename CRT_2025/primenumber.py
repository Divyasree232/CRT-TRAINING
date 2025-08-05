
#prime numbers code

num = int(input("enter a number : "))
factorsCount=0
for i in range(1,num+1):
    if(num%i==0):
        factorsCount=factorsCount+1
if(factorsCount==2):
    print("prime")
else:
    print("not prime")
