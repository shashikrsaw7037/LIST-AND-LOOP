# Write a Python program to remove duplicates from a list.



# Example list with duplicates
my_list = [3, 3, 4, 4, 5, 6, 6, 7, 8, 8, 5 ,5 ,6 ,7 ,8]
# Initialize an empty list to store unique elements
unique_list = []
# Loop through the original list
for num in my_list:
    # If the element is not already in the unique list, add it
    if num not in unique_list:
        
        unique_list.append(num) 
        
        
# Print the list without duplicates
print("List after removing duplicates:", unique_list)
