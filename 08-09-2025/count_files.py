import os
from collections import Counter
# files=["notes.txt", "app.py", "data.csv", "report.txt", "main.py"]
# t_count=0
# p_count=0
# for i in files:
#     k=i.split(".")
#     if(k[1]=="txt"):
#         t_count+=1
#     elif(k[1]=="py"):
#         p_count+=1
# print("Text files = ",t_count)
# print("Python files = ",p_count)
l=[]
dir1='D:/Python/08-09-2025'
for i in os.listdir(dir1):
    if os.path.isfile(i):
        a,e=os.path.splitext(i)
        l.append(e)
print(dict(Counter(l)))