
# To take given n is power of2 or not

n= int(input())
if(n==0):
    print(False)
print(n&(n-1)==0)

