### Single Inheritance
# Single inheritance involves a single child class inheriting from a single parent class.

# Base class
class Animal:
    def sound(self):
        return "Some generic sound"

# Derived class
class Dog(Animal):
    def sound(self):
        return "Bark"

# Create an instance of Dog
dog = Dog()
print("Single Inheritance:")
print(dog.sound())  # Output: Bark

