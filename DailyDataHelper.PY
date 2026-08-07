class DailyDataHelper:
    def __init__(self, data_list=None):
        """Constructor to set default values."""
        if data_list is None:
            self.data_list = ["Exercise", "Read", "Code", "Meditate"]
        else:
            self.data_list = data_list
        print("Daily Data Helper initialized with tasks.")

    def search_task(self, target_value):
        """Uses enumerate() to search with both index numbers and data values."""
        found = False
        for index, value in enumerate(self.data_list):
            if value.lower() == target_value.lower():
                print(f"Found '{value}' at index {index}.")
                found = True
        if not found:
            print(f"'{target_value}' not found in the list.")

    def display_all(self):
        """Helper method to list all current items."""
        print("\nCurrent Daily Data List:")
        for index, value in enumerate(self.data_list):
            print(f"  [{index}] {value}")

    def __del__(self):
        """Destructor to show when an object ends."""
        print("Daily Data Helper object destroyed. Session ended.")


# --- Demonstration of the Class ---
if __name__ == "__main__":
    # 1. Create object (triggers constructor with default values)
    helper = DailyDataHelper()
    
    # 2. Display the data
    helper.display_all()
    
    # 3. Search using enumerate functionality
    print("\n--- Searching Data ---")
    helper.search_task("Code")
    helper.search_task("Sleep")
    
    # 4. Explicitly delete to trigger the destructor
    print("\n--- Closing Session ---")
    del helper
