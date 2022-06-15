from validate_email import validate_email
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


def my_input(text, restrictions=[]):
    filtered = False
    input_res = ''
    while not filtered:
        input_res = input(text).strip()
        input_res_lower = input_res.lower()
        if input_res_lower == '':
            print("\nYou didn't enter any text.\n")
        elif len(restrictions) > 0:
            if input_res_lower not in restrictions:
                print(f'\nAnswers are restricted to the following: {restrictions}.\n')
            else:
                filtered = True
                break
        else:
            filtered = True
            break
    return input_res


data_manager = DataManager()


working = True
while working:
    first_name = my_input("Please enter your first name.").strip().lower().title()
    print(f"User entered: {first_name}.")
    last_name = my_input("Please enter your last name.").strip().lower().title()
    print(f"User entered: {last_name}.")
    email_entry = my_input("Please enter your email.").strip().lower()
    print(f"User entered: {email_entry}.")
    email_entry2 = my_input("Please enter your email again.").strip().lower()
    print(f"User entered: {email_entry2}.")
    if email_entry == email_entry2:
        if validate_email(email_entry):
            if data_manager.user_email_available(email_entry):
                data_manager.add_user(first_name, last_name, email_entry)

                print(f"{email_entry} has been added to our mailing list!")
                working = False
                break
            else:
                print("That email is already registered.")
                working = False
                break
        else:
            print("Please enter a valid email.")
    else:
        print("User entered emails that don't match.")
