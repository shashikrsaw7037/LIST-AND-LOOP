# Write a Python program to find the maximum of two numbers.
a = int(input("Enter first number:\n"))
b = int(input("Enter second number:\n"))
if(a>b and b<a):
    print(a,": First no. is greater")
elif(a<b and b>a):
    print(b,": Second no. is greater")

