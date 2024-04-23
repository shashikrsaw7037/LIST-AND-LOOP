
# Write a Python program to remove the nth index element from a list.

# Example list
my_list = [11, 24, 31, 84, 35]

# Index of the element to remove
n = int(input("Enter the index of the element to remove: "))

# Check if the index is valid
if 0 <= n < len(my_list):
    # Remove the element at index n
    removed_element = my_list.pop(n)
    print("Element removed:", removed_element)
    print("List after removal:", my_list)
else:
    print("Invalid index. Please enter a valid index.")
