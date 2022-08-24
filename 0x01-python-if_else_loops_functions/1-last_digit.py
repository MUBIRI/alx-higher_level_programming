#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last digit = number % 10
else:
    last digit = ((number * -1) % 10)
if last digit > 5:
    print(f"last digit of {number} is {last digit} and is greater than 5")
elif last digit == 0:
    print(f"last digit of {number} is {last digit} and is 0")
else:
    print(f"last digit of {number} is {last digit} and is less than 6 and not 0")
