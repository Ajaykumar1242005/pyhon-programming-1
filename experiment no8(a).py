import numpy as np
import pandas as pd
def numpy_to_dataframe(data):
    df = pd.DataFrame(data)
    return df
def series_to_dataframe(series):
    df = pd.DataFrame(series)
    return df
numpy_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
series = pd.Series([10, 20, 30, 40, 50])
array_df = numpy_to_dataframe(numpy_array)
series_df = series_to_dataframe(series)
print("Array DataFrame:")
print(array_df)
print("\nSeries DataFrame:")
print(series_df)
