import csv
import sys

_list = [
    {"name": "Bob", "phone": "0631234567", "email": "bob3214@gmail.com", "money": "32423423"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@ukr.net", "money": "1"},
    {"name": "Jon", "phone": "0631234567", "email": "jon00@gmail.com", "money": "342"},
    {"name": "Zak", "phone": "0631234567", "email": "zak44@gmail.com", "money": "3242"}
]


def loadFromCsv(filename: str):
    data = []
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append({
                    "name": row.get("name", "").strip(),
                    "phone": row.get("phone", "").strip(),
                    "email": row.get("email", "").strip(),
                    "money": row.get("money", "").strip()
                })
        print(f"Data successfully loaded from {filename}")
        return data
    except FileNotFoundError:
        print(f"File {filename} not found. Using default list.")
        return None
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None


def saveToCsv(filename: str, data_list: list):
    fieldnames = ["name", "phone", "email", "money"]
    try:
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_list)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving CSV: {e}")


def printAllList():
    for elem in _list:
        strForPrint = (
            "Student name is " + elem["name"] +
            ",  Phone is " + elem["phone"] +
            ", Email is " + elem["email"] +
            ", Has " + elem["money"] + " money"
        )
        print(strForPrint)
    return


def addNewElement(mes1: str, mes2: str, mes3: str, mes4: str):
    name = input(mes1)
    phone = input(mes2)
    email = input(mes3)
    money = input(mes4)
    newItem = {"name": name, "phone": phone, "email": email, "money": money}
    
    insertPosition = 0
    for item in _list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    _list.insert(insertPosition, newItem)
    print("New element has been added")
    return


def deleteElement(mes: str):
    name = input(mes)
    deletePosition = -1
    for item in _list:
        if name == item["name"]:
            deletePosition = _list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        del _list[deletePosition]
    return


def updateElement():
    list_size_before = len(_list)
    deleteElement("Please enter name to be updated: ")
    if len(_list) < list_size_before:
        addNewElement(
            "Please enter new name: ",
            "Please enter new phone: ",
            "Please enter new email: ",
            "Please enter new money value: "
        )
    else:
        print("not deleted")
    return


def main():
    global _list
    filename = sys.argv[1] if len(sys.argv) > 1 else "lab2.csv"
    
    loaded_data = loadFromCsv(filename)
    if loaded_data is not None and len(loaded_data) > 0:
        _list = loaded_data

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement("Please enter name: ", "Please enter phone: ", "Please enter email: ", "Please enter money value: ")
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement("Please enter name to be delated: ")
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                saveToCsv(filename, _list)
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


if __name__ == "__main__":
    main()