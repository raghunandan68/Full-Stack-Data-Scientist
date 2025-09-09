# import operator
# q=input()
# print(eval(f"operator.{q}"))
a,b=list(map(int,input("Enter two numbers seperated by space : ").split(" ")))
print("Menu\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
while True:
    ch=int(input("Enter your choice : "))
    if(ch<=1 and ch>=5):
        print("Invalid choice.")
        exit(1)
    else:
        if(ch==1):
            print(f"Addition of {a} and {b} is {a+b}")
        elif(ch==2):
            print(f"Difference of {a} and {b} is {a-b}")
        elif(ch==3):
            print(f"Product of {a} and {b} is {a*b}")
        elif(ch==4):
            if(b==0):
                print("Division not possible")
            else:
                print(f"Division of {a} and {b} is {a//b}")
        elif(ch==5):
            print("Exiting program...")
            exit(1)