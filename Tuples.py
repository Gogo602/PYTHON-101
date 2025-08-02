# Tuple is Immutable, meaning it cant be modified

# this is a list
animals = ["cat", "Dog", "Zebra", "Aardvaark"]
# this reverse the other of the items in the list
animals.sort()
print(animals)

# now this is a Tuple: It uses regular bracket() instead of angle bracket[]
foods = ("garri", "Beans", "Rice", "Soup",)

for food in foods:
    print(f"The food is: {food}")

# we cant modified it further as no attributes coes with it so it doesnot change all through the program