#Wap to check the string is prindrome or not.
s=input("Enter a string: ")
rev=''
for ind in range(len(s)-1,-1,-1):
    rev=rev+s[ind]
if s==rev:
    print("Palindrome string")
else:
    print("Not palindrome string")