# Write a Python program to count the frequency of each element in a list.




# Example list
my_list = [1, 2, 3, 1, 2, 1, 4, 5, 4]

# Initialize an empty dictionary to store the frequencies
frequency_dict = {} #  {1 -->element:1+1+1 -->frequency, 2:1+1, 3:1, 4:1+1, 5:1} 

# Count the frequency of each element in the list
for element in my_list:#
    if element in frequency_dict:#false
        frequency_dict[element] += 1
    else:
        frequency_dict[element] = 1

# Print the frequencies
for element, frequency in frequency_dict.items():
    print(f"Element {element}: Frequency {frequency}") #O/P
                                      