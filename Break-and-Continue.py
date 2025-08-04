# breaking out a loop or bypassing the loop entirely

items = ['one', 'two', 'three', 'four', 'five']

# using continue. skip the items 
for item in items:
    if item == "two" or item == "four":
        continue
    print(item)

# using break. automatically breakout of the loop when its get to the specified item
for item in items:
    if item == "three":
        break
    print(item)

# with while loop
# odd numbers
num = 0
while num <= 20:
    num += 1
    if num % 2 == 0:
        continue
    print(num)

# even numbers
even = 0
while even <= 20:
    even += 1
    if even % 2 == 1:
        continue
    print(even)


# break
num1 = 0 
while num1 <= 1000:
    num1 += 1
    if num1 == 13:
        break
    print(num1)