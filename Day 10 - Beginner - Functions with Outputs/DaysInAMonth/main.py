# Instructions
# In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.
#
# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
#
# days_in_month(year=2022, month=2)
# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:
#
# 28
# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.
#
# Hint
# Look at the function call at the bottom of the code to see the positional arguments. The order is very important.
#
# Feel free to choose your own parameter names.
#
# Remember that month_days is a List and Lists in Python start at position 0. So the number of days in January is month_days[0]
#
# Be careful with indentation.

# def my_input(text, restrictions=[]):
#     filtered = False
#     input_res = ''
#     while not filtered:
#         input_res = input(text).strip()
#         input_res_lower = input_res.lower()
#         if input_res_lower == '':
#             print("\nYou didn't enter any text.\n")
#         elif len(restrictions) > 0:
#             if input_res_lower not in restrictions:
#                 print(f'\nAnswers are restricted to the following: {restrictions}.\n')
#             else:
#                 filtered = True
#                 break
#         else:
#             filtered = True
#             break
#     return input_res


def is_leap(year):
    """Return True/False if year argument is a leap year"""
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap


def days_in_month(year, month):
    """Returns the number of days in the month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        if month == 2:
            return 29
        else:
            return month_days[month - 1]
    else:
        return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
