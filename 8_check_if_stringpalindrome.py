# Write a Python program to check if a string is a palindrome.
n  = (input("Enter the number:\n"))
rev = n[::-1]
print("Rverse string is :",rev)
if n == rev:
    print("It is palindrome string")
else:
    print("It is not palindrome string")