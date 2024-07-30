# Question 1: Write a program to get the name of the youngest and oldest in the group.
# File path for question in repo: app/assignment1/data_structures.py ->
# min_max_value function
# Input: {"Kelly":25,"John":30,"Andrew":21,"Sam":32,"Suzane":22}
# Output: {'max_key': 'Andrew', 'min_key': 'Sam'}

def min_max_value(ages):
    if not ages:
        return {"max_key": None, "min_key": None}
    min_key = min(ages, key=ages.get)
    max_key = max(ages, key=ages.get)
    return {"max_key": max_key, "min_key": min_key}

# Example usage
# ages = {"Kelly": 25, "John": 30, "Andrew": 21, "Sam": 32, "Suzane": 22}
# result = min_max_value(ages)
# print(result)  # Output: {'max_key': 'Sam', 'min_key': 'Andrew'}

# Question 2: Write a program to replace each special symbol in given string with #
# File path for question in repo: app/assignment1/data_structures.py -> replace_special_characters function
# Input: str1 = '/*Jon is @developer & musician!!'
# Output: "##Jon is #developer # musician##"

import re

def replace_special_characters(str1):
    return re.sub(r'[^A-Za-z0-9\s]', '#', str1)

# Example usage
# str1 = '/*Jon is @developer & musician!!'
# print(replace_special_characters(str1)) # Output: "##Jon is #developer # musician##"

# Question 3: You are given a nested list of characters, but few characters are missing in the list. Write a program to inject the missing characters at the right place maintaining the order and structure of the list.
# File path for question in repo: app/assignment1/data_structures.py -> extend_list function
# Input:
# List: ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# CharInject: ["h", "i", "j"]
# Output: ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

def extend_list(nested_list, inject_chars):
    # Finding the correct position to insert the missing characters
    def find_deepest_list(lst):
        for item in lst:
            if isinstance(item, list):
                return find_deepest_list(item)
        return lst
    
    deepest_list = find_deepest_list(nested_list)
    deepest_list.extend(inject_chars)
    return nested_list

# Example usage
# nested_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# inject_chars = ["h", "i", "j"]
# print(extend_list(nested_list, inject_chars)) # Output: ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']


# Question 4: You are given unstructured data. Write a program to sort the tuples in ascending order based on the second position value.
# File path for question in repo: app/assignment1/data_structures.py -> sort_tuples function
# Input: tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d',29))
# Output: (('c', 11), ('a', 23), ('d', 29), ('b', 37))

def sort_tuples(tuple1):
    return tuple(sorted(tuple1, key=lambda x: x[1]))

# Example usage
# tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# print(sort_tuples(tuple1)) # Output: (('c', 11), ('a', 23), ('d', 29), ('b', 37))


# Question 5: Tony wants to generate an account report between 2 dates and club them based on number of days. Write a program to calculate the number of days between two given dates so that Tony can easily club the reports.
# File path for question in repo: app/assignment1/data_structures.py -> calculate_number_of_days function
# Input:
# Date 1 – 25-01-2020
# Date 2 – 28-05-2022
# Output: 854

from datetime import datetime

def calculate_number_of_days(date1, date2):
    date_format = "%d-%m-%Y"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    delta = d2 - d1
    return delta.days

# Example usage
# date1 = "25-01-2020"
# date2 = "28-05-2022"
# print(calculate_number_of_days(date1, date2)) # Output: 854

# Question 6: Tony is working on two different data sets and wants to merge them. He is stuck with the problem as the data sets have a lot of common/duplicate items. Write a program to merge given 2 sets keeping the occurrence of duplicate items to only one set.
# File path for question in repo: app/assignment1/data_structures.py -> update_sets function
# Input:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Output:
# set1 = {10, 20, 30, 40, 50, 60, 70}
def update_sets(set1, set2):
    return set1.union(set2)

# Example usage
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(update_sets(set1, set2)) # Output: {70, 40, 10, 50, 20, 60, 30}
