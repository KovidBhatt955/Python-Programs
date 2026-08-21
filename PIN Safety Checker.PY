class Account:
    def __init__(self, owner: str, pin: str):
        self.owner = owner
        self.__pin = pin  # Private attribute

    # Getter/Setter for secure PIN modification
    def set_pin(self, old_pin: str, new_pin: str) -> bool:
        if old_pin == self.__pin:
            if len(new_pin) >= 4 and new_pin.isdigit():
                self.__pin = new_pin
                return True
        return False

    # Special function to control object string representation
    def __str__(self) -> str:
        return f"Account owner: {self.owner}, PIN status: Configured [SECURE]"

# Testing encapsulation and functionality
if __name__ == "__main__":
    acc = Account("Alice", "1234")
    
    # Testing private attribute access outside the class (will raise AttributeError)
    try:
        print(acc.__pin)
    except AttributeError:
        print("Cannot access private attribute __pin directly outside the class.")

    # Updating private data safely using the setter method
    success = acc.set_pin("1234", "5678")
    print(f"PIN update success: {success}")

    # Using __str__ special function with print()
    print(acc)
