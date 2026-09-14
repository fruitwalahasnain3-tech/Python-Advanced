numbers = [12, 25, 30, 45, 50, 63, 70, 81, 90]

result = filter(lambda x: x>30 and x%5 == 0  , numbers)

print(list(result))