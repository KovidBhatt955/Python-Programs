class Pet:
    # Initialize the pet's attributes
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    # Method to display pet information
    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age} years old")


# Creating an object (instance) of the Pet class
my_pet = Pet("Buddy", "Dog", 3)

# Accessing the object's method to show the details
my_pet.display_profile()
