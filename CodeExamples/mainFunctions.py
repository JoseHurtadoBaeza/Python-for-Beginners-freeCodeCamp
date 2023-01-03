# Functions 

"""def hello(name, age):
    print("Hello " + name + ", you are" + str(age) + " years old!")

hello("Beau", 39)"""

def change(value):
    value["name"] = "Syd"

val = {"name": "beau"}
change(val)

print(val)

def hello(name):
    print('Hello ' + name + '!')
    return name, "Beau", 8

print(hello("Syd"))
