def odd():
    for i in range(1, 100):
        if i % 2 != 0:
            print(i, end=' ')
        if i % 20 == 0:
            print()
    print("\n")


def threes():
    counter = 1
    for i in range(303, 2, -3):
        print(i, end=' ')
        counter += 1
        if counter % 6 == 0:
            print()
    print()


def listave(list):
    total = 0
    for x in list:
        total += x
    return total / (len(list))


def revstr(str):
    return reversed(str)


if __name__ == '__main__':
    menu_selection = 1

    while menu_selection != 5:
        print("Select operation.")
        print("1. Print odd numbers from 1 to 99 inclusive")
        print("2. Print multiples of 3 from 303 down to 3")
        print("3. Read integer values from user (q to quit) and print the average")
        print("4. Read a string from the user and print it backwards")
        print("5. Quit")
        menu_selection = int(input("Enter choice (1/2/3/4/5):"))
        print()

        if menu_selection == 1:
            odd()
            continue
        elif menu_selection == 2:
            threes()
            continue
        elif menu_selection == 3:
            avglist = []
            userinput = 0
            while userinput != 'q':
                try:
                    userinput = int(input("Enter integer (q to quit):"))
                    avglist.append(userinput)
                except ValueError:
                    break
            print()
            print(listave(avglist))
            print()
            continue
        elif menu_selection == 4:
            print(revstr(input("Enter string: ")))
            continue
        elif menu_selection == 5:
            break
        else:
            print("Invalid input")
            print()
            continue
