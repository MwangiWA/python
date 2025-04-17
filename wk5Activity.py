# Base class for all vehicles
class Vehicle:
    def move(self):
        # Placeholder method meant to be overridden by subclasses
        pass

# Subclass representing a Car
class Car(Vehicle):
    def move(self):
        # Specific implementation for car movement
        print("Car is driving 🚗")

# Subclass representing a Plane
class Plane(Vehicle):
    def move(self):
        # Specific implementation for plane movement
        print("Plane is flying ✈️")

# Subclass representing a Boat
class Boat(Vehicle):
    def move(self):
        # Specific implementation for boat movement
        print("Boat is sailing 🚢")

# List of different vehicle objects
vehicles = [Car(), Plane(), Boat()]

# Loop through each vehicle and call the move() method
# This demonstrates polymorphism – same method name, different behaviors
for v in vehicles:
    v.move()
