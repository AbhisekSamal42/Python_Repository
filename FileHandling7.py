# Writing data in to a file:-
 #'w' mode:-

  #Write():-
#example1:-
f=open('data.txt',mode='w')
data=f.write("hello world")
print(data)
f.close()

#example2:-
f=open('data.txt',mode='w')
data=f.write("hello \n world")
print(data)
f.close()


  #writelines():-

f=open('data.txt',mode='w')
lists=['India','is','our','country']
f.writelines(lists)
f.close()