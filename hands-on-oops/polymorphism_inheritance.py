#  Q6. Write a program to demonstrate polymorphism with inheritance.
# Base class
class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class 1
class Dog(Animal):
    def sound(self):
        return "Bark"

# Derived class 2
class Cat(Animal):
    def sound(self):
        return "Meow"

# Derived class 3
class Cow(Animal):
    def sound(self):
        return "Moo"

# Function to demonstrate polymorphism
def make_animal_sound(animal):
    print(animal.sound())

# Create instances of each class
dog = Dog()
cat = Cat()
cow = Cow()

# Demonstrate polymorphism
print("Polymorphism Demonstration:")
make_animal_sound(dog)  # Output: Bark
make_animal_sound(cat)  # Output: Meow
make_animal_sound(cow)  # Output: Moo
