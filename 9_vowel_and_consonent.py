# Write a Python program to count the number of vowels and consonants in a string.
# n = input("Enter a sentence:\n")

# count = 0

# for i in n:
#     # if i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U':
#     if i in 'aeiouAEIOU':
#         c=count+1 
#         print(c)
# else: 
#     print("Vowel is not there")
    
    
    
    
    
# n = input("Enter a sentence:\n")
# count = 0
# for i in n:
#     if i in 'aeiouAEIOU':
#         count += 1 
# if count > 0:
#     print("Number of vowels:", count)
# else:
#     print("Vowel is not there")
    
    
    
    



n = input("Enter a sentence:\n")

vowels = 0
consonants = 0

for i in n:
    if i in 'aeiouAEIOU':
        vowels += 1
    elif i.isalpha():
        consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)

