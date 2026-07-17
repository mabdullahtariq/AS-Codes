class greeting:
    def hello(self, name = None):
        if name is not None:
            print("Hello ",name)
        else:
            print("Hello")

greeting1 = greeting()
greeting1.hello("Ali")
greeting1.hello()

"-------------------------------------------------------------------------------------------------------------"

class calculate:
    def addition(self,a = 0,b = 0,c = 0):
        return a+b+c

objcal = calculate()
print(objcal.addition())
print(objcal.addition(5))
print(objcal.addition(10,5))
print(objcal.addition(5,10,20))