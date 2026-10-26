class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student name is {self.name} and age is {self.age}"

students = [
    Student("Олександр", 18),
    Student("Марія", 17),
    Student("Іван", 19),
    Student("Анна", 16)
]

sorted_by_age = sorted(students, key=lambda student: student.age)

for student in sorted_by_age:
    print(student)

print("\n")

sorted_by_name = sorted(students, key=lambda student: student.name.lower())

for student in sorted_by_name:
    print(student)