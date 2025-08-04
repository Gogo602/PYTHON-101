# Iterating over iterable object

fav_foods = ["Pizza", "MoiMoi", "Salmon"]

for food in fav_foods:
    print(f"My favourite food is {food}")


food = "Pizza"
for letter in food:
    print(letter)


# looping through dictionary

person = {
    "name": "Gogo",
    "twitter": "gogomarosi",
    "linkedln": "gogobenson"
}

for key, value in person.items():
    print(value)