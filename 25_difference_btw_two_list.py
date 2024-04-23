# Write a Python program to find the difference between two lists.
# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5]

# Find the difference between the two lists using a loop and condition
difference = []
for x in list1:
    if x not in list2:
        difference.append(x)

print("Difference between list1 and list2:", difference)
