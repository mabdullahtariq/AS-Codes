class Student():
    def SName(self):
        print("This is the student Name")
    def Sclass(self):
        print("This is A2 class")

student1 = Student()
student1.SName()
student1.Sclass()

student2 = Student()
student2.SName()

"-------------------------------------------------------------------------"

class Car:
    def __init__(self):
        self.Model = "Honda"
        self.year = 2025

    def display(self):
        print("My car model is", self.Model)
        print("My car year is", self.year)

Mycar1 = Car()
Mycar1.display()
print(Mycar1.Model)
print(Mycar1.year)

'----------------------------------------------------------------------------------------'

class Car:
    def __init__(self,m,y):
        self.Model = m
        self.year = y

    def display(self):
        print("My car model is", self.Model)
        print("My car year is", self.year)

#Object 1
carmodel = input("Enter your car model")
caryear = int(input("Enter your car year"))
Mycar1 = Car(carmodel,caryear)
Mycar1.display()

#Object 2
carmodel = input("Enter your car model")
caryear = int(input("Enter your car year"))
Mycar2 = Car(carmodel,caryear)
Mycar2.display()



"--------------------------------------------------------------------------------------"

class Car():

    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model)
        print("color is", self.color)


# both objects have different self which contain their attributes
audi = Car("audi a4", "blue")
ferrari = Car("ferrari 488", "green")

audi.show()  # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)

print("Model for audi is ", audi.model)
print("Colour for ferrari is ", ferrari.color)