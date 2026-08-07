# Create class
class Employee:

    # Initializing
    def __init__(self):
        print("Employee Created")

    # Calling destructor
    def __del__(self):
        print("Employee Exploded")

def Create_obj():
    print("Making Object...")
    obj = Employee()
    print("Function end...")
    return obj

print("Calling Create_obj() function...")
obj = Create_obj()
print("The Beautiful Program ends")