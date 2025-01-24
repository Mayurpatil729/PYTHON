
# Creating a Thread without using any class:

# from threading import * 

# def display(): 
#     for i in range(1,11): 
#         print("Child Thread") 
        
# t=Thread(target=display) #creating Thread object 
# t.start() #starting of Thread 
# for i in range(1,11): 
#     print("Main Thread")

# After t.start() is called, both the main thread and the child thread execute concurrently.
# The exact order of printed lines ("Main Thread" and "Child Thread") can vary because the threads are running in parallel and the operating system's scheduler decides which thread gets to run at any given moment.
# Thread is a pre defined class present in threading module which can be used to create our 
# own Threads.


######################################################################################################


## Creating a Thread by extending Thread class

# We have to create child class for Thread class. In that child class we have to override run() method 
# with our required job. Whenever we call start() method then automatically run() method will be 
# executed and performs our job.

from threading import * 

class MyThread(Thread):
    def run(self): 
        for i in range(10): 
            print("Child Thread-1") 
            
t=MyThread() 
t.start() 

for i in range(10): 
    print("Main Thread-1") 





######################################################################################################


## Creating a Thread without extending Thread class:


from threading import * 
class Test: 
    def display(self): 
        for i in range(10): 
            print("Child Thread-2") 
            
obj=Test() 
t=Thread(target=obj.display) 
t.start() 

for i in range(10): 
    print("Main Thread-2") 

