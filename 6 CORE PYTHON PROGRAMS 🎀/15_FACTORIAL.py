
# USING FOR LOOP

n = int(input("Enter any number : "))

factorial = 1
if n < 0:
    print("please enter the valid input")
if n == 0:
    print("Factorial = ", 1)
elif n > 0:
    for i in range(1, n+1):
        factorial = factorial*i
    print("Factorial = ", factorial)

# USING RECURSION

def fact(a):
    if a==0:
        return 1
    else:
        return((a)*fact(a-1))
    
num=int(input("Enter a number here : "))

result=fact(num)
print("The factorial of the given number is ",result)





