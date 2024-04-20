# ##Write a Python program to print the Fibonacci sequence up to n terms.
# ##0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,.
# num = int(input("Enter number"))
# i = 0 
# X = 0
# Y = 1
# while i < num:
#     Z =X+Y
#     print("--",X)
#     X=Y
#     Y=Z
#     i+=1
    
######USING for loop
# num = int(input("Enter number"))
# A = 0
# B = 1
# for i in range(num):
#     Temp = A + B
#     print(A)
#     A = B
#     B = Temp



def fib(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c = a+b
            a=b
            b=c
            print(c)
fib(5)