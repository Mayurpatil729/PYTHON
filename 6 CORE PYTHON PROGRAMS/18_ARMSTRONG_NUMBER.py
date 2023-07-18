num = int(input("Enter the any number : "))


back = num
sum = 0

while num != 0:
    rem = num % 10
    num = num//10
    sum = sum+rem*rem*rem


if (back == sum):
    print(f"{back}  is the armstrong number")
else:
    print(f"{num}  is not the armstrong number")


num = int(input("Enter a number here : "))
order = len(str(num))

sum = 0
temp = num


while temp > 0:
    digit = temp % 10
    sum += digit**order
    temp //= 10

if (sum==num):
    print(f"{back}  is the armstrong number")
else:
    print(f"{num}  is not the armstrong number")

# 153
# 370
# 371
# 407
# 
# 1634









