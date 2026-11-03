import sys
from classes.student import Student
from classes.studentList import StudentList
from classes.utils import FileManager

def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "lab2.csv"
    
    student_list = StudentList()
    
    loaded_data = FileManager.load_from_csv(filename)
    if loaded_data is not None and len(loaded_data) > 0:
        student_list.students = loaded_data

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice.upper():
            case "C":
                print("New element will be created:")
                name = input("Please enter name: ")
                phone = input("Please enter phone: ")
                email = input("Please enter email: ")
                money = input("Please enter money value: ")
                
                new_student = Student(name, phone, email, money)
                student_list.add_student(new_student)
                student_list.print_all()
            case "U":
                print("Existing element will be updated")
                old_name = input("Please enter name to be updated: ")
                
                new_name = input("Please enter new name: ")
                new_phone = input("Please enter new phone: ")
                new_email = input("Please enter new email: ")
                new_money = input("Please enter new money value: ")
                
                updated_student = Student(new_name, new_phone, new_email, new_money)
                student_list.update_student(old_name, updated_student)
                student_list.print_all()
            case "D":
                print("Element will be deleted")
                name_to_delete = input("Please enter name to be delated: ")
                student_list.delete_student(name_to_delete)
                student_list.print_all()
            case "P":
                print("List will be printed")
                student_list.print_all()
            case "X":
                FileManager.save_to_csv(filename, student_list.students)
                print("Exit()")
                break
            case _:
                print("Wrong chouse")

if __name__ == "__main__":
    main()