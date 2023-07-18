


lower=int(input("Enter the lower limit :"))
upper=int(input("Enter the upper limit :"))

sum=0
for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit =temp%10
        sum+=digit**order
        temp//=10
    if num==sum:
        print(num)


# for n in range(1, 500):
#     t = n
#     s = 0
#     while n != 0:
#         r = n % 10
#         s = s+r**3
#         n = n//10
#     if s == t:
#         print(t)











