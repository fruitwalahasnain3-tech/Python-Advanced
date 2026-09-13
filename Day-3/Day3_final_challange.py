students = {
    "Hasnain": 85,
    "Ali": 92,
    "Ahmed": 67,
    "Sara": 78,
    "John": 55
}

new_dic = {key:value+5 for key,value in students.items() if value >= 70}
print(new_dic)