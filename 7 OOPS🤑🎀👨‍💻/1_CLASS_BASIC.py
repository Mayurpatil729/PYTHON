# Basic

class Student:
    '''Look like an angel'''
    # variables(properties) like name, marks, rollno
    # Methods(actions / behaviour) like read, write, eat, sleep, talk


print(Student.__doc__)
print(Student.__dict__)
print(Student.__weakref__)
help(Student)


class Student1:
    def __init__(self):  # Constructor
        print("Constructor Execution....")
        self.name = "Charlie"
        self.rollno = 729
        self.marks = 85

    def talk(self):
        print("Hello I am ", self.name)
        print("My Roll no is : ", self.rollno)
        print("My Marks are: ", self.marks)


s1 = Student1()
print(s1.name)
print(s1.rollno)
print(s1.marks)
s1.talk()


s2 = Student1()
print(s2.name)
print(s2.rollno)
print(s2.marks)


print(id(s1))
print(id(s2))
