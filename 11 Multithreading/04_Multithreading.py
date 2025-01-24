
# Setting and Getting Name of a Thread:

# To get Name:
# t.name
# t.getName()

# To set Name:
# t.name="mayur"
# t.setName("mayur")

from threading import *
print(current_thread().getName())
current_thread().name='mayur'
print(current_thread().getName())
print(current_thread().name())











