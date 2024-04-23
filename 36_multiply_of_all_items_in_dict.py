# Write a Python program to multiply all the items in a dictionary.
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
mul = 1
for i in my_dict.values():
    mul*=i
print("Mutiply all the items in a dictionary",mul)