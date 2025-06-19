import time   
class Test:   
    def __init__(self):   
        print("Object Initialization...")   
    def __del__(self):   
        print("Fulfilling Last Wish and performing clean up activities...")   
        
t1=Test()   
t1=None   
time.sleep(5)   
print("End of application")   

###########################################################################################

import time   
class Test:   
    def __init__(self):   
        print("Constructor Execution...")   
    def __del__(self):   
        print("Destructor Execution...")   

t1=Test()   
t2=t1   
t3=t2   
del t1   
time.sleep(5)   
print("object not yet destroyed after deleting t1")   
del t2   
time.sleep(5)   
print("object not yet destroyed even after deleting t2")   
print("I am trying to delete last reference variable...")   
del t3    


##############################################################################################

import time
class Test:
    def __init__(self):
        print("Constructor Execution.....")
    
    def __del__(self):
        print("Destructor Execution..")
        

l1=[Test(),Test(),Test()]
del l1
time.sleep(5)   
print("End of application")   

###############################################################################################

import sys   
class Test:   
    pass   

t1=Test()   
t2=t1   
t3=t1   
t4=t1   
print(sys.getrefcount(t1))  

################################################################################################
















