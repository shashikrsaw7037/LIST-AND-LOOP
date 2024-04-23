############# Write a Python program to create a dictionary from two lists.




# Example lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Create a dictionary from the lists
result_dict = dict(zip(keys, values))

print("Resulting dictionary:", result_dict)
