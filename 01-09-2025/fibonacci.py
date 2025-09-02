def fib(n):
    if(n==1 or n==2):
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter number of terms : "))
print("Fibonacci of ",n," terms is = ",end=" ")
for i in range(1,n+1):
    print(fib(i),end= " ")