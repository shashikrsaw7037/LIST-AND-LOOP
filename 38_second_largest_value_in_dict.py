# 38. Write a Python program to find the second largest value in a dictionary



# # Define the dictionary
# my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# # Extract values from the dictionary
# values = list(my_dict.values())

# # Sort the values in descending order
# values.sort(reverse=True)

# # Check if there are at least two unique values in the dictionary
# if len(set(values)) >= 2:
#     # The second largest value is the second element in the sorted list
#     second_largest = values[1]
#     print("The second largest value in the dictionary is:", second_largest)
# else:
#     print("There are not enough unique values in the dictionary to find the second largest value.")




# 38. Write a Python program to find the second largest value in a dictionary
# Python code to find second largest
# element from a dictionary using sorted() method

# creating a new Dictionary
example_dict = {"mark": 13, "steve": 3, "bill": 6, "linus": 11} #3,6,11,13

# now directly print the second largest
# value in the dictionary
print("Output1:", sorted(example_dict.values())[-2]) #11

# More than 1 keys with maximum value are present
example_dict = {"fb": 20, "whatsapp": 12, "instagram": 20, "oculus": 10}  # 20,12,10
print("Output2:", sorted(set(example_dict.values()), reverse=True)[-2])
            #10,12,20