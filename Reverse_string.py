#Wap to  reverse the string by using range function.
s=input("Enter a string: ")
rev=''
for ind in range(len(s)-1,-1,-1):
    rev=rev+s[ind]
print(rev)


#Wap to reverse the string by not using reverse function.
s=input("Enter a string: ")
rev=''
for char in s:
    rev=char+rev
print(rev)