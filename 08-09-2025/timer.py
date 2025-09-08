import time
def countdown(n):
    while n>0:
        print(n)
        time.sleep(1)
        n-=1
s=input()
if(s.startswith("countdown(") and s.endswith(")")):
    n=int(s[10:len(s)-1])
    countdown(n)
    print("Time's up!")
else:
    print("Invalid input")