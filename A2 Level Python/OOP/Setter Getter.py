class MyClass:
    def __init__(self):
        self.__x = 10
    def getX(self):
        return self.__x
        #Getter
    def setx(self,x):
        self.__x = x
        #Setter

Myobj = MyClass()
print("Current Value: ",Myobj.getX())
y = input("Enter New Value : ",)
Myobj.setx(y)
print(Myobj.getX())

"------------------------------------------------------------------------------------------"