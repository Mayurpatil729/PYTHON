import time
from imp import reload
import module2
# import lib
print("program entering into the sleeping state")
time.sleep(10)
reload(module2)
print("program entering into the sleeping state")
time.sleep(10)
reload(module2)
print("This is last line of program")
