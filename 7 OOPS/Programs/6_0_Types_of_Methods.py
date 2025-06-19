class Student:
    collegename="IIT"
    director="H.c verma"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
    def getStudentInfo(self):
        print("Student Name : ",self.name)
        print("Student Rollno:",self.rollno)
        
    @classmethod
    def getCollegeInfo(cls):
        print("College name: ",cls.collegename)
        print("Director Name: ",cls.director)
    
    @staticmethod
    def getAverage(a,b,c):
        return (a+b+c)/3
        
s=Student("Mayur",101)
s.getStudentInfo()
Student.getCollegeInfo()








































