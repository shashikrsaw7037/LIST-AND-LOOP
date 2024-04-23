# Write a Python program to remove a key from a dictionary.
# Example dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Key to remove
key_to_remove = input("Enter the key to remove: ")

# Method 1: Using the del keyword
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"Key '{key_to_remove}' removed using del:", my_dict)
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")

# Method 2: Using the pop() method
removed_value = my_dict.pop(key_to_remove, None)
if removed_value is not None:
    print(f"Key '{key_to_remove}' removed using pop:", my_dict)
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")
