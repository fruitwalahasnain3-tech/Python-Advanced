marks = [45, 60, 72, 81, 94]
map_bonus = map(lambda x : x+5 , marks)
print(list(map_bonus))



# Tax
tax = [12000,11419,44451,55860]
tax_add = map(lambda x:(x*0.18) + x , tax)
print(list(tax_add))