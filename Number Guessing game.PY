secret_number = 85
num = int(input("Enter a secret Number from 10 100"))
if num == secret_number:
   print("That is correct!!!!!!")
elif num > secret_number:
    print("You are close.")
else:
    print("You are Far!")
