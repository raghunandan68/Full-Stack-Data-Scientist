import random
import string
n=int(input("Enter length : "))
ch=string.ascii_letters+string.digits
res=''.join(random.choice(ch) for _ in range(n))
print(res)