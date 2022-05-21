print('Welcome to the rollercoaster!')
h = int(input('What is your height in cm?'))
if h < 120:
    print("Sorry, you have to be taller to ride this ride.")
else:
    print('You can ride the rollercoster')
    t = 0
    a = int(input('What is your age?'))
    if a < 12:
        t = 5
        print(f'Child tickets are {"${:,.2f}".format(t)}.')
    elif a <= 18:
        t = 7
        print(f'Youth tickets are {"${:,.2f}".format(t)}.')
    elif 45 <= a <= 55:
        print(f'Everything is okay, Have a free ride on us!.')
    else:
        t = 12
        print(f'Adult tickets are {"${:,.2f}".format(t)}.')
    p = input('Do you want a picture for $3 more?\nClick "y" and the Enter for yes, or just click Enter for no.')
    if p == 'y':
        t += 3
    print(f'Your final bill is {"${:,.2f}".format(t)}')
