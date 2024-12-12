# Reading data from file:-
    
    #(i)read():-

f=open("data.txt",mode='r')
data=f.read()
print(data)
f.close()

   #(ii)readline():-

f=open("data.txt",mode='r')
data=f.readline()
print(data)
f.close()

   #(iii)readlines():-

f=open("data.txt",mode='r')
data=f.readlines()
print(data)
f.close()


# Reading a file using for loop:-

with open("data.txt", mode='r') as f:
    for line in f:
        print(line, end='')  # Print each line without adding an extra newline
