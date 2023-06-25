def reverse_tuple(tup):
    reversed_list = []
    for i in range(len(tup) - 1, -1, -1):
        reversed_list.append(tup[i])
    return tuple(reversed_list)
tuple_input = input("Enter the tuple elements (comma-separated): ")
input_tuple = tuple_input.split(',')
reversed_tuple = reverse_tuple(input_tuple)
print("Reversed tuple:", reversed_tuple)
