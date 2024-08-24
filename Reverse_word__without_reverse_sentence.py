var="change the example"
word=var.split()
result=[]
for word in word:
    rev=""
    for ind in range(len(word)-1,-1,-1):
        rev=rev+word[ind]
    result.append(rev)
print(" ".join(result))