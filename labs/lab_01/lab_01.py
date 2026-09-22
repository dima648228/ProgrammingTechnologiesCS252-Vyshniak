
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "email":"bob3214@gmail.com", "money":"32423423"},
    {"name":"Emma", "phone":"0631234567", "email":"emma@ukr.net", "money":"1"},
    {"name":"Jon",  "phone":"0631234567", "email":"jon00@gmail.com", "money":"342"},
    {"name":"Zak",  "phone":"0631234567", "email":"zak44@gmail.com", "money":"3242"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Email is " + elem["email"], " Has " + elem["money"] + " money"
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Plase enter student email: ")
    money = input("Plase enter student money: ")
    newItem = {"name": name, "phone": phone, "email": email, "money": money}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return

def updateElement():
    list_size_before = len(list)

    deleteElement()

    if len(list) < list_size_before: # успішно видалили
        addNewElement()
    else:
        print("not deleted")

    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")

main()