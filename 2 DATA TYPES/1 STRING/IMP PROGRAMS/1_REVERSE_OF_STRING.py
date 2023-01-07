'''                   REVERSE OF THE GIVEN STRING                                                 '''

s=input("Enter any string : ")
print(s[::-1])                            # * using slice operator

s1 = input("Enter any string to print reverse: ")
print("".join(reversed(s1)))                     # * using join


s = input("Enter some string : ")
i = len(s)-1                                     # *using while
target = ''

while i >= 0:
    target = target+s[i]
    i = i-1
print(target)


