# Define the function
def fibonacci(n):
    
# If statement telling the function what to return for n==1 and n==2
    if n in [1,2]:
        return 1
    
# Now return the previous term + the term before it
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter an integer: "))
    
# Using the for loop to check if the fumction works
for i in range(1,n):
    print(fibonacci(i))