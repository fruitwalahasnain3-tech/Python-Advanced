try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print(a/b)
except ValueError:
    print("Invalid input! Enter a vaild number")
except ZeroDivisionError:
    print("cannot divide by zero")