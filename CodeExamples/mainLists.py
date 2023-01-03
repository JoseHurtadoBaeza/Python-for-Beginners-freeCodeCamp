#dogs = []
dogs = ["Roger", 1, "Syd", True, "Quincy", 7]

print("Roger" in dogs)
print("Beau" in dogs)

dogs[2] = "Beau"
dogs.append("Judah")
dogs.extend(["Jose", 23])
dogs += ["Carlos", 15]

dogs.remove("Syd")
dogs.remove("Quincy")

print(dogs)
print(dogs[0])
print(dogs[-1])
print(dogs[-2])
print(dogs[2:4])
print(dogs[:3])
print(len(dogs))
print(dogs.pop())

items = ["Roger", 1, "Syd", True, "Quincy", 7]

items.insert(2, "Test")
items[1:1] = ["Test1", "Test2"]

print(items)