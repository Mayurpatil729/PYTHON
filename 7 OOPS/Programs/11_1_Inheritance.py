# How we can use members of one class inside another class:
# 1. By using Composition (Has-A Relationship)
# 2. By using Inheritance(IS-A Relationship)


######################################################################################


# 1. By using Composition(Has-A Relationship) :
# class Car:
# class Engine:
# class Car Has-A Engine Reference Code Reusability

# class Employee:
# c=Car()
# class Car:
# c ass Employee Has-A Car


########################################################################################
# Has Relationship Code







####################################################################################
# Inheritance Code
class X:
    a=10
    def m1(self):
        print("Parent class instance method")
    
    @classmethod
    def m2(cls):
        print("Parent class class method")
    
    @staticmethod
    def m3():
        print("Parent class static method")
        
class Y(X):
    pass

y=Y()
print(y.a)
y.m1()
y.m2()
y.m3()

#############################################################################################


# class X:
#     def m1():
#     def m2():
#     def m3():
#     def m4():
        
# class Y(X):
#     x=X()
#     x.m1()
#     x.m2()
#     x.m3()
#     x.m4()
# class Y has-a X Reference


# y=Y()
# y.m1()
# y.m2()
# y.m3()

# class Y(X):
# class childclass(parentclass):
#     class c extends p



#############################################################################################################













