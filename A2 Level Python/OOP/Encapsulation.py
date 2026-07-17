class MyClass:
    def __init__(self):
        self.__x = 10
    def GetX(self):
        return self.__x

Myobj = MyClass()
print(Myobj.GetX())

"-------------------------------------------------------------------------------"

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amount):
        if amount <0:
            print("Deposit amount should be positive")
        else:
            self.__balance = self.__balance + amount
            print("Amount has been added")

    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient funds")
        elif amount < 500:
            print("Withdraw amount should be 500 atleast")
        elif amount % 500 != 0:
            print("Withdraw amount should be multiple of 500")
        else:
            self.__balance -=amount
            print("Amount has been withdrawn successfully")
    def getbalance(self):
        print("Your current balance is PKR",self.__balance)

account1 = BankAccount("Tahir")
account1.getbalance()

useramount = int(input("Enter your amount: ",))
account1.deposit(useramount)

useramount = int(input("Enter your amount: ",))
account1.withdraw(useramount)

account1.getbalance()