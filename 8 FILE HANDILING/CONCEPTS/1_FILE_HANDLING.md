⟫⇛               FILE HANDLING         ⇚⟪
we have to store our data permanently for future purpose.
For this requirement we should go for files.

Types of Files:

1. Text Files: abc.txt ==> to store characters
2. binary files : e binary data like images,video files, audio files etc


==> OPENING FILE:
f = open(filename, mode)
Modes : 
r -->  open an existing file for read operation.
w --> open an existing file for write operation.
a --> open an existing file for append operation

r+ --> To read and write data into the file.
w+  -> To write and read data. It will override existing data.
a+ -->  To append and read data from the file.It wont override existing data.

x --> To open a file in exclusive creation mode for write operation

==> CLOSING FILE:
f.close()

name --> Name of opened file
mode --> Mode in which the file is opened
closed --> Returns boolean value indicates that file is closed or not
readable() --> Retruns boolean value indicates that whether file is readable or not
writable() --> Returns boolean value indicates that whether file is writable or not.


Writing data to text files:==>

write(str)
writelines(list of lines)


f=open("ABCD.txt",'w')
f.write("python\n") 
f.write("LANGUAGE\n") 
print("Data written to the file successfully")
f.close()

==>Reading Character Data from text files:

read()--> To read total data from the file
read(n) --> To read 'n' characters from the file
readline()--> To read only one line
readlines()-->To read all lines into a list

f=open("abc.txt",'r') 
data=f.read() 
print(data) 
f.close()






















