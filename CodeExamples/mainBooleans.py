done = "beau"

print(type(done) == bool)

if done:
    print("yes")
else:
    print("no")

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])