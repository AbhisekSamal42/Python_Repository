#create one list and give the input at run time.
size=int(input("Enter the length of list: "))
l=[]
for num in range(size):
    val=int(input("Enter elements: "))
    l.append(val)
print(l)


#create one list and give the input at run time by using list comprehension method.
size=int(input("Enter the length of list: "))
print([int(input("Enter the elements: ")) for ele in range(size)])