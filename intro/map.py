def add_five(x):
    return x + 1

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

#lambda
result = list(map(lambda x: x+1, nums))
print(result)