import random
random.seed(2)

die1 = 0
die2 = 0
dice_sum = 0
twos = ''
threes = ''
fours = ''
fives = ''
sixes = ''
sevens = ''
eights = ''
nines = ''
tens = ''
elevens = ''
twelves = ''

for i in range(100):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice_sum = die1 + die2
    if dice_sum == 2:
        twos = twos + '*'
    elif dice_sum == 3:
        threes = threes + '*'
    elif dice_sum == 4:
        fours = fours + '*'
    elif dice_sum == 5:
        fives = fives + '*'
    elif dice_sum == 6:
        sixes = sixes + '*'
    elif dice_sum == 7:
        sevens = sevens + '*'
    elif dice_sum == 8:
        eights = eights + '*'
    elif dice_sum == 9:
        nines = nines + '*'
    elif dice_sum == 10:
        tens = tens + '*'
    elif dice_sum == 11:
        elevens = elevens + '*'
    elif dice_sum == 12:
        twelves = twelves + '*'

print("2s: %s" % twos)
print("3s: %s" % threes)
print("4s: %s" % fours)
print("5s: %s" % fives)
print("6s: %s" % sixes)
print("7s: %s" % sevens)
print("8s: %s" % eights)
print("9s: %s" % nines)
print("10s: %s" % tens)
print("11s: %s" % elevens)
print("12s: %s" % twelves)
