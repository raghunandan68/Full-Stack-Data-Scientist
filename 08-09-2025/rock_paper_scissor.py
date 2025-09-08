import random
chances=['Rock','Paper','Scissor']
s=input("Enter user's choice : ")
c=random.choice(chances)
if(s==c):
    print("Match Tied!")
elif(s=="Rock" and c=="Paper"):
    print("You chose ",s," Computer chose ",c)
    print("Computer wins!")
elif(s=="Rock" and c=="Scissor"):
    print("You chose ",s," Computer chose ",c)
    print("You win!")
elif(s=="Paper" and c=="Rock"):
    print("You chose ",s," Computer chose ",c)
    print("You win!")
elif(s=="Paper" and c=="Scissor"):
    print("You chose ",s," Computer chose ",c)
    print("Computer wins!")
elif(s=="Scissor" and c=="Rock"):
    print("You chose ",s," Computer chose ",c)
    print("Computer wins!")
elif(s=="Scissor" and c=="Paper"):
    print("You chose ",s," Computer chose ",c)
    print("You win!")