
#checking kth with "or" operation    -set
#If bit is 0 → becomes 1
#If bit is 1 → remains 1

class Solution:
    def setKthBit(self, n, k):# here it keeps 13 means in binary 1101 in the place of kth place
        n = n | (1 << k)
        return n

# Input from user
n = int(input("Enter a number (n): "))  # Example: 9
k = int(input("Enter the bit position to set (k): "))  # Example: 1

# Create object
obj = Solution()
result = obj.setKthBit(n, k)

# Output
print(f"Binary before setting bit: {bin(n)}")
print(f"Binary after setting bit {k}: {bin(result)}")
print(f"Decimal result: {result}")
