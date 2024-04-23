#31. Write a Python program to check if a given key exists in a dictionary.


# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
# Key to check
key_to_check = 'b'
# Flag to indicate if key exists
key_exists = False 
# Iterate through each key-value pair in the dictionary
for key in my_dict:#{'a': 1, 'b': 2, 'c': 3}
    # Check if the current key matches the key to check
    if key == key_to_check: 
        # Set the flag to True and break the loop
        key_exists = True
        break
# Check the result
if key_exists:
    print("The key '{}' exists in the dictionary.".format(key_to_check))
else:
    print("The key '{}' does not exist in the dictionary.".format(key_to_check))

















def check_key(dictionary, key):
    if key in dictionary:
        print(f"The key '{key}' exists in the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
check_key(my_dict, 'b')  # Output: The key 'b' exists in the dictionary.
check_key(my_dict, 'd')  # Output: The key 'd' does not exist in the dictionary.
