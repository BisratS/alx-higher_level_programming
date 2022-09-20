#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    lD = number % 10
else:
    lD = number % -10

print(f"Last digit of {number} is {lD}", end="")

if lD > 5:
    print(" and is greater than 5")
elif lD == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
