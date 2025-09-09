with open('sample.txt','r') as f:
    f.read(3)
print(f.closed)
try:
    x=int("a")
except ValueError as e:
    print(type(e).__name__)