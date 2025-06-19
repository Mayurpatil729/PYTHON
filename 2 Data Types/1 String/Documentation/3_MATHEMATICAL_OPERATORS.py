'''                Mathematical operators                   '''
s=' Engineers '



# string concatenation
print("python"+" "+"language")      # both argument should be string


#string * for repetition
print("python"*3)           # one argument should be int 



# len()

print(len(s))


# to acces each character in f/b direction
s="learning python is very easy "
n=len(s)
i=0
print("\nForward direction")
while i<n:
    print(s[i],end="")
    i+=1
print("\nBackward direction")
i=-1
while i>=-n:
    print(s[i],end='')
    i=i-1
    


#alternative ways  :
s = "Learning Python is very easy !!!"
print("\nForward direction")
for i in s:
    print(i, end=' ')

print("\nForward direction")
for i in s[::]:
    print(i, end=' ')

print("\nBackward direction")
for i in s[::-1]:
     print(i, end=' ')
