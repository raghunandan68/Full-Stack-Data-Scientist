class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def getAverage(self):
        return sum(self.marks)/len(self.marks)
    def add_mark(self,mark):
        marks_list=self.marks
        marks_list.append(mark)
        return marks_list
    def get_highest(self):
        return max(self.marks)
    def get_lowest(self):
        return min(self.marks)
s=Student("Tom", [90, 80, 85])
print("Average = ",s.getAverage())
print("Added marks = ",s.add_mark(95))
print("Maximum = ",s.get_highest())
print("Minimum = ",s.get_lowest())