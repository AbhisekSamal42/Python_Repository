# tell():-

f=open("data.txt",mode='r')
print(f.tell())
data=f.read(3)
print(f.tell())
print(data)
f.close()

#seek():-

f = open("data.txt", mode='r')  
print(f.tell())  
data = f.read(3)  
print(data)  
print(f.seek(0)) 
print(f.read()) 
f.close()  
