students = [
    {"name": "Hasnain", "marks": 85},
    {"name": "Ali", "marks": 92},
    {"name": "Ahmed", "marks": 67},
    {"name": "Sara", "marks": 78},
    {"name": "John", "marks": 55}
]

result = filter(lambda items: items["marks"]>=80,students)
print(list(result))