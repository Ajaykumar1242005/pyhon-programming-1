def is_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
input_list = input("Enter the list elements(with space): ").split()
input_list = [int(num) for num in input_list]
result = is_ascending(input_list)

if result:
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")
