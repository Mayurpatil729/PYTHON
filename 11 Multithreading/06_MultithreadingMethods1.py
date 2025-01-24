# active_count():
# This function returns the number of active threads currently running.

from threading import * 
import time 
def display(): 
    print(current_thread().getName(),"...started") 
    time.sleep(3) 
    print(current_thread().getName(),"...ended") 

print("The Number of active Threads:",active_count()) 
t1=Thread(target=display,name="ChildThread1") 
t2=Thread(target=display,name="ChildThread2") 
t3=Thread(target=display,name="ChildThread3") 
t1.start() 
t2.start() 
t3.start() 
print("The Number of active Threads:",active_count()) 
time.sleep(5) 
print("The Number of active Threads:",active_count()) 


################################################################################ 


# enumerate() function:
# This function returns a list of all active threads currently running.

from threading import * 
import time 
def display(): 
    print(current_thread().getName(),"...started") 
    time.sleep(3) 
    print(current_thread().getName(),"...ended") 

t1=Thread(target=display,name="ChildThread1") 
t2=Thread(target=display,name="ChildThread2") 
t3=Thread(target=display,name="ChildThread3") 
t1.start() 
t2.start() 
t3.start() 

l=enumerate() 
for t in l: 
    print("Thread Name:",t.name) 
    print("Thread Identification Number : ",t.ident)
    print()


time.sleep(10) 
l=enumerate() 
for t in l: 
    print("Thread Name:",t.name)
    print("Thread Identification Number : ",t.ident)
    print()




################################################################################ 

# isAlive():
# isAlive() method checks whether a thread is still executing or not.

from threading import * 
import time 
def display(): 
    print(current_thread().getName(),"...started") 
    time.sleep(3) 
    print(current_thread().getName(),"...ended") 
    
t1=Thread(target=display,name="ChildThread1") 
t2=Thread(target=display,name="ChildThread2") 
t1.start() 
t2.start() 

print(t1.name,"is Alive :",t1.isAlive()) 
print(t2.name,"is Alive :",t2.isAlive()) 
time.sleep(10) 
print(t1.name,"is Alive :",t1.isAlive()) 
print(t2.name,"is Alive :",t2.isAlive()) 


















