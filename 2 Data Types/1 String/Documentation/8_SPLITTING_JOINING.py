#SPLITTING OF STRING
s = "Everything is connected"

l = s.split('n')
p = s.split()
print(type(l))
for x in l:
    print(x)



#JOINING OF STRING
print('\n\t joining of string')

#tuple
t=('mango','banana','apple')
s='+'.join(t)
print(s)

#list
l=['hyderabad','singapore','london','dubai']
s=':'.join(l)
print(s)


print()

str1="Mayur , patil "
rev_wrd=" ".join(str1.split()[::-1])
print(rev_wrd)