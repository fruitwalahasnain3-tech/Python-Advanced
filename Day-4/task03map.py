def cube(x):
    return x*x*x

numbers = [3, 5, 7, 9]

result = map(cube, numbers)

print(list(result))