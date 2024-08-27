#Add two matrix .
mat1=[[1,2],[3,4]]
mat2=[[4,5],[6,7]]
if len(mat1)==len(mat2) and len(mat1[0])==len(mat2[0]):
    result=[]
    for rows in range(len(mat1)):
        line=[]
        for col in range(len(mat1[0])):
            line.append(mat1[rows][col]+mat2[rows][col])
        result.append(line)
    print(result)
else:
    print("Addition not possible")



