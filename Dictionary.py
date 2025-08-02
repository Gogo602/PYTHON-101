
person = {
    "name": "Gogo",
    "twitter": "gogomarosi",
    "balance": 25000,
    "interest": 380,
    "Due": 30
}
print(person)

# add new item to the dictionary
person["otherName"] = "Marosi"
print(person)

# delete item from the dictionary
del person["otherName"]

print(person)

# multiply the inteest with the date and store it in debt
debt = person["interest"] * person['Due']

print(debt)

# add dept to the person dictionary
person["Debt"] = debt

print(person)

# nameUp = person["otherName"].upper()
 
# print(nameUp)
