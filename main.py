# Assignment 4 
# Name: Farzana jafary
# Description:
# This program allows the user to choose an Afghan sweet, pay using 100 AFN banknotes,
# and calculates the change using Afghani currency denominations.

print("Select a sweet to purchase:")
print("a) Shir Pira for 160 AFS")
print("b) Kulcha for 120 AFS")
print("c) Gosh-e-Feel for 210 AFS")
print("d) Baklava for 350 AFS")

# Get user input
choice = input("What item do you want? ")

# Allow uppercase or lowercase
choice = choice.lower()

# Branching for item selection
if choice == "a":
    item = "Shir Pira"
    cost = 160
elif choice == "b":
    item = "Kulcha"
    cost = 120
elif choice == "c":
    item = "Gosh-e-Feel"
    cost = 210
elif choice == "d":
    item = "Baklava"
    cost = 350
else:
    print("Invalid choice entered.")
    item = "Kulcha"
    cost = 120
    print("The item selected is Kulcha.")

# Ask for payment in 100 AFN banknotes
banknotes = int(input("Pay with 100 AFN banknotes. How many? "))
payment = banknotes * 100

print(f"Cost is {cost} AFS")
print(f"Payment is {payment} AFS")

# Check if enough payment
if payment < cost:
    print(f"You did not pay enough money and will not receive the {item}")
else:
    # Calculate change
    change = payment - cost
    
    print(f"You purchased the {item}")
    print(f"Your change is {change} AFS")

    # Calculate breakdown of change
    fifty = change // 50
    change %= 50

    twenty = change // 20
    change %= 20

    ten = change // 10
    change %= 10

    five = change // 5
    change %= 5

    one = change

    # Print results
    print("Number of 50 AFN:", fifty)
    print("Number of 20 AFN:", twenty)
    print("Number of 10 AFN:", ten)
    print("Number of 5 AFN:", five)
    print("Number of 1 AFN:", one)
