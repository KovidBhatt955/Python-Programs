# Create a class 
class Student:
    grade = 10
    print("Hello I am a student of grade", grade)

# Create an object
ob = Student()

# Create a class
class Vehicle:

# Create init method
   def __init__(self, max_Speed, mileage):

       # Bind the arguements\
       self.max_speed = max_Speed
       self.mileage = mileage

# Object Creation
modelX = Vehicle(240, 18)

# Access the variables inside init method
print("Model Max Speed : ", modelX.max_speed)
print("Model Mileage : ", modelX.mileage)

# Create a class
class Parrot:

    # Class attribute
    species = "Bird"

    # Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Parrot class
blu = Parrot("Blu", 10)
woo= Parrot("Woo", 15)

# Access the class attributes
print("Blu is a {}", format(blu.species))
print("Woo is also a {}", format(woo.species))

# Access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))