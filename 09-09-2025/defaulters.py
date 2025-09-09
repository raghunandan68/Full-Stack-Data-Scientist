d={}
n=int(input("Enter no. of students : "))
for i in range(n):
    a,b=list(map(str,input(f"Enter student {i+1} name and attendance seperated by space : ").split(" ")))
    d[a]=b
for i in d:
    if(int(d[i])<75):
        print(i,end=" ")