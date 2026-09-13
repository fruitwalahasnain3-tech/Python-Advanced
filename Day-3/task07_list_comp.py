numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new = [i*i if i %2==0 else i*3 for i in numbers]
print(new)

# 📒 Important note

# Don't confuse these two patterns:

# Filtering:

# [i for i in numbers if i % 2 == 0]

# Conditional transformation:

# [i*i if i % 2 == 0 else i*3 for i in numbers]

# The first removes values that don't satisfy the condition.

# The second keeps every value, but changes it differently depending on the condition.