def Linear_search(L,user=int(input("Enter a number from the given list: "))):
    for ind in range(len(L)):
        if L[ind]==user:
            return ind
    return -1
L=[12,13,14,45,35,15,17,78,98]
print(Linear_search(L))