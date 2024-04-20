# Write a Python program to find the factorial of a number using recursion.
n= int(input("Enter number:\n"))
sum =  1
i = 1
while i<=n:
    print("number",i)
    sum *=i
    i+=1
print("Factorial of number",sum)