def dis(x):
    return (x*(-0.10) + x)

prices = [100, 200, 500, 1000]

result = map(dis,prices)

print(list(result))