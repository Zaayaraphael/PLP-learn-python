# Assignment 1: Design Your Own Class

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery  # percentage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}%")

    def info(self):
        print(f"📱 {self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}%")

# Inheritance Example
class iPhone(Smartphone):
    def __init__(self, model, storage, battery, ios_version):
        super().__init__("Apple", model, storage, battery)  # parent constructor
        self.ios_version = ios_version

    def use_siri(self):
        print(f"{self.model} says: 'Hey Siri!' 🤖")

    # Overriding (Polymorphism example inside inheritance)
    def info(self):
        print(f"🍎 iPhone {self.model} (iOS {self.ios_version}) | Storage: {self.storage}GB | Battery: {self.battery}%")


# Testing the classes
phone1 = Smartphone("Samsung", "Galaxy S23", 128, 80)
phone1.info()
phone1.call("08012345678")
phone1.charge(15)

print("\n--- iPhone Inheritance Example ---")
iphone1 = iPhone("14 Pro", 256, 60, "iOS 17")
iphone1.info()
iphone1.use_siri()
