#  Q7. Write a class called Employee with instance variables: name and salary and an instance method: getDetails().  Make the instance variables - (name and salary) private, public, and protected in three separate examples and print the value of these variables in the method getDetails().

class EmployeePublic:
    def __init__(self, name, salary):
        self.name = name  # Public variable
        self.salary = salary  # Public variable

    def getDetails(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

# Example usage
employee_public = EmployeePublic("Alice", 50000)
employee_public.getDetails()  # Output: Name: Alice, Salary: 50000
print(employee_public.name)  # Output: Alice
print(employee_public.salary)  # Output: 50000


### Example 2: Protected Instance Variables

class EmployeeProtected:
    def __init__(self, name, salary):
        self._name = name  # Protected variable
        self._salary = salary  # Protected variable

    def getDetails(self):
        print(f"Name: {self._name}, Salary: {self._salary}")

# Example usage
employee_protected = EmployeeProtected("Bob", 60000)
employee_protected.getDetails()  # Output: Name: Bob, Salary: 60000
print(employee_protected._name)  # Output: Bob (not recommended to access directly)
print(employee_protected._salary)  # Output: 60000 (not recommended to access directly)


### Example 3: Private Instance Variables
# Private instance variables are indicated by a double underscore and cannot be accessed directly from outside the class.

class EmployeePrivate:
    def __init__(self, name, salary):
        self.__name = name  # Private variable
        self.__salary = salary  # Private variable

    def getDetails(self):
        print(f"Name: {self.__name}, Salary: {self.__salary}")

# Example usage
employee_private = EmployeePrivate("Charlie", 70000)
employee_private.getDetails()  # Output: Name: Charlie, Salary: 70000

# The following lines will raise an AttributeError
# print(employee_private.__name)  # AttributeError
# print(employee_private.__salary)  # AttributeError

# Accessing private variables using name mangling
print(employee_private._EmployeePrivate__name)  # Output: Charlie (not recommended)
print(employee_private._EmployeePrivate__salary)  # Output: 70000 (not recommended)

