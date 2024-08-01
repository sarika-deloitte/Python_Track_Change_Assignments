### Hybrid Inheritance
#  Hybrid inheritance is a combination of two or more types of inheritance.


# Base class
class Animal:
    def sound(self):
        return "Some generic sound"

# Intermediate derived class
class Mammal(Animal):
    def has_fur(self):
        return True

# Another base class
class Pet:
    def is_pet(self):
        return True

# Final derived class
class Dog(Mammal, Pet):
    def sound(self):
        return "Bark"

# Create an instance of Dog
dog = Dog()
print("\nHybrid Inheritance:")
print(dog.sound())  # Output: Bark
print(dog.has_fur())  # Output: True
print(dog.is_pet())  # Output: True
