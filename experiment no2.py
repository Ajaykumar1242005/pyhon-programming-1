def is_obtainable(first_string, second_string):
    i = 0  
    j = 0
    while i < len(first_string) and j < len(second_string):
        if first_string[i] == second_string[j]:
            j += 1
        i += 1
    return j == len(second_string)
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")
result = is_obtainable(first_string, second_string)
if result:
    print("The second string can be obtained from the first string.")
else:
    print("The second string cannot be obtained from the first string.")
    
