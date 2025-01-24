
# join() method:
# If a thread wants to wait until completing some other thread then we should go for join() method.

from threading import * 
import time 
def display(): 
    for i in range(10): 
        print("Seetha Thread") 
        time.sleep(2) 

t=Thread(target=display) 
t.start() 
t.join()#This Line executed by Main Thread 

for i in range(10): 
    print("Rama Thread")


# Note: We can call join() method with time period also.
# t.join(seconds)
# In this case thread will wait only specified amount of time.

##############################################################################

from threading import * 
import time 
def display(): 
    for i in range(10): 
        print("Seetha Thread") 
        time.sleep(2)

t=Thread(target=display) 
t.start() 
t.join(5)#This Line executed by Main Thread 
for i in range(10): 
    print("Rama Thread") 



















