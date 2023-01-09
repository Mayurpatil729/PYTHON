
num = int(input("Enter the number : "))

if num <= 0:
    print("please enter the valid input")
else:
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count = count+1
        i = i+1
    if (count == 2):
        print("Given number is Prime number ")
    else:
        print("Given number is not a prime number")


# def isprime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#         return True


# x = int(input('Enter number'))
# if isprime(x):
#     print("The", x, "is prime number")
# else:
#     print("The", x, "is not prime number")


# n = eval(input("Enter the number : "))
# if n <= 1:
#     print("it is not a prime number")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("It is not a prime number")
#             break
#     else:
#         print("It is a prime number")
            
            
            
            
            
            
            
            
            
            
