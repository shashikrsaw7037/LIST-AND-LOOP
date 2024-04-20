# Write a Python program to find the union of two lists.


# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Combine both lists to form the union
union = list1 + list2

# Remove duplicates by converting the list to a set and back to a list
union = list(set(union))

# Print the union of the two lists
print("Union of the two lists:", union)
