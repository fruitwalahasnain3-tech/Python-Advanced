try:
    a = int(input("Enter number 1 :"))
    b = int(input("Enter number 2 :"))

    result = a/b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")