# 1. Create the parent Vehicle class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return f"The engine of the {self.make} {self.model} is starting."


# 2. Build a child Car class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, doors):
        # 3. Use super() to inherit parent features
        super().__init__(make, model)
        self.doors = doors

    # 4. Override a method from the parent class
    def start_engine(self):
        parent_msg = super().start_engine()
        return f"{parent_msg} It is a sleek {self.doors}-door car."


# --- Demonstration and Verification ---

# Create an instance of the child class
my_car = Car("Tesla", "Model 3", 4)

# Call the overridden method
print(my_car.start_engine())

# 5. Check the inheritance relationship with issubclass()
is_child = issubclass(Car, Vehicle)
print(f"Is Car a subclass of Vehicle? {is_child}")
