#Wap to find highest value in the list.
def Highest(L):
    maxval=L[0]
    for ind in range(1,len(L)):
        if L[ind]>maxval:
            maxval=L[ind]
    return maxval
L=[12,19,13,14,15,45,63,400]
print(Highest(L))