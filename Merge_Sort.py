def Merge(Mlist,Llist,Rlist):
    mind,lind,rind=0,0,0
    while lind<len(Llist) and rind<len(Rlist):
        if Llist[lind]>Rlist[rind]:
            Mlist[mind]=Rlist[rind]
            rind=rind+1
        else:
            Mlist[mind]=Llist[lind]
            lind=lind+1
        mind=mind+1
    while lind<len(Llist):
        Mlist[mind]=Llist[lind]
        mind=mind+1
        lind=lind+1
    while rind<len(Rlist):
        Mlist[mind]=Rlist[rind]
        mind=mind+1
        rind=rind+1
def Divide(L):
    if len(L)>1:
        left,right=L[:len(L)//2],L[len(L)//2:]
        Divide(left)
        Divide(right)
        Merge(L,left,right)
L=[11,44,99,23,99,12,11,0]
Divide(L)
print(L)