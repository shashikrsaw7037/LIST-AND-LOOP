# Write a Python program to find the second largest element in an array.
from array import *
arr =array('i', [101, 107, 2017, 1098, 7832, 763467, 213486, 76312867])
arr1 =sorted(arr)
print(arr1)
print("the second largest element in an array :",arr1[-2])





# from array import *
# arr = array('i', [101, 107, 2017, 1098, 7832, 763467, 213486, 76312867])
# # Initialize the maximum and second maximum elements
# max_element = arr[0]
# second_max_element = arr[0]                                                //////CHATGPT
# # Find the maximum element in the array
# for num in arr:
#     if num > max_element:
#         second_max_element = max_element
#         max_element = num
#     elif num > second_max_element and num != max_element:
#         second_max_element = num
# print("The second largest element in the array is:", second_max_element)
