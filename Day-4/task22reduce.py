from functools import reduce

prices = [1200, 800, 2500, 450, 1000]

result = reduce(lambda x,y : x+y , prices)
print(result)