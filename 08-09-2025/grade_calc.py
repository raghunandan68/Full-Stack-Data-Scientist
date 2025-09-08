def cal_grade(marks):
    grade=''
    res=sum(marks)/len(marks)
    if(res>=80):
        grade='Grade A'
    elif(res>=70):
        grade='Grade B'
    elif(res>=60):
        grade='Grade C'
    elif(res>=50):
        grade='Grade D'
    elif(res>=40):
        grade='Grade E'
    else:
        grade='Fail'
    return grade
s=eval(input("Enter marks : "))
print(cal_grade(s))