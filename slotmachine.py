import random  # import the random module
random.seed(2)  # dictates random sequence

# Variables for holding the numbers
user_play = 'y'

while user_play == 'y':
    print("Python Slot Machine")
    first_num = random.randint(0, 9)
    second_num = random.randint(0, 9)
    third_num = random.randint(0, 9)
    print("%d %d %d" % (first_num, second_num, third_num))
    if first_num == second_num and second_num == third_num:
        print("Jackpot!!!")
    elif first_num == second_num or first_num == third_num or second_num == third_num:
        print("Matched 2!!")
    else:
        print("Sorry you lost!")
    user_play = input("Play again (y)?:")

print("Thanks for playing!")
