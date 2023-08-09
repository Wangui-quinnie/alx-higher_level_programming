#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# To get the last digit use the modulo % operator
if number >= 0:
    last_num = abs(number) % 10
else:
    last_num = abs(number) % -10

if last_num > 5:
    print(F"Last digit of {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(F"Last digit of {number} is {last_num} and is 0")
else:
    print(F"Last digit of {number} is {last_num} and is less than 6 and not 0")
