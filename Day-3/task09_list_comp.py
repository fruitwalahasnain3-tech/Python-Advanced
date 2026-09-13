marks = [45, 78, 92, 61, 88, 34, 95, 72]

grade = [
    "A" if i >= 90
    else "B" if i >= 80
    else "C" if i >= 70
    else "D" if i >= 60
    else "F"
    for i in marks
]
print(grade)