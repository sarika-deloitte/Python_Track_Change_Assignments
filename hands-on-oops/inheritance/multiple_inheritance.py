### Multiple Inheritance
#  Multiple inheritance is when a class can be derived from more than one base class.


# Base classes
class Engine:
    def brand(self):
        return "Brand A"

class Wheels:
    def count(self):
        return 4

# Derived class
class Car(Engine, Wheels):
    def details(self):
        return f"Engine brand: {self.brand()}, Wheels count: {self.count()}"

# Create an instance of Car
car = Car()
print("\nMultiple Inheritance:")
print(car.details())  # Output: Engine brand: Brand A, Wheels count: 4
