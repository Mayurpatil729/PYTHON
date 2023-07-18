class Test:
    def __init__(self):
        print("Constructor",id(self))

    def m1(self, x):
        print("Method")


t = Test()  # Default constructor will be executed which is provided by PVM
t.__init__()
t.__init__()
t.__init__()
t.__init__()

print()
print()

print(id(t))
t.m1(10)
