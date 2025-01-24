class Student1:
    def __init__(self):  # Constructor
        # print("Constructor Execution....")
        self.name = "Charlie"
        self.rollno = 729
        self.marks = 85

    def talk(self):
        print("Hello I am ", self.name)
        print("My Roll no is : ", self.rollno)
        print("My Marks are: ", self.marks)


s1 = Student1()
print('Student1:', s1.name, s1.rollno, s1.marks)
print('Address of s1:', id(s1))
s2 = Student1()
print('Student2:', s2.name, s2.rollno, s2.marks)
print("Address of s2: ", id(s2))


print()


class Student1:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def talk(self):
        print("Hello I am ", self.name)
        print("My Roll no is : ", self.rollno)
        print("My Marks are: ", self.marks)


s1 = Student1('sunny', 101, 90)
print('Student1:', s1.name, s1.rollno, s1.marks)
print('Address of s1:', id(s1))
s2 = Student1('bunny', 102, 98)
print('Student2:', s2.name, s2.rollno, s2.marks)
print("Address of s2: ", id(s2))

############################################


class Student:
    def __init__(self,name,grade): #__init__method-Constructor, Value initialize -fix
    #self parameter-reference or connection build btw class and object - fix
        self.name=name
        self.grade=grade    
        
        
        
        
        
        
student1=Student()
print(student1.name,student1.grade)

student2=Student()
print(student2.name,student2.grade)
















