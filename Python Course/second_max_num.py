def secondmax (list1):
    maxnum=0
    secondmaxnum=0
    for i in range (1,len(list1)):
        if list1[i] >maxnum:
            maxnum=list1[i]
    for j in range (1,len(list1)):
        if list1[j]<maxnum:
            if list1[j] > secondmaxnum:
                secondmaxnum=list1[j]
    return secondmaxnum


list1=[]
num=int(input("enter a number to the list,-1 ends"))
while num != -1:
    list1.append(num)
    num=int(input("enter another number to the list,-1 ends"))

print(f"your list is: {list1}")
print(f"the second max number is: {secondmax(list1)}")


