import requests
import random
import json
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import time
from faker import Faker


def reqMyData(url):
    r = requests.get(url=url)
    data = r.json()
    return data


def pause(t=1):
    time.sleep(t)


# set some data variables
fake = Faker()
random_info_url = "https://hiveword.com/papi/random/"
for_the_best_text = 'Probably for the best. Good bye.'
promtDefault_text = 'Type "y", then hit Enter to continue, or just hit Enter to quit'
# location_url_country should be "" to have any random country
location_url = "locationNames?"
location_url_country = "country=US"
# call the random data API to get location
loc_data = reqMyData(random_info_url + location_url + location_url_country)[0]
death_location = f'{loc_data["name"]}, {loc_data["state"]}, {loc_data["country"]}'
# call the random data API to get person
killer = fake.first_name()
date_format = "%m/%d/%Y"
cause_of_death = random.choice(json.load(open('crystalBall.json'))['deaths'])
# to date calculation it's a random date between 4 months from now, and ten years from now.
death_date = fake.date_between(start_date='+4m', end_date='+10y')
diff = relativedelta(death_date, datetime.now())

# THE APP
print("Hello. I'm Baba Zolfar, and I have only one desire.")
pause(1)
print("To ruin your day, by telling you when you expire!")
pause(3)
print("Come, shiver in terror, let me see tears in your eyes!")
pause(1)
print("Tell me child... do you want to know when you die?")
pause(2)
print()
q = input(promtDefault_text + ' while you\'re ahead?\n')
if q != 'y':
    print()
    print(for_the_best_text)
    print()
else:
    print()
    print(f'You have {diff.years} years, {diff.months} months, {diff.weeks} weeks, {diff.days} days left.')
    pause(2)
    print('You know...')
    pause(2)
    print('To get your affairs in order')
    pause()
    print('and...')
    pause(2)
    print("I don't know, pet your pet or whatever it is hoomans do...")
    pause(3)
    print(f"Because on {death_date.strftime(date_format)} YER DONE!")
    print()
    pause(3)
    print('Do you want to know how you die?')
    q = input(promtDefault_text + ' before it gets worse.')
    if q != 'y':
        print()
        print(for_the_best_text)
        print()
    else:
        print()
        print(cause_of_death)
        print()
        pause(3)
        print('Do you want to know who you are going to be with?')
        q = input(promtDefault_text + ', seriously kid, no one will judge you')
        if q != 'y':
            print()
            print(for_the_best_text)
            print()
        else:
            print()
            print(killer)
            print()
            pause(3)
            print('Do you want to know what it all means?')
            q = input(promtDefault_text)
            if q != 'y':
                print()
                print(for_the_best_text)
                print()
            else:
                print()
                print("Don't we all, buddy?")
                pause()
                print("Don't we all...")
                pause(3)
                print("Till next time")
                pause()
                print("I've been Baba Zolfar,")
                pause(3)
                print("and you've been wasting what precious time you have left!")
