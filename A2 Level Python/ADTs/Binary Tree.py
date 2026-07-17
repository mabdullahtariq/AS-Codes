
ArrayNodes =[[0 for X in range(3)] for Y in range(20)]
RootPointer = -1
FreeNode = 0

def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter the Data: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1: # Add to start
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")
    return ArrayNodes, RootPointer, FreeNode

def PrintAll(ArrayNodes):
    for X in range(0, 20):
        print(str(ArrayNodes[X][0]), " ", str(ArrayNodes[X][1]), " ",
              str(ArrayNodes[X][2]))

for X in range(0 ,3):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes ,RootPointer ,FreeNode)


PrintAll(ArrayNodes)

'------------------------------------------------------------------------------------------------------------'

ArrayNode = []
for x in range(0,20):
    ArrayNode.append([-1,-1,-1])

ArrayNode = [[1,20,5],[2,15,-1],[-1,3,3],[-1,9,4],[1,10,-1],[-1,58,-1]]
FreeNode = 6
RootPointer = 0


#Searching in Binary Tree
def SearchValue(Root, ValueToFind):
    global ArrayNode
    if Root == -1:
        return -1
    elif ArrayNode[Root][1] == ValueToFind:
        return Root
    elif ArrayNode[Root][1] == -1:
        return -1
    if (ArrayNode[Root][1]>ValueToFind):
        return SearchValue(ArrayNode[Root][0], ValueToFind)
    if (ArrayNode[Root][1]<ValueToFind):
        return SearchValue(ArrayNode[Root][2],ValueToFind)


Search = int(input("Enter a value you want to search"))
Returnvalue = SearchValue(RootPointer,Search)
if Returnvalue == -1:
    print("Not Found")
else:
    print("Found at" + str(Returnvalue))

'-------------------------------------------------------------------------------'

#Inorder Binary Tree Traversal
def InOrder(ArrayNodes, RootNode):
    if ArrayNodes[RootNode][0] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][0])
    print(str(ArrayNodes[RootNode][1]))
    if ArrayNodes[RootNode][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][2])

ArrayNodes = [[1, 11, 2],[3, 2, 4],[-1, 13, -1],[-1, 1, -1],[-1, 5, -1]]
RootPointer = 0
print("#Inorder Binary Tree Traversal")
InOrder(ArrayNodes, RootPointer)

#Preorder Binary Tree Traversal
def PreOrder(ArrayNodes, RootNode):
    print(str(ArrayNodes[RootNode][1]))
    if ArrayNodes[RootNode][0] != -1:
        PreOrder(ArrayNodes, ArrayNodes[RootNode][0])
    if ArrayNodes[RootNode][2] != -1:
        PreOrder(ArrayNodes, ArrayNodes[RootNode][2])

ArrayNodes = [[1, 11, 2],[3, 2, 4],[-1, 13, -1],[-1, 1, -1],[-1, 5, -1]]
RootPointer = 0
print("#Preorder Binary Tree Traversal")
PreOrder(ArrayNodes,RootPointer)

#Postorder Binary Tree Traversal
def PostOrder(ArrayNodes, RootNode):
    if ArrayNodes[RootNode][0] != -1:
        PostOrder(ArrayNodes, ArrayNodes[RootNode][0])
    if ArrayNodes[RootNode][2] != -1:
        PostOrder(ArrayNodes, ArrayNodes[RootNode][2])
    print(str(ArrayNodes[RootNode][1]))

ArrayNodes = [[1, 11, 2],[3, 2, 4],[-1, 13, -1],[-1, 1, -1],[-1, 5, -1]]
RootPointer = 0
print("#Postorder Binary Tree Traversal")
PostOrder(ArrayNodes,RootPointer)

'-------------------------------------------------------------------------------'

'Complete question of Searching and Adding node in Binary Tree.'
ArrayNode = []
ArrayNode = [[1,20,5],[2,15,-1],[-1,3,3],[-1,9,4],[1,10,-1],[-1,58,-1]]
for x in range(6,20):
    ArrayNode.append([-1,-1,-1])

FreeNode = 6
RootPointer = 0

#Searching in Binary Tree
def SearchValue(Root, ValueToFind):
    global ArrayNode
    if Root == -1:
        return -1
    elif ArrayNode[Root][1] == ValueToFind:
        return Root
    elif ArrayNode[Root][1] == -1:
        return -1
    if (ArrayNode[Root][1]>ValueToFind):
        return SearchValue(ArrayNode[Root][0], ValueToFind)
    if (ArrayNode[Root][1]<ValueToFind):
        return SearchValue(ArrayNode[Root][2],ValueToFind)

def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter the Data: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1: # Add to start
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")
    return ArrayNodes, RootPointer, FreeNode

def PrintAll(ArrayNodes):
    for X in range(0, 20):
        print(str(ArrayNodes[X][0]), " ", str(ArrayNodes[X][1]), " ",
              str(ArrayNodes[X][2]))

Search = int(input("Enter a value you want to search"))
Returnvalue = SearchValue(RootPointer,Search)
if Returnvalue == -1:
    print("Not Found")
else:
    print("Found at" + str(Returnvalue))

for X in range(0 ,3):
    ArrayNode, RootPointer, FreeNode = AddNode(ArrayNode ,RootPointer ,FreeNode)


PrintAll(ArrayNode)