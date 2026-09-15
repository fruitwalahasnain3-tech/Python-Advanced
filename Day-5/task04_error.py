try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print(a/b)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero")
else: 
    print("Division Successfully!")