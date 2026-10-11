
def test_dict_functions(item: dict):
    print(f"Current dict values: {item}")

    print(f"keys() result: {list(item.keys())}")

    print(f"values() result: {list(item.values())}")

    print(f"items() result: {list(item.items())}")

    item.update({"Age": 26, "City": "Kyiv"})
    print(f"update() result: {item}")

    del item["role"]
    print(f"del item['role'] result: {item}")

    item.clear()
    print(f"clear() result: {item}")

test_dict_functions({"Name": "Ivan", "Age": 29, "role": "Admin"})