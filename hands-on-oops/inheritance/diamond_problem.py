# Base class
class A:
    def __init__(self):
        print("A's constructor")

    def method(self):
        print("Method from class A")

# Intermediate derived class 1
class B(A):
    def __init__(self):
        super().__init__()
        print("B's constructor")

    def method(self):
        print("Method from class B")

# Intermediate derived class 2
class C(A):
    def __init__(self):
        super().__init__()
        print("C's constructor")

    def method(self):
        print("Method from class C")

# Final derived class
class D(B, C):
    def __init__(self):
        super().__init__()
        print("D's constructor")

# Create an instance of D
d = D()
print("\nDiamond Problem Demonstration:")
d.method()

# Display the Method Resolution Order
print("\nMethod Resolution Order (MRO):")
print(D.mro())

