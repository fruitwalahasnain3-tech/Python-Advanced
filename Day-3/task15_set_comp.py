numbers = {10, 15, 20, 15, 30, 20, 35, 40, 35}

new = {i for i in numbers if i %2 == 0}

print(sorted(new))