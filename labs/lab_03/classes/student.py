class Student:
    def __init__(self, name: str, phone: str, email: str, money: str):
        self.name = name
        self.phone = phone
        self.email = email
        self.money = money

    def __str__(self):
        return f"Student name is {self.name},  Phone is {self.phone}, Email is {self.email}, Has {self.money} money"