# Taking input from the user
age = int(input("Enter your age: "))

# Outer condition
if age >= 10:
    # Inner (nested) condition
    if age <= 20:
        print("The age is between 10 and 20.")
    else:
        print("The age is not between 10 and 20 (it is greater than 20).")
else:
    print("The age is not between 10 and 20 (it is less than 10).")
