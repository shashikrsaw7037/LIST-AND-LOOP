# Write a Python program to find the largest element in an array.
from array import *
arr =array('i', [101, 107, 2017, 1098, 7832, 763467, 213486, 76312867])
arr1 =sorted(arr)
print(arr1)
print("the largest element in an array :",arr1[-1])

# from array import *
# arr = array('i', [101, 107, 2017, 1098, 7832, 763467, 213486, 76312867])
# max_element = arr[0]
# print(max_element)
# for num in arr:                                      /////CHATGPT
#     if num > max_element:
#         max_element = num
# print("The largest element in the array is:", max_element)

