def Quick(L):
    if len(L)<=1:
        return L
    pivot=L[0]
    low=[L[ind] for ind in range(1,len(L)) if pivot> L[ind]]
    high=[L[ind] for ind in range(1,len(L)) if pivot<=L[ind]]
    return Quick(low)+[pivot]+Quick(high)
var=[17,12,-13,34,54,65,78,98]
print(Quick(var))