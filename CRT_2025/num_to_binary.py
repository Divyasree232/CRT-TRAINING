
# Bit Manipulation
# Decimal to binary

# Ask the user to input a number and store it as an integer in variable 'n'
n = int(input("Enter a number: "))

# Initialize an empty string to store the binary result
binaryResult = ""

# Use a loop to convert the decimal number to binary
while n != 0:
    rem = n % 2                    # Get the remainder when n is divided by 2 (this is the binary digit)
    binaryResult += str(rem)       # Add the digit (as a string) to the result (in reverse order)
    n = n // 2                     # Divide n by 2 (integer division) to process the next bit
# Since the binary digits were added in reverse, reverse the string to get correct binary
print(binaryResult[::-1])          # Print the final binary representation


 # bin is used to covert number to binary number
 # n= 13
 #print(bin(n)) with output 0b1101
 
 #bin without getting 0b
 #n=13
 #print(bin(n)[2::]) with output 1101 which 0b by using [2::]
