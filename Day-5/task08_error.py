try:
    marks = int(input("Enter student marks: "))

    try:
        if marks < 0 or marks > 100:
            raise ValueError("Marks are betweem 0 to 100")
    except ValueError as e:
        print(e)
    else:
        print("Marks accepted:", marks)        
except ValueError:
    print("Invalid marks! Enter a number.")
