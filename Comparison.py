# Comparison in Python

# 1
teacher = "Kalob Taulien"

if teacher == "Kalob Taulien":
    print("Show Teacher Portal")
else:
    print("You are a student. welcome to Python 101") 

# 2 
name = input("What is your name: ")

if name == "Bob":
    print("welcome Bob")
    bring_food = "garri"
elif name == "Gogo":
    print("Welcome Gogo")
    bring_food = "You too like food"
else:
    print("You are not Bob, get outta here")
    bring_food = "Indomie"
print(f"You are eating: {bring_food}")


# 3
age = 17
if age > 18:
    print("You can vote")
elif age < 18:
    print("you are not allowed to vote")
else:
    print("enter a valid age")

# 4
if age >= 17:
    print("Start doing something meaningful with your life")
else:
    print("You are still a kid")

# 5
if age <= 17:
    print("learn Coding")
else:
    print("You messed up your early age")

# 6
if age != 18:
    print("You are not allowed to join 500 meters race")
else:
    print("Join the lineup")




