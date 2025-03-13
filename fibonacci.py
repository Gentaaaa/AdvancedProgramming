#Function to calculate the nth Fibonacci number
 # The Fibonacci squence starts with 0 and 1
  # Each subsequent number is the sum of the two preceding ones 
  # Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
  # Parameter: n (int) - the position in the sequence (0-indexed)
  # Returns: the nth Fibonacci number

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

 #add a few test cases 
print(fibonacci(0)) # Expected: 0
print(fibonacci(1)) # Expected: 1
print(fibonacci(2)) # Expected: 1
print(fibonacci(3)) # Expected: 2
print(fibonacci(4)) # Expected: 3
print(fibonacci(5)) # Expected: 5
print(fibonacci(6)) # Expected: 8
print(fibonacci(7)) # Expected: 13
print(fibonacci(8)) # Expected: 21
print(fibonacci(9)) # Expected: 34

#Improve fibonacci function
def fibonacci(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibonacci(n-1, computed) + fibonacci(n-2, computed)
    return computed[n]