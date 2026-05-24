#check if there are at least 1 same number at 2 lists:

def mylist(list1,list2):
    for i in range(0,len(list1)):
       for j in range(0,len(list2)):
           if list1[i]==list2[j]:
            print("True")
            break

list1=[1,2,3]
list2=[4,5,2]
mylist(list1,list2)


#delete odd numbers from the list:

def mylist2(list3, list4):
   for i in range(0, len(list3)):
        if int(list3[i] % 2)==0:
            list4.append(list3[i])
   return list4

list3=[1,2,3,4,5,6,7,8,9]
list4=[]
mylist2(list3,list4)
print("old list:",list3)
print("new list:",list4)


