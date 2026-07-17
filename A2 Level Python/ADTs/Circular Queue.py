global MyData
global Start
global End
global Size
MyData = [0 for count in range(5)]
Start = 0
End = 0
Size = 0

def Enqueue(item):
    global MyData
    global Start
    global End
    global Size
    if Size == 5:
        print("Queue is full")
    elif Size < 5 and End == 5:
        End = 0
        MyData[End] = item
        End +=1
        Size +=1
    else:
        MyData[End] = item
        End += 1
        Size += 1
def Dequeue():
    global MyData
    global Start
    global End
    global Size
    if Size ==0:
        print("Queue is empty")
    else:
        MyData[Start]=0
        Start +=1
        Size -=1

for count in range(5):
    Enqueue(5)

print(MyData)
Dequeue()
Dequeue()
Dequeue()

print(MyData)
Enqueue(5)

print(MyData)

"----------------------------------------------------------------------------"

global MyList
global Soq,EoQ

MyList = [0 for count in range(8)]
Soq = 0
EoQ = -1
Size = 0

def Enqueue(value):
    global MyList
    global Soq, EoQ
    global Size
    if Size == 8:
        print("Queue is full")
    elif Size<8 and EoQ == 7:
        EoQ =0
        MyList[EoQ] = value
        Size += 1
    else:
        EoQ += 1
        MyList[EoQ]= value
        Size +=1
        print("Added")

def Dequeue():
    global MyList
    global Soq, EoQ
    global Size
    if Soq>EoQ:
        print("Queue is empty")
    else:
        MyList[Soq] = 0
        Soq += 1
        Size-=1

Enqueue(1)
Enqueue(2)
Enqueue(3)
Enqueue(4)
Enqueue(5)
Enqueue(6)
Enqueue(7)
Enqueue(8)
print(MyList)
print("Size of Queue is",Size)


Dequeue()
Dequeue()
Dequeue()

print(MyList)
print("Size of Queue is",Size)

Enqueue(71)
print(MyList)