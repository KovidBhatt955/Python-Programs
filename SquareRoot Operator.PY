import math

# Get input from the user
num = float(input("Enter a number: "))

# Method 1: Using the exponentiation operator (power of 0.5)
result1 = num ** 0.5

# Method 2: Using the math library
result2 = math.sqrt(num)

print(f"The square root of {num} is {result1}")
