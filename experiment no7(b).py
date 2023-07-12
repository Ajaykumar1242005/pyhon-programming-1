import numpy as np

def convert_to_array(data):
    arr = np.array(data)
    return arr

# Example usage
my_list = [1, 2, 3, 4, 5]
my_tuple = (6, 7, 8, 9, 10)

list_array = convert_to_array(my_list)
tuple_array = convert_to_array(my_tuple)

print("List array:", list_array)
print("Tuple array:", tuple_array)
