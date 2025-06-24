# Function to calculate the nth Fibonacci number
# The Fibonacci sequence starts with 0 and 1
# Each subsequent number is the sum of the two preceding ones 
# Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Parameter: n (int) - the position in the sequence (0-indexed)
# Returns: the nth Fibonacci number

# Simple recursive version
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Add a few test cases
print("Simple Recursive Version:")
print(fibonacci(0))  # Expected: 0
print(fibonacci(1))  # Expected: 1
print(fibonacci(2))  # Expected: 1
print(fibonacci(3))  # Expected: 2
print(fibonacci(4))  # Expected: 3
print(fibonacci(5))  # Expected: 5
print(fibonacci(6))  # Expected: 8
print(fibonacci(7))  # Expected: 13
print(fibonacci(8))  # Expected: 21
print(fibonacci(9))  # Expected: 34

# Improved version with memoization
def fibonacci_optimized(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibonacci_optimized(n-1, computed) + fibonacci_optimized(n-2, computed)
    return computed[n]

# Test optimized version
print("\nOptimized Version with Memoization:")
for i in range(10):
    print(fibonacci_optimized(i))  # Expected: same as above
