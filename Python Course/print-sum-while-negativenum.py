#stop when user enters negative number and print the sum:

mysum = 0
n = int(input("please enter a number:"))
while (n>=0):
    mysum = mysum + n
    n = int(input("please enter an another number:"))
print("sum is:" + mysum)
