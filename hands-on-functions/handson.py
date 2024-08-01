#  1. Write a program to create function func1() to accept a variable length of arguments and print their value.

def func1(*args):
    for arg in args:
        print(arg, end= ' ')
    return 

# Example usage
# func1(1, 2, 3, 4)  # Output: 1 2 3 4
# func1('a', 'b', 'c')  # Output: a b c

# 2. Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

# Example usage
# result = calculation(10, 5)
# print(result)  # Output: (15, 5)

# 3. Write a function to find the sum of a list of numbers

def sum_of_list(numbers):
    return sum(numbers)

# Example usage
# numbers = [1, 2, 3, 4, 5]
# print(sum_of_list(numbers))  # Output: 15

# Q4 onwards check in decorator_fun.py