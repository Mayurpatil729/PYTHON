from threading import *
mt=current_thread()
print(mt.isDaemon())
print(mt.daemon)

#################################################

# The threads which are running in the background are called Daemon Threads.
# The main objective of Daemon Threads is to provide support for Non Daemon Threads( like main 
# thread)
# Eg: Garbage Collector

#################################################

# We can change Daemon nature by using setDaemon() method of Thread class.
# t.setDaemon(True)
# t.setDaemon(False)

# once thread started we cannot change its Daemon nature

#################################################


from threading import *
def job():
    print("Executed by child thread : ")
    
t=Thread(target=job)
print(t.isDaemon())
t.setDaemon(True)
print(t.isDaemon())

# Default Nature:
# By default Main Thread is always non-daemon.But for the remaining threads Daemon nature will 
# be inherited from parent to child.i.e if the Parent Thread is Daemon then child thread is also 
# Daemon and if the Parent Thread is Non Daemon then ChildThread is also Non Daemon.

#################################################


from threading import *
import time
def job1():
    print('executed by t1 : ')
    t2=Thread(target=job2)
    print("t2 is Daemon : ",t2.isDaemon())
    t2.start()

def job2():
    print("Executed by t2 : ")

t1=Thread(target=job1)
t1.setDaemon(True)
print("t1 is Daemon : ",t1.is_Daemon())
t1.start()
# time.sleep(10)


#################################################


