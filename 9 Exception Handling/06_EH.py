class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg=msg
        
class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg

age=int(input("Enter Age : "))
if age>60:
    raise TooYoungException("Your age already crossed marriage age, no chance of getting marriage")
elif age<18:
    raise TooOldException("Please wait some more time, definitely you will get best match ")







