var="I am proud to be an Indian"
word=var.split()
ans=[]
for ind in range(len(word)-1,-1,-1):
    ans.append(word[ind])
print(" ".join(ans))