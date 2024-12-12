# How to Open  and close a file:-

f=open("data.txt",mode='r')
if f:
    print("File open Successfully opened.")
f.close()


# File object Variable example:-

f=open("data.txt",mode='r',encoding='utf-8')
print("File name is :",f.name)
print("Encoding is :",f.encoding)
print("Mode is :",f.mode)
print("Is file closed :",f.closed)
f.close()
print("Is file closed :",f.closed)


# File object Method example:-
   #example:-1

f=open("data.txt",mode='r')
print(f.readable())
print(f.writable())
f.close()
    
  #example:-2

f=open("data.txt",mode='w')
print(f.readable())
print(f.writable())
f.close()
  
  #example:-3

f=open("data.txt",mode='w+')
if f.readable():
    print("File is readable.")
f.close()