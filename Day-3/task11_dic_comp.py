students = {
    "Hasnain": 85,
    "Ali": 92,
    "Ahmed": 67,
    "Sara": 78
}

dic = {key:value for key, value in students.items() if value>70}
print(dic)