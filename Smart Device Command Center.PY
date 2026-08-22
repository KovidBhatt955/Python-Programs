from abc import ABC, abstractmethod

# --- Base Abstract Class ---
class SmartDevice(ABC):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on
        status = "ON" if self.is_on else "OFF"
        print(f"[{status}] {self.name} in {self.location}")

    @abstractmethod
    def activate(self):
        pass

# --- Concrete Subclasses ---
class Light(SmartDevice):
    def activate(self):
        if self.is_on:
            print(f"Action: Dimming {self.name} to 80% brightness.")

class Thermostat(SmartDevice):
    def activate(self):
        if self.is_on:
            print(f"Action: Adjusting {self.name} temperature to 72F.")

class Camera(SmartDevice):
    def activate(self):
        if self.is_on:
            print(f"Action: {self.name} is now recording a live video feed.")

# --- Polymorphism in Action ---
if __name__ == "__main__":
    devices = [
        Light("Living Room Light", "Main Hall"),
        Thermostat("Nest", "Hallway"),
        Camera("Ring Cam", "Front Door")
    ]

    print("--- Powering On Devices ---")
    for device in devices:
        device.toggle()

    print("\n--- Running System Routine ---")
    for device in devices:
        device.activate()
