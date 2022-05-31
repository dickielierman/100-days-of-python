from turtle import *
import pandas
from scoreboard import Scoreboard

screen = Screen()
screen.title('Remember The US States game')
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)
scoreboard = Scoreboard()

file_loc = '50_states.csv'
data = pandas.read_csv(file_loc)
playing = True
while scoreboard.correct_guess_count < scoreboard.total_states and playing:
    cg = scoreboard.correct_guess_count
    ts = scoreboard.total_states
    state_list = data.state.to_list()
    answer = textinput(title=f"{cg}/{ts} states remembered", prompt='Can you remember more of them?').lower().title()
    if answer == 'Exit':
        missed_states = []
        for state in state_list:
            if state not in scoreboard.correct_guesses:
                missed_states.append(state)
        pandas.DataFrame({"States To Learn": missed_states}).to_csv('states_to_learn.csv')
        playing = False
    if answer in state_list:
        d = data[data.state == answer]
        scoreboard.add_state(d.state.item(), int(d.x), int(d.y))

screen.exitonclick()