a,b=list(map(int,input("Enter two numbers seperated by space : ").split(" ")))
try:
    res=a/b
    print(res)
except:
    print("Cannot divide by zero")