names = ["Hasnain", "Ali", "Ahmed", "Sara", "John", "Alexander"]

result = filter(lambda x: len(x) > 4,names)

print(list(result))