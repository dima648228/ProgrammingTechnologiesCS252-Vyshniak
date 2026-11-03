import pytest

from classes.studentList import StudentList
from classes.student import Student
from classes.utils import FileManager

@pytest.fixture
def student_directory():
    directory = StudentList()
    directory.students = [
        Student("Bob", "0631234567", "bob3214@gmail.com", "32423423"),
        Student("Emma", "0631234567", "emma@ukr.net", "1"),
        Student("Jon", "0631234567", "jon00@gmail.com", "342"),
        Student("Zak", "0631234567", "zak44@gmail.com", "3242")
    ]
    return directory

#перевірка на успішне додавання елементу
def test_add_new_element(student_directory):
    new_student = Student("Alex", "0991112233", "alex@gmail.com", "500")
    student_directory.add_student(new_student) 

    assert len(student_directory.students) == 5
    assert student_directory.students[0].name == "Alex"

#перевірка на успішне видалення елементу
def test_delete_element_success(student_directory):
    result = student_directory.delete_student("Emma")

    assert result is True
    assert len(student_directory.students) == 3
    names = [student.name for student in student_directory.students]
    assert "Emma" not in names

#перевірка на відсутність імені при видаленні
def test_delete_element_not_found(student_directory):
    result = student_directory.delete_student("fdughfdoprgmpdrh")

    assert result is False
    assert len(student_directory.students) == 4

#перевірка на успішне оновлення елемента
def test_update_element(student_directory):
    updated_student = Student("Bobby", "0990000000", "bobby@gmail.com", "5000")
    student_directory.update_student("Bob", updated_student)

    names = [student.name for student in student_directory.students]
    assert "Bob" not in names
    assert "Bobby" in names

#перевірка на успішне збереження та завантаження файлу 
def test_csv_save_and_load(tmp_path, student_directory):
    test_file = tmp_path / "lab2.csv"
    
    FileManager.save_to_csv(str(test_file), student_directory.students)
    
    loaded_directory = StudentList()
    loaded_directory.students = FileManager.load_from_csv(str(test_file))

    assert loaded_directory.students is not None
    assert len(loaded_directory.students) == 4
    assert loaded_directory.students[0].name == "Bob"