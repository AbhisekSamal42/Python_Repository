def is_Facinating(num):
    Check=str(num*1)+str(num*2)+str(num*3)
    for val in range(1,10):
        if str(val) not in Check:
            return False
    return True
num=int(input("Enter a number: "))
if is_Facinating(num):
    print("Facinating number")
else:
    print("Not facinating number")