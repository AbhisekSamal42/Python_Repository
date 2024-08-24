#i/p is var ="aaabbcccccddd"
#o/p is 3a2b5c3d

var="aaabbcccccddd"
var=var+" "
res=""
count=1
for ind in range(len(var)-1):
    if var[ind]==var[ind+1]:
      count=count+1
    else:
       res=res+str(count)+var[ind]
       count=1
print(res)