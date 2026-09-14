from functools import reduce

prices = [500, 1200, 800, 2500, 3000, 700, 1500]

result = filter(lambda x: x>=1000 , prices)
result = map(lambda x: x*(-0.10) + x, list(result))
result = reduce(lambda x,y : x+y , result)
print(result)