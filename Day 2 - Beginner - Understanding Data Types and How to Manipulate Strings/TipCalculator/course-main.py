# TODO If the bill was $150.00, split between 5 people, with 12% tip.
# TODO Each person should pay (150.00 / 5) * 1.12 = 33.6
# TODO Format the result to 2 decimal places = 33.60
# TODO Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# TODO Write your code below this line 👇
print('Welcome to the tip calculator!')
bill = float(input("What was the total bill? $").replace('$',''))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
print(f'Each person should pay: {"${:,.2f}".format((tip / 100 * bill + bill) / people)}')