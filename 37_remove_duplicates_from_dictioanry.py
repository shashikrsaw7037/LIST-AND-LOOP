# Write a Python program to remove duplicates from a dictionary.

# # Original dictionary with duplicates
# original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2,'e': 2}

# # Create an empty dictionary to store unique key-value pairs
# unique_dict = {}

# # Iterate through the original dictionary
# for key, value in original_dict.items():
#     # Check if the key is already present in the unique dictionary
#     if key not in unique_dict:
#         # If not present, add the key-value pair to the unique dictionary
#         unique_dict[key] = value

# # Print the original and unique dictionaries
# print("Original Dictionary                 :", original_dict)
# print("Dictionary after removing duplicates:", unique_dict)














# ########Write a Python program to remove duplicates from a dictionary.

# Python3 code to demonstrate working of
# Remove duplicate values in dictionary
# Using loop

# initializing dictionary
test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}

# printing original dictionary
print("The original dictionary is : " +str(test_dict))

# Remove duplicate values in dictionary
# Using loop
temp = []
res = dict()#dictionary data type

for key, val in test_dict.items():

	if val not in temp:
		temp.append(val)
		res[key] = val

# printing result
print("The dictionary after values removal : " + str(res))
