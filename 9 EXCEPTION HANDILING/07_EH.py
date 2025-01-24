f=None
try:
    f=open("abc.txt",'r')
except:
    print("Some problem while locating and opening the file")
else:
    print("file opened successfully")
    print("The data present in the file is : ")
    print("#"*30)
    print(f.read())
finally:
    if f is not None:
        f.close()











