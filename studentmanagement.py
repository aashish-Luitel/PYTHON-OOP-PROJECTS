class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class student(person):
    def __init__(self, name, age, grade):
        self.grade = grade
        super().__init__(name, age)

    def __str__(self):
        return f"{self.name} is {self.age} years old. They are currently studying in {self.grade} grade"

student1 = student("Aashish", 15, 11)
student2 = student("Ram", 14, 9)

print(student1)
print(student2)