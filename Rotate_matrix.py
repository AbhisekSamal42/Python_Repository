#Rotate the matrix 90.
mat=[[12,13],[43,54]]
result=[]
for row in range(len(mat)):
    line=[]
    for col in range(len(mat)-1,-1,-1):
        line.append(mat[col][row])
    result.append(line)
print(result)