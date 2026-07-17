MyList = [4,6,7,2,1]
Boundary = 4
print("Before Sorting")
print(MyList)

swap = True
while swap == True:
    swap = False
    for index in range(0,Boundary):
        if MyList[index]> MyList[index+1]:
            temp = MyList[index+1]
            MyList[index+1] = MyList[index]
            MyList[index] = temp
            swap = True
    Boundary -=1

print("After Sorting")
print(MyList)

"-----------------------------------------------------------------------"

Mylist = [5,4,3,2,1]
print(Mylist)

#Ascending Order
for count in range(4):
    for index in range(4):
        if Mylist[index]>Mylist[index+1]:
            temp = Mylist[index]
            Mylist[index]= Mylist[index+1]
            Mylist[index+1]= temp

print(Mylist)

#Descending Order
for count in range(4):
    for index in range(4):
        if Mylist[index]<Mylist[index+1]:
            temp = Mylist[index]
            Mylist[index]= Mylist[index+1]
            Mylist[index+1]= temp

print(Mylist)
