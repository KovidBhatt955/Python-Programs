# Power Calculator

# Input the base and exponent
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = 1

# Using a loop to multiply the base 'n' times
for _ in range(exponent):
    result *= base

print(f"{base} raised to the power of {exponent} is: {result}")
