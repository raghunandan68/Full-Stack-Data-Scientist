l=eval(input("Enter the list : "))
p=0
n=0
z=0
for i in l:
    if(i>0):
        p+=1
    elif(i<0):
        n+=1
    elif(i==0):
        z+=1
print("Positive = ",p," Negative = ",n," Zero = ",z)