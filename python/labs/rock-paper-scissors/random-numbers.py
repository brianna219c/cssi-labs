import random

print("Welcome to Bri's random playground!")

die1 = random.randint(1,6)
die2 = random.randint(1,6)

sum = die1 + die2

if die1 == die2:
    print("Move up: %s spaces, roll again!" % (sum))


else:
    print("Move up: %s spaces, Next players turn!" % (sum))
