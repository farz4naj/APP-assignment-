# Assignment 6
# Name: Farzana Jafary
# Description: A simple game using loops where the user picks a case
#              and rolls a D20 to try to win points.

import random

total_points = 0

# play the game 5 times
for round_num in range(5):

    # get the case number
    choice = input("Enter a number (1-5): ")
    choice = int(choice)

    while choice < 1 or choice > 5:
        choice = int(input("Enter a number (1-5): "))

    print(f"You are playing for Case {choice}")
    print("To win, roll one of the following numbers")

    # show winning numbers depending on the case
    if choice == 1:
        # even numbers
        for x in range(2, 21, 2):
            print(x, end=" ")
        print()

    elif choice == 2:
        # odd numbers
        for x in range(1, 20, 2):
            print(x, end=" ")
        print()

    elif choice == 3:
        # 5 to 10
        for x in range(5, 11):
            print(x, end=" ")
        print()

    elif choice == 4:
        # even numbers 10 or more
        for x in range(10, 21, 2):
            print(x, end=" ")
        print()

    else:  # choice == 5
        # multiples of 3
        for x in range(3, 21, 3):
            print(x, end=" ")
        print()

    # roll the dice (D20)
    roll = random.randint(1, 20)
    print(f"\nYou rolled a {roll}")

    won = False   # track if the user wins

    # check conditions
    if choice == 1:
        if roll % 2 == 0:
            won = True

    elif choice == 2:
        if roll % 2 == 1:
            won = True

    elif choice == 3:
        if roll >= 5 and roll <= 10:
            won = True

    elif choice == 4:
        if roll >= 10 and roll % 2 == 0:
            won = True

    elif choice == 5:
        if roll % 3 == 0:
            won = True

    # print result
    if won:
        print("You win 50 points!\n")
        total_points += 50
    else:
        print("You didn't win.\n")

# final result
print(f"Your total score is {total_points} points.")