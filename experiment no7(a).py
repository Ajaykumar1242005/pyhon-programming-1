import numpy as np

def list_to_numpy(lst):
    arr = np.array(lst)
    return arr

# Example usage
numeric_list = [1, 2, 3, 4, 5]
numpy_array = list_to_numpy(numeric_list)
print(numpy_array)
