def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


x = int(input('Enter number'))
if isprime(x):
    print("The", x, "is prime number")
else:
    print("The", x, "is not prime number")