
#subsets code for when subset is equal to k

nums = list(map(int,input().split()))
k=int(input())
n = len(nums)
total_subsets = 1 << n  # 2^n subsets
ans = []

for val in range(total_subsets):
    lst = []
    for i in range(n):
        if val & (1 << i):
            lst.append(nums[i])
    ans.append(lst)
for subset in ans:
    if sum(subset)==k:
        print("subset is equal to k when : ",subset)
