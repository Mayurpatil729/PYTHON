
############################################
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


############################################################################

#Student Details
student_1=['Madhav',10]  # Name, Grade
student_2=['Vishakha',12]
student_3='keshav'

student_1.append('A')

print(f'{student_1[0]} is in class {student_2[1]}' )

### Using OOPs - Creating Student Records

# Class - blueprint or template
class Student :
    name='Madhav'
    grade=10
    # pass

# object - instance of class
student1= Student()
print(student1.name,student1.grade)















