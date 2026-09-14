students = {
    "Hasnain": 85,
    "Ali": 92,
    "Ahmed": 67,
    "Sara": 78,
    "John": 55
}

result = filter(lambda items: items[1] >= 70 ,students.items() )

print(list(result))