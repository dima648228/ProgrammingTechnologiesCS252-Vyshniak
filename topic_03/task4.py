def find_insert_position(sorted_list, target):
    low = 0
    high = len(sorted_list)

    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low

sorted_arr = [10, 20, 30, 40, 50]
new_item = 35

position = find_insert_position(sorted_arr, new_item)

print(f"Sorted list: {sorted_arr}")
print(f"New element: {new_item}")
print(f"Position for insert: {position}")

sorted_arr.insert(position, new_item)
print(f"Result: {sorted_arr}")