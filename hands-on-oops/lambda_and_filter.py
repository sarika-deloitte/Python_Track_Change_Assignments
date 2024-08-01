# Q4. Write a function to print out the intersection of two arrays in Python using Lambda expression and filter function

def intersection(arr1, arr2):
    # Use filter and lambda to find the intersection
    intersected_elements = list(filter(lambda x: x in arr2, arr1))
    return intersected_elements

# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
result = intersection(array1, array2)
print("The intersection of the two arrays is:", result)