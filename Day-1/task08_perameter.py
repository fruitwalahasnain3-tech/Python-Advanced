def student_info(name,*marks,**info):
    print(name)
    print(marks)
    print(info)

student_info(
    "Hasnain",
    84,75,94,
    course = "BCA",
    semester = 5
)