f = open("ABC.txt", 'w')
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
print("Is File Closed : ", f.closed)
f.close()
print("Is File Closed : ", f.closed)


f = open("ABCD.txt", 'w')
f.write("python\n")
f.write("LANGUAGE\n")
f = open("ABCD.txt", 'r')
print()

data=f.read()
print(data)

print("Data written to the file successfully")
f.close()


print()
print("append file :")
f=open("abcde.txt",'w')
list=["sunny","bunny","vinny","chinny"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()






