#sum of numbers 1-100 (4 different options):

mysum=0
for i in range (1,101):
    mysum=mysum+i
    print(mysum)

a=101
b=1
mysum2=0
while b<a:
    mysum2=mysum2+b
    print(mysum2)
    b=b+1

mysum3=sum(range(0,101))
print(mysum3)

#by list comprehension:

list1=[]
for n in range(0,101):
    list1.append(n)

print(sum(list1))

