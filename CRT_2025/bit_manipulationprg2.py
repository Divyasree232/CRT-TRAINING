# Binary string to convert
binaryString = "1101"

# p2 will represent powers of 2 (starting from 2^0 = 1)
p2 = 1

# Initialize result to 0 (this will store the final decimal number)
result = 0

# Loop through each bit in reverse (starting from rightmost bit)
for i in binaryString[::-1]:  # [::-1] means reverse the string
    if i == '1':              # If the current bit is 1
        result = result + p2  # Add the current power of 2 to the result
    p2 = p2 * 2               # Move to the next power of 2 (2^1, 2^2, etc.)

# Print the final decimal result
print(result)
