# Copy content of one file in to another file using python.

f1=open("data.txt",mode='r',encoding='utf-8')
f2=open("data1.txt",mode='w',encoding='utf-8')

data=f1.readlines()
for line in data:
    f2.write(line)
f1.close()
f2.close()