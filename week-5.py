#  Polymorphism Challenge  No. 2: Vehicles

class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("🚗 Car is driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("✈️ Plane is flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("🚤 Boat is sailing on the water!")

# Testing polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
