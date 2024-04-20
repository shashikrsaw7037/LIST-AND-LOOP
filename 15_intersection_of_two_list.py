# Write a Python program to find the intersection of two lists.

# Example lists

list1 = [3, 4, 5, 6, 7]
list2 = [5, 6, 7, 8, 9]
# Initialize an empty list to store the intersection
intersection = []

# Loop through elements of list1
for element in list1:#5
    # Check if the element is present in list2
    if element in list2:
       # Add the element to the intersection list if it's present in both lists
        intersection.append(element)

# Print the intersection of the two lists
print("Intersection of the two lists:", intersection)
