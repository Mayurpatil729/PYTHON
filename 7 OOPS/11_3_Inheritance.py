class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print("Eating and Beer Drinking")
        
        
class SE(Person):
    def __init__(self,name,age,eno,esal):
        self.eno=eno
        self.esal=esal
    def work(self):
        print("Python coding is something like drinking chilled beer")
        

s=SE("Mayur",45,100,1000000)
print(s.name,s.age,s.eno,s.esal)
s.eatndrink()
s.work()


#####################################################################################

class A:
    def m1(self):
        self.x=10
class B(A):
    def m1(self):
        super().m1()
        #self.x=20
    def disp(self):
        print(self.x)
        print(super().x)

b=B()
b.m1()
b.disp()


########################################################################################







































































