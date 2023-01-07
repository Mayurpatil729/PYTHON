Bytes = eval(input("ENTER THE BYTES TO CONVERT"))
mb = Bytes//1024*1024
gb = Bytes//(1024*1024*1024)
tb = Bytes//(1024*1024*1024*1024)
print("bytes to mb = ", mb)
print("bytes to gb = ", gb)
print("bytes to tb = ", tb)