def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num % 2 == 0:  
    if num < 0:
        print("Factorial does not exist for negative numbers.")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        fact = factorial(num)
        print("The factorial of", num, "is", fact)
else:  
    temp = num
    rev = 0

    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10

    if temp == rev:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
