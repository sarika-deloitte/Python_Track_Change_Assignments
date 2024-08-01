#  Q8. Write a class which has static, instance and class methods defined in it.
class MyClass:
    # Class attribute
    class_attribute = "I am a class attribute"

    def __init__(self, instance_attribute):
        # Instance attribute
        self.instance_attribute = instance_attribute

    # Instance method
    def instance_method(self):
        print(f"Instance method called. Instance attribute: {self.instance_attribute}")

    # Class method
    @classmethod
    def class_method(cls):
        print(f"Class method called. Class attribute: {cls.class_attribute}")

    # Static method
    @staticmethod
    def static_method():
        print("Static method called. No access to instance or class attributes.")

# Example usage
# Create an instance of MyClass
my_instance = MyClass("I am an instance attribute")

# Call instance method
my_instance.instance_method()  # Output: Instance method called. Instance attribute: I am an instance attribute

# Call class method
MyClass.class_method()  # Output: Class method called. Class attribute: I am a class attribute

# Call static method
MyClass.static_method()  # Output: Static method called. No access to instance or class attributes.
