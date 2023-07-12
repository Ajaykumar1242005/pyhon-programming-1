import pandas as pd
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([6, 7, 8, 9, 10])
addition = series1 + series2
subtraction = series1 - series2
multiplication = series1 * series2
division = series1 / series2
print("Addition:")
print(addition)
print("\nSubtraction:")
print(subtraction)
print("\nMultiplication:")
print(multiplication)
print("\nDivision:")
print(division)
