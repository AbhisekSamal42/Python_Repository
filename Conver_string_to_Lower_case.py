#using lower method.

s=input("Enter a string in capital letter: ")
print(s.lower())

#Without using lower method.

s=input("Enter a string in capital letter: ")
res=""
for ind in range(len(s)):
    if "A"<=s[ind]<="Z":
        res=res+chr(ord(s[ind])+32)
    else:
        res=res+s[ind]
print(res)