import student_utils as stu
user = int(input("Enter Marks: "))

print("Grade: ", stu.student_grade(user))
print("Status: ", stu.student_status(user))