# Final Project
# Name: Farzana Jafary
# Description: Coffee shop program that lets the user order drinks,
#              including mystery items, and applies a discount.

import random

# lists for items and costs
items = ["latte", "espresso", "cappuccino", "matcha", "chai"]
costs = [130, 90, 70, 100, 50]

total_cost = 0
discountableAmount = 20.0
discountPercent = 20

print("Welcome to my Coffee Shop!\n")

# print menu using range loop
print("Menu:")
for i in range(len(items)):
    print("\t" + items[i].capitalize() + ":\t" + str(costs[i]))

print()

# main loop
choice = input('Enter an item OR Enter "M" for mystery item OR Enter "Done": ')

while choice.lower() != "done":

    # MYSTERY ITEM
    if choice.lower() == "m":
        mystery = random.choice(items)
        print("\nYour mystery item is:", mystery)

        buy = input("Do you wish to purchase it? Y/N: ")

        while buy.lower() not in ["y", "n"]:
            buy = input("Do you wish to purchase it? Y/N: ")

        if buy.lower() == "y":
            idx = items.index(mystery)
            total_cost += costs[idx]
            print("1", mystery, "- Got it! That's", costs[idx], "AFS\n")
        else:
            print("OK, skipping this mystery item!\n")

    # MENU ITEM
    elif choice.lower() in items:
        amount = input(f"How many {choice.lower()} do you want? (1 or more): ")

        # validate amount
        while not amount.isdigit() or int(amount) < 1:
            amount = input(f"How many {choice.lower()} do you want? (1 or more): ")

        amount = int(amount)

        item_index = items.index(choice.lower())
        item_cost = costs[item_index] * amount
        total_cost += item_cost

        print(f"{amount} {choice.lower()} - Got it! That's {item_cost} AFS\n")

    # INVALID INPUT
    else:
        print("Invalid item!\n")

    # show menu again
    print("Want More? Here's the Menu again -\n")
    print("Menu:")
    for i in range(len(items)):
        print("\t" + items[i].capitalize() + ":\t" + str(costs[i]))
    print()

    # ask again
    choice = input('Enter an item OR Enter "M" for mystery item OR Enter "Done": ')

# After DONE
print()

if total_cost == 0:
    print("You didn't buy anything.")
else:
    # discount
    if total_cost > discountableAmount:
        print(f"Your total cost is more than {discountableAmount} AFS.")
        print(f"Congratulations, you receive a {discountPercent}% discount!")
        discount_value = (discountPercent / 100) * total_cost
        total_cost = total_cost - discount_value

    print("Your total cost is:", total_cost)

print("\nThank you for shopping here!")