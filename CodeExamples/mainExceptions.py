# Exceptions

"""result = 2 / 0
print(result)"""

"""try:
    # some lines of code
except <ERROR1>:
    # handler <ERROR1>
except <ERROR2>:
    # handler <ERROR2>
else:
    # no exceptions were raised, the code ran succesfully
finally:
    # do something in any case"""

"""try:
    # some lines of code
except EOFError:
    # handler <ERROR1>
except <ERROR2>:
    # handler <ERROR2>
else:
    # no exceptions were raised, the code ran succesfully
finally:
    # do something in any case"""

"""try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')
finally:
    result = 1

print(result) # 1"""

"""try:
    raise Exception('An error!')
except Exception as error:
    print(error)"""

class DogNotFoundException(Exception):
    print("inside")
    pass 

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found!')