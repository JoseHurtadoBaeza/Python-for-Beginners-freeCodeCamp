items = ["Roger", "Syd", "Beau", "Quincy"]

items.sort()
print(items)

items = ["Roger", "bob", "Beau", "Quincy"]

itemscopy = items[:]
items.sort(key=str.lower)
print(items)
print(itemscopy)

print(sorted(items, key=str.lower))
print(items)