products = {
    "Laptop": 60000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500
}

result = filter(lambda items: items[1] < 3000 , products.items())
print(list(result))