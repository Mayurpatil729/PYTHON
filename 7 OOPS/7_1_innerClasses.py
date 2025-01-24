class Person:
    def __init__(self):
        print("Person class Constrctor")
        self.name="Mayur"
        self.db=self.Dob()
    def display(self):
        print("Name: ",self.name)
    class Dob:
        def __init_(self):
            print("Dob Class Constructor")
            self.dd=28
            self.mm=5
            self.yy=1947
        def display(self):
            print("Dob={}/{}/{}".format(self.dd,self.mm,self.yy))

#########################################
p=Person()   
p.display()   
x=p.db   
x.display()  
############################################


class Human:
    def __init__(self):  
        self.name="sunny"
        self.head=self.Head()
        self.brain=self.Brain()
    def display(self):
        print("Hello",self.name)
        
    class Head:
        def talk(self):
            print("Talking....")
            
    class Brain:
        def think(self):
            print("Thinking.......")
        
h=Human()
h.display()
h.head.talk()









