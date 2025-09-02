phone={"Suhel": 9876543210, "Ravi": 9123456780, "Anita": 9988776655}
name=input("Enter the search name : ")
for i in phone:
    if(i.lower()==name.lower()):
        print("Phone Number of ",i," = ",phone.get(i))
        break
