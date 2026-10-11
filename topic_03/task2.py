
def test_list_functions(values: []):
    print(f"Current list values: {values}")

    values.append(90)
    print(f"append(90) result: {values}")

    values.extend([30, 20])
    print(f"extend([30, 20]) result: {values}")

    values.insert(1, 44)
    print(f"insert(1, 44) result: {values}")

    values.remove(30)
    print(f"remove(30) result: {values}")

    values_copy = values.copy()
    print(f"copy() result: {values_copy}")

    values.sort()
    print(f"sort() result: {values}")

    values.reverse()
    print(f"reverse() result: {values}")

    values.clear()
    print(f"clear() result: {values}")

values = [35, 23, 89, 10]
test_list_functions(values)