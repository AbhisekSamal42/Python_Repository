#Create a 3*5 matrix.

rows=3
column=5
mat=[]
for row in range(rows):
    line=[]
    for col in range(column):
        line.append(int(input("Enter the value: ")))
    mat.append(line)
print(mat)

#Using list comprehension method create 3*5 matrix.

rows=int(input("Enter number of rows: "))
columns=int(input("Enter number of columns: "))
print([[int(input("Enter values: ")) for col in range(columns)]for row in range(rows)])