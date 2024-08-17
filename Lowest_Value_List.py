#Wap to find the smaller value in the list.
def Lowest(L):
    minval=L[0]
    for ind in range(1,len(L)):
        if L[ind]<minval:
            minval=L[ind]
    return minval
L=[12,13,14,2,3,465,34,23,45,98]
print(Lowest(L))