class Professor:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.course = None
        self.task = None
    def teach(self, course):
        self.course = course
        return f"{self.name} is teaching {self.course}"
    def give_assignment(self, task):
        self.task = task
        return f"Assignment given: {self.task}"
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.assignments = []
    def enroll(self, course):
        self.courses.append(course)
        return f"{self.name} enrolled in {course}"
    def submit_assignment(self, task):
        self.assignments.append(task)
        return f"{self.name} submitted {task}"
prof = Professor("Dr. Smith", "Computer Science")
stud = Student("Alice")
print(prof.teach("Python"))
print(stud.enroll("Python"))
print(prof.give_assignment("Project 1"))
print(stud.submit_assignment("Project 1"))