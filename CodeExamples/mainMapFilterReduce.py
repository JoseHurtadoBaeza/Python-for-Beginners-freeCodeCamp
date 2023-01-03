# map(), filter(), reduce()

# Map Example
numbers = [1, 2, 3]

"""def double(a):
    return a * 2"""

#double = lambda a : a * 2

##result = map(double, numbers)

result = map(lambda a : a * 2, numbers)

print(list(result))

# Filter Example

numbers = [1, 2, 3, 4, 5, 6]

"""def isEven(n):
    return n % 2 == 0"""

#result = filter(isEven, numbers)

result = filter(lambda n : n % 2 == 0, numbers)

print(list(result))

# Reduce Example

from functools import reduce

expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

"""sum = 0
for expense in expenses:
    sum += expense[1]"""

sum = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum)