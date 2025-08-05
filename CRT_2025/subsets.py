
#subsets

nums = list(map(int,input().split()))
n = len(nums)
total_subsets = 1 << n  # 2^n subsets
ans = []

for val in range(total_subsets):
    lst = []
    for i in range(n):
        if val & (1 << i):
            lst.append(nums[i])
    ans.append(lst)

# Print all subsets
print("All subsets:")
for subset in ans:
    print(subset)
