#Wap to calculate square of number by using map function.

'''def square(a):
    return a*a
l=[12,13,14,16,17]
print(list(map(square,l)))'''



  # (OR) we can do square of nuber by using for loop.



def square(a):
    return a*a
l=[12,13,14,16,17]
for ele in map(square,l):
    print(ele)