# Write a Python program to check if a number is prime.

n = int(input("Enter Number:\n"))

if n <2:
    print("It is not prime no")
else:
    for i in range(2,n):
        if n%i==0:
            print("It is not prime no")
            break
    else:
        print("It is prime no")


