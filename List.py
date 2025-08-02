
# always remember list is mutable in the sense that it can be modified

# import modules for maths operations
from functools import reduce
from operator import mul
from operator import add 
from operator import sub

# a list is basics

lst = [1, 2, 3, 4]
lst.append(5)

# mathematical operations on lst
addLst = reduce(add, lst)
mulLst = reduce(mul, lst)
subLst = reduce(sub, lst)
print(addLst, mulLst, subLst)

few = lst.copy()
print(few)

print(lst)
print(type(lst))
 

addTotal = 0
subTotal = lst[0]
multiTotal = 1
for item in lst[1:]:
    addTotal += item
    subTotal -= item
    multiTotal *= item
print(addTotal)
print(subTotal)
print(multiTotal)