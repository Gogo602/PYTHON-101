#  Type casting is basically changing a variable from one data type to another

# get user age
age = input("what is your age: ")
# check the data type
data_type = type(age)

# cast age into integer(number)
age = int(age)
# check the data type
data_type = type(age)

print(f"Your age is {age}")

print(f"Your age in Dog years is {age * 7}") 

# list of groceries
grocery_list = ["apple", "pineapple", "crunch", "Mango", "Coconut", "apple"]
# check for type
print(type(grocery_list))

# cast it into tuple so it cant be modified
grocery_list = tuple(grocery_list)
print(grocery_list)
print(type(grocery_list))

# cast it into set so it will be completely unique
grocery_list = set(grocery_list)
print(grocery_list)
print(type(grocery_list))
