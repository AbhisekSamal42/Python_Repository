#wap to print Sum of two number by using lambda function.
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
sum=(lambda a,b:a+b)
print(sum(a,b))