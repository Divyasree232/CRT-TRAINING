
# patterns

n = int(input("enter a number : "))
for i in range(n): # outer loop indicates number of rows  ||  i indicates row number
    for j in range (n): # inner loop indicates number of columns
        # when n=4
        # if print("*") then vertically 16 stars 
        #if print("*",end=" ") then horizontally prints 16 stars with spaces 
        print("*",end=" ")
    print() # by this print() outside it prints rows 4 and columns 4

# pattern 2 for row plus 1

n = int(input("enter a number : "))
for i in range(n): # outer loop indicates number of rows  AND  i indicates row number
    for j in range (i+1): # inner loop indicates number of columns
        print("*",end=" ")
    print() 
    
# pattern 3 for row minus 1

n = int(input("enter a number : "))
for i in range(n): 
    for j in range (n-i): 
        print("*",end=" ")
    print() 
