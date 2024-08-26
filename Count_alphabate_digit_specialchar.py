s ="ABHISEK 24@ abhisek"
alphaCount = 0
digCount = 0
specialcharCount = 0

for ch in s:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        alphaCount += 1
    elif '0' <= ch <= '9':
        digCount += 1
    else:
        specialcharCount += 1

print(alphaCount, digCount, specialcharCount)
