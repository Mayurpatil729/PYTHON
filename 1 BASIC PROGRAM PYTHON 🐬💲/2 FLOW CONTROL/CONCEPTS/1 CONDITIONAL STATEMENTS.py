'''        IF         '''  # switch case is  not available in python but match case is availabel in python

'''
password=input("Enter the password :")

if password=="python" :
    print("password is correct ")
if password == "729":
    print("vip member ")

'''

'''         IF ELSE       '''

'''
name=input("Enter the name :")
if name=="mayur":
    print("hello mayur")
    print('good morning')
else :
    print("who are you ")

'''

'''       IF ELIF             '''

'''
day = int(input("Enter the day number :"))

if day == 1:
    print("\t\n sunday ")
elif day == 2:
    print("\n\t Monday")
elif day == 3:
    print("\n\t Tuesday")
elif day == 4:
    print("\n\t wednesday")
elif day == 5:
    print("\n\t Thursday")
elif day == 6:
    print("\n\t Friday")
elif day == 7:
    print("\n\t Saturday")
else:
    print("\n\t Enter the valid number")

'''

"""            short hand if       """
a = 18
b = 29
if a < b:
    print("a is greater than b")


"""       MATCH CASE                      """

l = int(input("Enter any number ="))

match l:
    case 1:
        print("1")
    case 2:
        print("2")
