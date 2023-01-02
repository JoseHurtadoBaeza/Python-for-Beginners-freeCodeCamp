# Dictionaries

dog = {"name": "Roger", "age": 8, "color": "green"}

#dog["name"] = "Syd"

"""print(dog.get("name"))
print(dog.get("color", "brown"))
print(dog.pop("name"))
print(dog.popitem())
print(dog)"""

print("color" in dog)
print(dog.keys())
print(list(dog.keys()))
print(dog.values())
print(dog.items())

dog["favorite food"] = "Meat"

del dog['color']

dogCopy = dog.copy()

print(len(dog))