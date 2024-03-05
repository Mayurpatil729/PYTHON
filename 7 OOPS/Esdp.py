# # Bank Account
# class BankAccount:
#     def __init__(self, name, account_number, balance=0):
#         self.name = name
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Amount {amount} deposited successfully.")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Amount {amount} withdrawn successfully.")
#         else:
#             print("Insufficient balance. Withdrawal not allowed.")

#     def display_info(self):
#         print(f"Depositor Name: {self.name}")
#         print(f"Account Number: {self.account_number}")
#         print(f"Balance: {self.balance}")


# # Example usage
# account = BankAccount(name="Mayur Patil",
#                       account_number="123456", balance=1000)

# account.display_info()

# account.deposit(500)
# account.display_info()

# account.withdraw(200)
# account.display_info()

# account.withdraw(1500)
# account.display_info()



=========================================================================================================




# class Student:
#     def __init__(self, name, roll_no, address, percentage):
#         self.name = name
#         self.roll_no = roll_no
#         self.address = address
#         self.percentage = percentage
#         self.grade = self.calculate_grade()

#     def calculate_grade(self):
#         if self.percentage >= 70:
#             return "Distinction"
#         elif self.percentage >= 60:
#             return "First Class"
#         elif self.percentage >= 40:
#             return "Second Class"
#         else:
#             return "Fail"

#     def display_info(self):
#         print("Student Information:")
#         print(f"Name: {self.name}")
#         print(f"Roll No: {self.roll_no}")
#         print(f"Address: {self.address}")
#         print(f"Percentage: {self.percentage}%")
#         print(f"Grade: {self.grade}")


# # Example usage
# name = input("Enter student name: ")
# roll_no = input("Enter roll number: ")
# address = input("Enter address: ")
# percentage = float(input("Enter percentage: "))

# student = Student(name, roll_no, address, percentage)
# student.display_info()


=================================================================================================================================

# class Student:
#     def __init__(self, roll_no, name):
#         self.roll_no = roll_no
#         self.name = name
#         self.voted = False  # Indicates whether the student has voted or not

#     def display_details(self):
#         print(f"Student Roll No: {self.roll_no}")
#         print(f"Student Name: {self.name}")

#     def vote(self):
#         if not self.voted:
#             print("Vote successfully cast for the college president!")
#             self.voted = True
#             return True
#         else:
#             print("You have already voted. Multiple votes are not allowed.")
#             return False




# class PresidentNominee:
#     def __init__(self, name):
#         self.name = name
#         self.vote_count = 0  # Count of votes received by the nominee


# def main():
#     # Dictionary to store student information (roll_no: Student object)
#     students = {}
#     # Dictionary to store president nominees (name: PresidentNominee object)
#     nominees = {}

#     while True:
#         print("\nCollege President Voting Program")
#         print("1. Student Registration")
#         print("2. Student Login")
#         print("3. Update Details")
#         print("4. Voting")
#         print("5. Logout")
#         print("6. Admin Login")
#         print("7. Exit")
#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             roll_no = input("Enter your roll number: ")
#             name = input("Enter your name: ")
#             students[roll_no] = Student(roll_no, name)
#             print("Student registered successfully.")

#         elif choice == 2:
#             roll_no = input("Enter your roll number: ")
#             if roll_no in students:
#                 students[roll_no].display_details()
#             else:
#                 print("Student not found. Please register first.")

#         elif choice == 3:
#             roll_no = input("Enter your roll number: ")
#             if roll_no in students:
#                 name = input("Enter your updated name: ")
#                 students[roll_no].name = name
#                 print("Details updated successfully.")
#             else:
#                 print("Student not found. Please register first.")

#         elif choice == 4:
#             roll_no = input("Enter your roll number: ")
#             if roll_no in students:
#                 student = students[roll_no]
#                 if not student.voted:
#                     print("President Nominees:")
#                     for nominee in nominees.values():
#                         print(nominee.name)

#                     vote_choice = input(
#                         "Enter the name of the nominee you want to vote for: ")
#                     if vote_choice in nominees:
#                         nominee = nominees[vote_choice]
#                         nominee.vote_count += 1
#                         if student.vote():
#                             print("Thank you for voting!")
#                     else:
#                         print("Invalid nominee name.")
#                 else:
#                     print("You have already voted. Multiple votes are not allowed.")
#             else:
#                 print("Student not found. Please register first.")

#         elif choice == 5:
#             print("Logout successful.")

#         elif choice == 6:
#             print("\nAdmin Login")
#             admin_password = "admin123"  # Change this to a more secure password
#             password = input("Enter the admin password: ")
#             if password == admin_password:
#                 while True:
#                     print("\nAdmin Menu")
#                     print("1. Add President Nominee")
#                     print("2. Update President Nominee")
#                     print("3. Remove President Nominee")
#                     print("4. View Voting Details")
#                     print("5. Logout")
#                     admin_choice = int(input("Enter your choice: "))

#                     if admin_choice == 1:
#                         nominee_name = input("Enter the name of the nominee: ")
#                         nominees[nominee_name] = PresidentNominee(nominee_name)
#                         print("President nominee added successfully.")

#                     elif admin_choice == 2:
#                         print("President Nominees:")
#                         for nominee in nominees.values():
#                             print(nominee.name)

#                         nominee_name = input(
#                             "Enter the name of the nominee to update: ")
#                         if nominee_name in nominees:
#                             updated_name = input(
#                                 "Enter the updated name for the nominee: ")
#                             nominees[nominee_name].name = updated_name
#                             print("President nominee updated successfully.")
#                         else:
#                             print("Invalid nominee name.")

#                     elif admin_choice == 3:
#                         print("President Nominees:")
#                         for nominee in nominees.values():
#                             print(nominee.name)

#                         nominee_name = input(
#                             "Enter the name of the nominee to remove: ")
#                         if nominee_name in nominees:
#                             del nominees[nominee_name]
#                             print("President nominee removed successfully.")
#                         else:
#                             print("Invalid nominee name.")

#                     elif admin_choice == 4:
#                         print("Voting Details:")
#                         for nominee in nominees.values():
#                             print(f"{nominee.name}: {nominee.vote_count} votes")

#                     elif admin_choice == 5:
#                         print("Admin logout successful.")
#                         break


















