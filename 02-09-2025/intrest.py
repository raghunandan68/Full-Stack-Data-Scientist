principle=int(input("Enter principle amount : "))
rate=int(input("Enter rate of intrest : "))
time=int(input("Enter time period : "))
type=input("Enter type of intrest : ")
if(type=="simple" or type=="Simple"):
    total=(principle*rate*time)/100
    print("Simple Intrest = ",total)
    print("Total amount = ",total+principle)
elif(type=="compound" or type=="Compound"):
    amount=(principle*((1+(rate/100))**time))
    ci=amount-principle
    print("Compound Intrest = ",ci)
    print("Total amount = ",ci+principle)