class Employee:
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def bonus(self):
        if(self.role=="Manager"):
            print("Bonus = ",self.salary*0.2)
            self.salary+=self.salary*0.2
            print("Total salary(including bonus) = ",self.salary)
        elif(self.role=="Developer"):
            print("Bonus = ",self.salary*0.1)
            self.salary+=self.salary*0.1
            print("Total salary(including bonus) = ",self.salary)
        elif(self.role=="Intern"):
            print("Bonus = ",self.salary*0.05)
            self.salary+=self.salary*0.05
            print("Total salary(including bonus) = ",self.salary)
e=Employee("Shaan",50000,"Manager")
e.bonus()
e=Employee("Surya",40000,"Developer")
e.bonus()
e=Employee("Raghu",30000,"Intern")
e.bonus()