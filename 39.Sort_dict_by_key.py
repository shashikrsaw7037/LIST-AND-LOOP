# 39. Write a Python program to sort a dictionary by key.
# # Define the dictionary
my_dict = {'b': 2, 'a': 1, 'd': 4, 'c': 3}

# Sort the dictionary by keys and store the result in a list of tuples
sorted_dict = sorted(my_dict.items())

# Create a new dictionary from the sorted list of tuples
sorted_dict = dict(sorted_dict)
sorted_dict = sorted(my_dict)
# Print the sorted dictionary
print("Dictionary sorted by keys:", sorted_dict)






































# Create a dictionary 'color_dict' with color names as keys and their corresponding color codes in hexadecimal format as values.
color_dict = {
    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}

# Iterate through the keys of the 'color_dict' dictionary after sorting them in lexicographical order.
for key in sorted(color_dict):
    # Print each key-value pair where '%s' is a placeholder for the key and its associated color code.
    print("%s: %s" % (key, color_dict[key]))
	