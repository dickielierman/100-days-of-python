year = int(input('Year: '))

def divisible_by(val, check):

    if val % check == 0:
        return True
    else:
        return False
if divisible_by(year, 4) == True:
    if divisible_by(year, 100) == True:
        if divisible_by(year, 400) == True:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")