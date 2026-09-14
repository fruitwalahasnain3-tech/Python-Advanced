from functools import reduce

def multi(x,y):
    return x*y

numbers = [2, 3, 4, 5]

result = reduce(multi,numbers)

print(result)