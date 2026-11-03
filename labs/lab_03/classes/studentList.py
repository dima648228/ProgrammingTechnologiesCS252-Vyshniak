from classes.student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        insert_position = 0
        for s in self.students:
            if student.name > s.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student)
        print("New element has been added")

    def delete_student(self, name: str) -> bool:
        delete_position = -1
        for i, student in enumerate(self.students):
            if student.name == name:
                delete_position = i
                break
        
        if delete_position == -1:
            print("Element was not found")
            return False
        else:
            print(f"Dele position {delete_position}")
            del self.students[delete_position]
            return True

    def update_student(self, old_name: str, new_student: Student):
        if self.delete_student(old_name):
            self.add_student(new_student)
        else:
            print("not deleted")

    def print_all(self):
        for student in self.students:
            print(student)