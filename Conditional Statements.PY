# Program to determine grade based on score

# Input: Get the score from the user
score = float(input("Enter your score (0-100): "))

# Conditional statements to check the grade
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
