from functools import reduce

numbers = [5, 10, 15, 20]

result = reduce(lambda x,y: x+y, numbers)

print(result)