# Instructions
# Create a logging_decorator() which is going to log the name of the function that was called, the arguments it was given and finally the returned output.
#
# Expected Output
#
#
# Hints
# You can use function.__name__ to get the name of the function.
# You'll need to use *args
# NOTE: There are no tests for this exercise so that you can create your own functions. Just make sure it does what the video shows.


# Create the logging_decorator() function 👇

def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(type(args))
        print(type(kwargs))
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned: {result}")

    return wrapper

# Use the decorator 👇

@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)

