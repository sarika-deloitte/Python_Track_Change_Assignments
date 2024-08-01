#  Q10. Write a Python program to add two given lists and find the difference between lists. Use map () function.
# nums1 = [6, 5, 3, 9]
# nums2 = [0, 1, 7, 7]

def add_lists(nums1, nums2):
    """
    Adds corresponding elements of two lists.
    
    Parameters:
    nums1 (list): The first list of numbers.
    nums2 (list): The second list of numbers.
    
    Returns:
    list: A new list with the sums of the corresponding elements.
    """
    return list(map(lambda x, y: x + y, nums1, nums2))

def diff_lists(nums1, nums2):
    """
    Finds the difference between corresponding elements of two lists.
    
    Parameters:
    nums1 (list): The first list of numbers.
    nums2 (list): The second list of numbers.
    
    Returns:
    list: A new list with the differences of the corresponding elements.
    """
    return list(map(lambda x, y: x - y, nums1, nums2))

# Example usage
nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]

sum_result = add_lists(nums1, nums2)
diff_result = diff_lists(nums1, nums2)

print("Sum of the two lists:", sum_result)
print("Difference between the two lists:", diff_result)

