class Employee:
    name = ""
    dep = ""
    salary = 0

    def setdata(self):
        self.name = input("Enter Name:\t")
        self.dep = input("Enter Department:\t")
        self.salary = int(input("Enter Salary:\t"))

    def showdata(self):
        print("Name\t:", self.name)
        print("Department\t:", self.dep)
        print("Salary\t:", self.salary)
emp=Employee()
emp.setdata()
emp.showdata()