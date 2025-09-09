import os
count=0
with open('sample.txt','r') as f:
    c=f.read()
    for k in c:
        if(k==' ' or k=='\n'):
            count+=1
print("Total words = ",count)