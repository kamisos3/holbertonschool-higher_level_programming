#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"

if number > 5:
    print(f"{str} {number} is {number} and is greater than 5")
if number == 0:
    print(f"{str} {number} is 0 and is 0")
if number < 6 | number > 0:
    print(f"{str} {number} is {number} and is less than 6 and not 0")
