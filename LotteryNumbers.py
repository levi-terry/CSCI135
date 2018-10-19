import random
import datetime
random.seed(datetime.datetime.now())

number1 = random.randint(1, 70)
number2 = random.randint(1, 70)
number3 = random.randint(1, 70)
number4 = random.randint(1, 70)
number5 = random.randint(1, 70)
powerball = random.randint(1, 25)
while number2 == number1:
    number2 = random.randint(1, 70)
while number3 == number2 or number3 == number1:
    number3 = random.randint(1, 70)
while number4 == number3 or number4 == number2 or number4 == number1:
    number4 = random.randint(1, 70)
while number5 == number4 or number5 == number3 or number5 == number2 or number5 == number1:
    number5 = random.randint(1, 70)

print("Here are your lucky numbers:")
print(number1)
print(number2)
print(number3)
print(number4)
print(number5)
print(powerball)
