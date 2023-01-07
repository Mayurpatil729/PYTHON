'''       ACCESS CHARACTERS BY USING OPERATORS                     '''
'''
# 1 ]  BY USING INDEX

s = "Engineers"

# postive index
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[6])
print(s[7])
print(s[8])
# print(s[9])          #index error out of range


# negative index
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])
print(s[-7])
print(s[-8])
print(s[-9])


s = input("Enter any string : ")
i = 0
for x in s:
    print("The character present at positive index {} and at negative index is {} is {} " .format(
        i, i-len(s), x))
    i = i+1

'''
# 2 ]  BY  USING SLICE OPERATOR

print("SLICE OPERATOR")

s = "learning python is very very easy "

# print(s[1:7:0])
# slice step cannot be 0

print(s[::])


print(s[1:7:1])  # 1 forward direction,

print(s[1:7:2])

print(s[1:7:-1])  # -1 backward direcition , 1 to 7 there is no 7 in backdirection

print(s[1:7:-2])


# forward direction
# begin =0
# end= len of string
#step =1
print("Forward direction")

print(s[:6:1])
print(s[3:0:1])  # if end is 0 then result is always empty
print(s[0:1:])

# backward directions
# begin=-1
# end=-(len of string+1)

print("Backward direction")

print(s[:0:-1])
print(s[2:-1:-1])  # iƒ end is -1 then result is always empty
