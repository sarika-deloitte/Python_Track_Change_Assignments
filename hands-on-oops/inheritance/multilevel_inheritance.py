### Multi-Level Inheritance
#  Multi-level inheritance is when a class is derived from another derived class.

# Base class
class Animal:
    def sound(self):
        return "Some generic sound"

# Intermediate derived class
class Mammal(Animal):
    def has_fur(self):
        return True

# Final derived class
class Cat(Mammal):
    def sound(self):
        return "Meow"

# Create an instance of Cat
cat = Cat()
print("\nMulti-Level Inheritance:")
print(cat.sound())  # Output: Meow
print(cat.has_fur())  # Output: True

