# Take marks as imput from user
print("Enter marks obtaines in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

# Let's calculate the percentage of the marks
sum = math+english+science+hindi
print("Sum of math, english, science and hindi are = ", sum)

perc = (sum/400)*100

print(end = "Percentage Mark = ")
print(perc)