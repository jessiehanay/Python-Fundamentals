num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number:"))
if (num1 > num2):
    print(f"{num1} is the bigger of the first 2")
else:
    print(f"{num2} is the bigger of the first 2")

#check is they are both have the same sign(+/-)-->both positive or both negative
if(num1>0 and num2>0) or (num1<0 and num2<0):
    print("True")
else:
    print("False")

 #now with 3 numbers
num3 = int(input("Enter another number: "))
if (num1 > num2):
    if(num1 > num3):
        print(f"{num1} is the biggest")
    else:
        print(f"{num3} is the biggest")
else:
    if(num2 > num3):
        print(f"{num2} is the biggest")
    else:
        print(f"{num3} is the biggest")