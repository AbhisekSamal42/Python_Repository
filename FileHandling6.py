# WAP to print number of characters, words and lines present in the file.

f=open('data.txt',mode='r')
num_of_words=0
num_of_lines=0
num_of_chars=0
for line in f:
    num_of_lines=num_of_lines+1
    line=line.strip('\n')
    num_of_chars=num_of_chars+len(line)
    list1=line.split()
    num_of_words=num_of_words+len(list1)
f.close()
print("Number of lines:",num_of_lines)
print("Number of words:",num_of_words)
print("number of chars:",num_of_chars)


# Wap to count number of vowles available in the file.

f=open('data.txt',mode='r')
count=0
for line in f:
    for vowel in line:
        if vowel in 'aeiou':
            count=count+1
f.close()
print(count)

# Wap to count number of special character available in a file.

f=open('data.txt',mode='r')
count=0
for line in f:
    line=line.strip('\n')
    for ch in line:
        if not('A'<=ch<='Z' or 'a'<=ch<='z' or '0'<=ch<='9'):
            count=count+1
f.close()
print(count)