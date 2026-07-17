file = open("FirstFileProgram.txt", "w")

for count in range(10):
    Mydata = input("Enter student name")
    file.write(Mydata)
    file.write("\n")


MyArray = ["" for count in range(10)]
file = open("FirstFileProgram.txt", "r")
for count in range(10):
    FileData = file.readline().strip() #strip whitespaces hta deta hai
    MyArray[count]=FileData

print(MyArray)

"---------------------------------------------------------------------"
try:
    File = open("Progress.txt","r")
    GameData = File.read()
    File.close()
except:
    print("File does not exist")

try:
    num = int(input("Enter Number :" ))
    print(num)
except ValueError:
    print("Integer Only")

try:
    num = 5/0
    print(num)
except ZeroDivisionError:
    print("Can't Divide by Zero")

try:
    file = open("StackData.txt","r")
except IOError:
    print("File does not exist")


    ("\n is new line | EOF = for line in file: ")