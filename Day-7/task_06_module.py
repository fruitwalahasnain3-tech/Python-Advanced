from validation import is_valid
import student_utils as stu

user = int(input("Enter Marks: "))


if is_valid(user):
    print("Grade: ",stu.student_grade(user))
    print("Status: ",stu.student_status(user))
else:
    print("Invalid Marks")