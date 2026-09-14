from functools import reduce

words = ["Python", "is", "very", "powerful"]

result = reduce(lambda x,y : x+" "+y, words)
print(result)