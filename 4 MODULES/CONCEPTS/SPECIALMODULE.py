
def f1():
    if __name__ == "__main__":
        print("The code is executed directly as a program")
        print("The value of name : ", __name__)
    else:
        print("The code is exectued indirectly")
        print("The value of name : ", __name__)


f1()


# a special variable __name__ will be added internally.
# This variable stores information regarding whether the program is executed as an
# individual program or as a module.

# If the program executed as an individual program then the value of this variable is
# __main__
# If the program executed as a module from some other program then the value of this
# variable is the name of module where it is defined.

# Hence by using this __name__ variable we can identify whether the program executed
# directly or as a module


































