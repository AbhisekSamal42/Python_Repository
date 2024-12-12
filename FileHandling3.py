# Ways of closing file:-
   #(i)Normal way example:-

f=open("data.txt",mode='r')
f.close()

   #(ii)Using Exception handling:-

try:
    f=open("data.txt",mode='r')
finally:
    f.close()

   #(iii)With statement:-

with open("data.txt",mode='r') as f:
    data=f.read
    print(data)