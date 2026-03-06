class Student: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if self.grades:
            return sum(self.grades)/ len(self.grades)
        return 0
    
# Creating Objects
student1 = Student("Alice", 20)
student1.add_grade(89)
student1.add_grade(91)
print("The average of student1: " , student1.get_average())