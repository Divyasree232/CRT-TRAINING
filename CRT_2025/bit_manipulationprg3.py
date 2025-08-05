

#checking with reverse to "or"  - clear (if the kth position 0->0 otherwise 1->0)
print("\n checking with reverse to 'or'\n ")
n=int(input())
k=int(input())
n=n&(~(1<<k))
print(n)


#toggle kth bit


print("\n toggle kth bit \n")
n=int(input()) # 1 1 0 1
k=int(input()) # if k=1 then 0 0 1 0 EX-OR means o->1 and 1->0 to all numbers
n=n^(1<<k)
print(n)

