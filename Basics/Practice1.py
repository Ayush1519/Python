a= int(input("Enter value of a: ")) # question no 2
b= int(input("Enter value of b: "))
c=int(input("Enter value of c:"))

if(a>b and a>c):
    print("a is greatest")
elif(b>a and b>c):
    print("b is greatest")
else:
    print("c is greatest")

marks= int(input("Enter marks: ")) # question no 3
if(marks>90):
    print("Grade A")
elif(marks>80):
    print("Grade B")
elif(marks>70):
    print("Grade C")
else:
    print("Fail")

age= int(input("Enter age: ")) # question no 4
if(age<13):
    print("Child")
elif(age>13):
    print("Teen")
elif(age>23 and age<59):
    print("Adult")
else:
    print("Senior citizen")

attempts = 0

while attempts < 3:
    username = input("Enter your name: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "123":
        print("Login Successful")
        break
    else:
        attempts += 1
        print("Invalid credentials. Attempts left:", 3 - attempts)

if attempts == 3:
    print("Account Locked")
