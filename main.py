from functools import reduce

numbers = [300, 2]
result = reduce(lambda x, y: x * y, numbers)
print(result)
