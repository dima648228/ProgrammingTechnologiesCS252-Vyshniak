import pytest
import lab_02
from lab_02 import (
    addNewElement,
    deleteElement,
    updateElement,
    loadFromCsv,
    saveToCsv
)


@pytest.fixture(autouse=True)
def reset_list():
    lab_02._list = [
        {"name": "Bob", "phone": "0631234567", "email": "bob3214@gmail.com", "money": "32423423"},
        {"name": "Emma", "phone": "0631234567", "email": "emma@ukr.net", "money": "1"},
        {"name": "Jon", "phone": "0631234567", "email": "jon00@gmail.com", "money": "342"},
        {"name": "Zak", "phone": "0631234567", "email": "zak44@gmail.com", "money": "3242"}
    ]

#перевірка на успішне додавання елементу
def test_add_new_element(monkeypatch):
    user_inputs = iter(["Alex", "0991112233", "alex@gmail.com", "500"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    addNewElement("", "", "", "")

    assert len(lab_02._list) == 5
    assert lab_02._list[0]["name"] == "Alex"

#перевірка на успішне видалення елементу
def test_delete_element_success(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Emma")

    deleteElement("Enter name: ")

    assert len(lab_02._list) == 3
    names = [item["name"] for item in lab_02._list]
    assert "Emma" not in names

#перевірка на відсутність імені при видаленні
def test_delete_element_not_found(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "fdughfdoprgmpdrh")

    deleteElement("Enter name: ")

    assert len(lab_02._list) == 4

#перевірка на успішне оновлення елемента
def test_update_element(monkeypatch):
    user_inputs = iter(["Bob", "Bobby", "0990000000", "bobby@gmail.com", "5000"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    updateElement()

    names = [item["name"] for item in lab_02._list]
    assert "Bob" not in names
    assert "Bobby" in names

#перевірка на успішне збереження та завантаження файлу 
def test_csv_save_and_load(tmp_path):
    test_file = "lab2.csv"

    saveToCsv(test_file, lab_02._list)
    loaded_data = loadFromCsv(test_file)

    assert loaded_data is not None
    assert len(loaded_data) == 4
    assert loaded_data[0]["name"] == "Bob"