temp=int(input("Enter the temperature : "))
if(temp>=35):
    print("Too hot, stay indoors!")
elif(temp>=20 and temp<35):
    print("Nice weather, go out!")
elif(temp<20):
    print("It’s cold, wear warm clothes!")