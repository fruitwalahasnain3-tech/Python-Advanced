def mark(x):
    return x>=70
marks = [45, 67, 82, 91, 56, 74, 38, 88]

result=filter(mark,marks)
print(list(result))