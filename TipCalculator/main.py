# Intro
import random


CRED = '\033[91m'
CEND = '\033[0m'


def return_currency(val):
    return "${:,.2f}".format(val)


def convert_y_to_bool(val):
    if val == 'y':
        return True
    else:
        return False


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def is_interger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def amount_is_zero(amt):
    if float(amt) == 0:
        return True
    else:
        return False


def less_than(amt, check):
    if float(amt) < check:
        return True
    else:
        return False


def greater_than(amt, check):
    if float(amt) > check:
        return True
    else:
        return False


def less_than_message(suggestion, special_char):
    list_of_names = ["Champ", "McDuck", "Penny Squeezer", "Cheapskate", "Hoss", "Tiger", "Frugal McDugal", "Ebenezer", "Stingy Stan"]
    dollarsign = ''
    percentsign = ''
    if special_char == '$':
        dollarsign = '$'
    if special_char == '%':
        percentsign = '%'
    name = random.choice(list_of_names)
    return CRED+'Kind of a dick move, ' + name + '.' + CEND +' Would you like to reconsider? Maybe something higher than ' + dollarsign + str(suggestion) + percentsign + '?\nEnter "y" to adjust the amount, or click Enter to continue.\n'

def print_error(mystr):
    print(CRED + str(mystr) + CEND)

# create some variables we'll need
float_check_error = 'Please enter a whole number (example: "23"), or a float (example: "23.99")'
int_check_error = 'Please enter a whole number (example: "23")'
tip_too_low = '\n\nYour total tip is less than $5.00.\nRegardless of the total bill, please be considerate of service workers who are\nworking very hard to give you the creature comforts you\'re enjoying...'
bill_split = False
tip_split = False
tip_lang = ''
bill_lang = ''
grand_total = ''
tip_warn = ''
the_math = ''

# Start script
print("Hey! You need help with your tip? I'll help you figure it out!")

# ask for bill amount
answered = False
while not answered:
    total_bill = input("What is the total amount?\n")
    if isfloat(total_bill):
        total_bill = float(total_bill)
        answered = True
        break
    else:
        print_error(float_check_error)

# ask if percent, difference, add
answered = False
while not answered:
    tip_type = input("Will this be:\na: Percent of the total\nb: Adding to total\nc: the difference between the bill and a higher number\n")
    if tip_type not in ['a', 'b', 'c']:
        print(CRED+'You must select "a", "b", or "c"'+CEND)
    else:
        answered = True
        break

# if percent
if tip_type == 'a':
    answered = False
    while not answered:
        percent_of_bill = input("What percent would you like to tip? Enter number only\n")
        if is_interger(percent_of_bill) and int(percent_of_bill) > 0:
            if less_than(percent_of_bill, 10):
                reconsider = input(less_than_message(10, "%"))
                if not reconsider == 'y':
                    percent_of_bill = int(percent_of_bill)
                    answered = True
                    break
            else:
                answered = True
                break
        else:
            print_error(int_check_error + "\n** ZERO IS NOT ALLOWED **")

# if add
elif tip_type == 'b':
    answered = False
    while not answered:
        add_to_bill = input("What amount would you like to add to your total? Enter number only\n")
        if isfloat(add_to_bill):
            if less_than(add_to_bill, 5):
                reconsider = input(less_than_message(5, "$"))
                if not reconsider == 'y':
                    add_to_bill = float(add_to_bill)
                    answered = True
                    break
            else:
                answered = True
                break
        else:
            print_error(float_check_error)

# if difference
elif tip_type == 'c':
    answered = False
    while not answered:
        greater_than_bill = input("Please enter an amount greater that the bill total: " + str(total_bill) + "?\n")
        if isfloat(greater_than_bill):
            if greater_than(float(greater_than_bill), total_bill):
                greater_than_bill = float(greater_than_bill)
                answered = True
                break
        else:
            print_error(float_check_error)

# splitting options
# splitting tip
split_option_tip = input("Would You like to split the tip? Please answer 'y' for yes or any other key for no.\n")
split_option_tip = convert_y_to_bool(split_option_tip)
if split_option_tip:
    answered = False
    while not answered:
        tip_split = input("How many ways would you like to split the tip?\nWhole numbers only and 0 is not allowed.\n")
        if is_interger(tip_split) and int(tip_split) > 0:
            tip_split = int(tip_split)
            answered = True
            break
        else:
            print_error(int_check_error + "\n** ZERO IS NOT ALLOWED **")

# splitting bill
split_option_bill = input("Would You like to split the bill? Please answer 'y' for yes or any other key for no.\n")
split_option_bill = convert_y_to_bool(split_option_bill)
if split_option_bill:
    answered = False
    while not answered:
        bill_split = input("How many ways would you like to split the bill?\nWhole numbers only and 0 is not allowed.\n")
        if is_interger(bill_split) and int(bill_split) > 0:
            bill_split = int(bill_split)
            answered = True
            break
        else:
            print_error(int_check_error + "\n** ZERO IS NOT ALLOWED **")

# Do Calculations
# percent calc
if tip_type == 'a':
    tip = (total_bill * int(percent_of_bill))/100
    the_math = 'Percent: ' + return_currency(total_bill) + " * " + str(percent_of_bill) + ' / 100 = ' + return_currency(tip)
    if less_than(tip, 5):
        tip_warn = tip_too_low

# add to calc
if tip_type == 'b':
    tip = int(add_to_bill)
    the_math = 'Adding to bill: $' + add_to_bill + ". This function is really just used to get a total + tip = grand total for credit card receipts."
    if less_than(tip, 5):
        tip_warn = tip_too_low

# difference of calc
if tip_type == 'c':
    tip = float(greater_than_bill) - float(total_bill)
    the_math = 'Difference: ' + str(return_currency(float(greater_than_bill))) + ' - ' + str(return_currency(float(total_bill))) + ' = ' + str(return_currency(tip)) + '.'
    if less_than(tip, 5):
        tip_warn = tip_too_low

# splitting calc
# tip split calc
if tip_split and tip_split > 0:
    split_tip = tip / tip_split
    tip_lang = "The original " + str(return_currency(tip)) + " tip was split by " + str(tip_split) + "\nYou now owe " + str(return_currency(split_tip) + ".")
else:
    tip_lang = 'Your calculated tip is: ' + str(return_currency(tip)) + "."

# bill split calc
if bill_split and bill_split > 0:
    split_bill = total_bill / bill_split
    bill_lang = 'The original ' + return_currency(total_bill) + ' bill was split by ' + str(bill_split) + '\nYou now owe ' + return_currency(split_bill) + '.'
else:
    bill_lang = 'Your bill is ' + return_currency(total_bill) + '.'

# grand total calc
grand_total = 'Your grand total is ' + return_currency(total_bill + tip) + '. This reflects the FULL bill total + the FULL tip amount regardless of splitting.'

# print results
print(the_math)
print(tip_lang)
print(bill_lang)
print(grand_total)
print(CRED + tip_warn.upper() + CEND)

