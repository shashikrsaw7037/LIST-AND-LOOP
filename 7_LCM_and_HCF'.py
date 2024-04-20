##### Write a Python program to find the LCM of two numbers.


a = int(input("Enter first Number :\n"))#6
b = int(input("Enter second number :\n"))#8
maxNum = max(a,b)#8

while True:
    if(maxNum%a==0 and maxNum%b==0):#24%6==0 and 24%8==0
       break
    maxNum = maxNum + 1
print(f"The LCM of {a} and {b} is {maxNum}")







##### Write a Python program to find the HCF of two numbers.
num1 = int(input("Enter first Number :\n"))
num2 = int(input("Enter second number :\n"))

# minNum = min(num1,num2)
if num2>num1:
    minNum = num1
else:
    minNum = num2
    
for i in range(1,minNum+1):
    if num1%i==0 and num2%i==0:
        hcf = i
print(f"The HCF/GCD of two numbers is {hcf}")