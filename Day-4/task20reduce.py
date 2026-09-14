from functools import reduce

numbers = [45, 82, 17, 96, 54, 73]

result = reduce(lambda x,y: x if x > y else y, numbers)
print(result)