try:
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks are betweem 0 to 100")
except ValueError as e:
    print(e)
else:
    print("Status : Valid")