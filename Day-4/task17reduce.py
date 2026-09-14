from functools import reduce

def add(x,y):
    return x+y

numbers = [10, 20, 30, 40, 50]

result= reduce(add,numbers)

print(result)