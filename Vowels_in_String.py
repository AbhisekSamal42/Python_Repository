var="I am proud to be an Indian"
vowels="aeiouAEIOU"
res=""
for ch in var:
    if ch in vowels:
        res=res+ch
print(res)