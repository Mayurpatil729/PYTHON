class Test:
    def __init__(self):
        print("Address of object refered by self:",id(self))
        
t=Test()
print("Address of object referd by t: ",id(t))

print()
t1=Test()
print("Address of object referd by t1 : ",id(t1))





