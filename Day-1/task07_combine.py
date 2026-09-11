def student_info(*marks,**info):
    print(marks)
    print(info)


student_info(
    84,
    94,
    74,
    name="Hasnain",
    course = "BCA",
    semester = 5
)