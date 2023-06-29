# This program calculates and displays travel expenses
# 6/25/2023
# CTI-110 P2HW1 - Travel
# Kristopher Williams
#


print("This program calculates and displays travel expenses")
print()
budget = int(input("Enter Budget: "))
print()
travel = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
hotel = int(input("Approximately, how much will you need for accomdation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
print()
print("-"*12,"Travel Expenses", "-"*13)
print("Location:                    " +  travel)
print("Initial Budget:              $" + str(format(budget,',.1f')))
print()
print("Fuel Budget:               $" + format(gas,',.1f'))
print("Accomodation:           $" + format(hotel,',.1f'))
print("Food:                         $" + format(food,',.1f'))
print()
balance = budget - (gas + hotel + food)
print("-"*50)
print("Remaing Balance:       $" + format(balance,',.1f'))

