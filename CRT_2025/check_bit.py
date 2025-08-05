
#checking kth bit with "and" operation  - check

class Solution:
    def checkKthBit(self, n, k):
        if (n & (1 << k)) == 0:
            return False
        return True
# Taking input
n = int(input("Enter a number (n): "))  # Example: 13
k = int(input("Enter the bit position (k): "))  # Example: 2
# Creating object and calling method
obj = Solution()
result = obj.checkKthBit(n, k)
# Printing result
print("K-th bit is set:", result)
