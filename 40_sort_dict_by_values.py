# 40. Write a Python program to sort a dictionary by value
# my_dict = {'b': 2, 'a': 1, 'd': 4, 'c': 3}

# a=my_dict.values()
# sort_dict = sorted(a)
# print(sort_dict)


# Define the dictionary
my_dict = {'z': 2, 'a': 1, 'd': 4, 'c': 3}

# Sort the dictionary by values and store the result in a list of tuples
sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])

# Create a new dictionary from the sorted list of tuples
sorted_dict = dict(sorted_dict)

# Print the sorted dictionary
print("Dictionary sorted by values:", sorted_dict)
