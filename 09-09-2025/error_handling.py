try:
    n=int(input("Enter number 1 : "))
    b=int(input("Enter number 2 : "))
    res=n/b
    print(res)
except(ValueError):
    print("Enter valid input")
except(ZeroDivisionError):
    print("Cannot divide by zero.")
finally:
    print("Task done.")