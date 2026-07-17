class vehicle:
    def __init__(self,brand):
        self.brand = brand
    def description(self):
        print("This is a ", self.brand,"vehicle.")
class car(vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model
    def description(self):
        print(f"This is a {self.brand} {self.model} car.")

car1 = car("Toyota","Corolla")
car1.description()
car2 = vehicle("Honda")
car2.description()

"-----------------------------------------------------------------------------------------------------------"

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def greet(self):
        print(f"Hello, My name is {self.name}.")

class Employee(Person):
    def __init__(self,name,age,job_title):
        super().__init__(name,age)
        self.job_title = job_title
    def greet(self):
        super().greet()
        print(f"I am a {self.job_title}.")

employee1 = Employee("Ahyan",30,"Software Engineer")
employee1.greet()