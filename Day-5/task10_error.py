try:
    name = input("Enter student Name: ")
    marks = int(input("Enter student marks: "))
    try:
        if marks < 0 or marks > 100:
            raise ValueError("Marks are in between 0 to 100")
    except ValueError as e:
        print(e)
    else:
        print("\nStudent: ", name)
        print("Marks: ", marks)
        if marks >= 50:
            print("Status: Pass")
        else:
            print("Status: Fail")

except ValueError:
    print("Invalid Input!")

finally:
    print("Progra finished")