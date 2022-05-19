
# Hurdle 1
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# this was my solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for i in range(6):
    jump()

# Hurdle 2
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# this was my solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    jump()


# Hurdle 3
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# this was my solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    while front_is_clear() and not at_goal():
        move()
    if not at_goal():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
while not at_goal():
    jump()


# Hurdle 4
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# this was my solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    while front_is_clear() and not at_goal():
        move()
    if not at_goal():
        turn_left()
        while not right_is_clear():
            move()
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()
while not at_goal():
    jump()

# The maze
#  https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# this was my solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def work_the_maze():
    if not wall_on_right():
        turn_right()
    if front_is_clear():
        move()
    else:
        turn_left()
while front_is_clear():
    move()
turn_left()
while not at_goal():
    work_the_maze()