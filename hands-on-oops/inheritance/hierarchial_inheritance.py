### Hierarchical Inheritance
#  Hierarchical inheritance is when multiple classes are derived from a single base class.

# Base class
class Animal:
    def sound(self):
        return "Some generic sound"

# Derived class 1
class Dog(Animal):
    def sound(self):
        return "Bark"

# Derived class 2
class Cat(Animal):
    def sound(self):
        return "Meow"

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()
print("\nHierarchical Inheritance:")
print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow
