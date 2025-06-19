# class Test:
#     @classmethod
#     def m1(cls):
#         print(id(cls))

#     @classmethod
#     def m2(cls):
#         print(id(cls))

# print(id(Test))
# Test.m1()
# Test.m2()


class Test:
    def __init__(self):
        self.a = 10  # instance variable
        self.b = 20  # instance variable
        self.c = 30
        self.d = 40

    def m1(self):
        self.c = 30  # instance variable


t1 = Test()
t1.m1()
t1.d = 40  # instance variable
t1.e = 50  # instance variable
t2 = Test()
t2.f = 40

print(t1.__dict__)
del t1.d,t1.e
print(t1.__dict__)

print(t2.__dict__)
