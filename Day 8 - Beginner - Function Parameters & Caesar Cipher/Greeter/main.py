def greet():
    print("Hello.")
    print("I'm your greeter.")
    print("You've been greeted.")


def greet_with_input(val):
    print(f'Hello, {val}')
    print(f"I'm your greeter, {val}.")
    print("What a coincidence that we share the same name!.")


def function_with_params(params):
    print(f'Hello, {params["name"]}')
    print(f'What is it like in {params["location"]}?')
    if "dob" in params:
        print(f"DOB: {params['dob']}")


function_with_params({"name": 'Tim', "location": "Chattanooga"})
