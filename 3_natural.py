# Write a Python program to find the sum of natural numbers up to n using a while loop.
n= int(input("Enter number:\n"))
sum =  0
i = 1
while i<=n:
    print("Natural number",i)
    sum +=i
    i+=1
print("Sum of natural number",sum)