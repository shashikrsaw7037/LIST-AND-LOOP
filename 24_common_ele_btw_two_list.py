# Write a Python program to find the common elements between two lists.
# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)

# Find the intersection of the sets
common_elements = set1.intersection(set2)

# Convert the intersection set back to a list
common_elements_list = list(common_elements)

print("Common elements between the two lists:", common_elements_list)
