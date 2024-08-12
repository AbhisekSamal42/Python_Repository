def is_even(num):
    if num%2==0:
        return "Even number"
    return "odd number"
for val in map(is_even,range(11,16)):
    print(val)