"""      TUPLE PACKING AND UNPACKING :           """

a = 10
b = 20
c = 30
d = 40
t = a, b, c, d
print(t) #* Here a, b, c, d are packed into a tuple t. This is nothing but tuple packing

#Tuple unpacking is the reverse process of tuple packing
#We can unpack a tuple and assign its values to different variable
print()
t=(10,20,30,40,50)
a,b,c,d,e=t
print("a=",a,"b=",b,"c=",c,"d=",d,"e=",e)


#Note: At the time of tuple unpacking the number of variables and number of values
#should be same., otherwise we will get ValueError.

'''                   TUPLE COMPREHENSION                   '''

#! NOT SUPPORTED

T=(x**3 for x in range(1,7))
print(type(T))
for x in T:
    print(x)