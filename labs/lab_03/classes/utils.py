import csv

from classes.student import Student

class FileManager:
    @staticmethod
    def load_from_csv(filename: str):
        data = []
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    student = Student(
                        name=row.get("name", "").strip(),
                        phone=row.get("phone", "").strip(),
                        email=row.get("email", "").strip(),
                        money=row.get("money", "").strip()
                    )
                    data.append(student)
            print(f"Data successfully loaded from {filename}")
            return data
        except FileNotFoundError:
            print(f"File {filename} not found. Using default list.")
            return None
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return None

    @staticmethod
    def save_to_csv(filename: str, students_list: list):
        fieldnames = ["name", "phone", "email", "money"]
        try:
            with open(filename, mode='w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for student in students_list:
                    writer.writerow({
                        "name": student.name,
                        "phone": student.phone,
                        "email": student.email,
                        "money": student.money
                    })
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving CSV: {e}")