prices = [100, 250, 500, 750, 1000]

tax = map(lambda x: (x*0.18) + x , prices)

print(list(tax))