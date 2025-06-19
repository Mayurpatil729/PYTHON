# We can declare a method with same class name .

class Test:
    def Test(self):
        print("A special method...")


t = Test()  # __init__() with be executed
t.Test()  # method will be executed
