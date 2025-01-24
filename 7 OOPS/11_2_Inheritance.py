

class P:
    def __init__(self):
        self.x=10
class C(P):
    def __init__(self):
        super().__init__()
        self.y=20
        # self.x=20
        # print(super().x)
        # print(self.x)
        print(self.__dict__)
        
c=C()





#############################################################################################
class P:
    a=10
    def __init__(self,x):
        self.x=x
        
class C(P):
    pass

c=C(777)
print(c.a)
print(c.x)









