num=int(input("enter your number"))
while(num != 0):
    print(f"{num}/2={num/2}")
    print(f"{num}/3={num/3}")
    num=int(input("enter another number"))
    if(num==0):
        break
