'''                   FUNCTIONS                                   '''

#! len()  :
print()
t = (10, 203, 30, 40)
print(len(t))

#! count():
print()
t = (10, 20, 20, 10, 30, 30, 40, 50)
print(t.count(20))


#! index():
print()
t = (10, 20, 30, 40, 50, 60)
print(t.index(30))
print(t.index(40))
# print(t.index(100)) # valueerror

#! sorted():
print()
t = (20, 50, 80, 10., 30, 40, 80)
t1 = sorted(t)
print(t)
print(t1)  # * list[]
t2 = sorted(t, reverse=True)
print(t2)

#! min() and max() funciton :
print()
t = 10, 20, 30, 450, 80, 90, -9
print(type(t))
print(max(t))
print(min(t))


#! cmp():
print()
t1=(10,20,30)
t2=(40,50,60)
t3=(10,20,30)
#print(cmp(t1,t2)) only in python 2 it is availabe
#print(cmp(t1,t3))


#!


'''            Mathematical operators for tuple               '''
#! Concatenation Operator(+)
print()
t1 = (10, 20, 30)
t2 = (70, 80, 90)
t = t1+t2
print(t)


#! Multiplication operator or repetition operator(*
print()
t = (10, 20, 30)
t2 = t*3
print(t2)
