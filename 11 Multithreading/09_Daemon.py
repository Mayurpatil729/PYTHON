from threading import * 
import time 
def job(): 
    for i in range(10): 
        print("Lazy Thread") 
        time.sleep(2) 

t=Thread(target=job) 
#t.setDaemon(True)===>Line-1 
t.start() 
time.sleep(5) 
print("End Of Main Thread")








