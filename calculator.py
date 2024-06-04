print("this is a calculator program//////////////////////////")
print("this will show the uses  print,escape command and user input command and data type")
print("\n")
print("--------------------------------------calculator---------------------------------------------------")
print("enter the first nummber:-")
x= int(input())
print("enter the second number:-")
y=int(input())
print("enter the operation")
z=str(input())
match z:
    case "+":
        print("sum of X and Y is :", x+y)
    case "-":
        print("subraction of X and Y is :", x-y)
    case "*":
        print("multiplication of X and Y is :", x*y)
    case "/":
        print("division of X and Y is :", x/y)
    case _:
        print("invalid number or operation")




