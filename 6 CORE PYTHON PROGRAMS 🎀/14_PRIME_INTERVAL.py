
# num = int(input("Enter the number : "))

# if num <= 0:
#     print("please enter the valid input")
# else:
#     i = 1
#     count = 0
#     while i <= num:
#         if num % i == 0:
#             count = count+1
#         i = i+1
#     if (count == 2):
#         print("Given number is Prime number ")
#     else:
#         print("Given number is not a prime number")


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


s = eval(input("Enter the starting number : "))
e = eval(input("Enter the ending number : "))

num=0
if s <= 1:
    print("it is not a prime number")
else:
    for num in range(s, e+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
