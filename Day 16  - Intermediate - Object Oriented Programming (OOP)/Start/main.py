from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()
table.field_names = ["Column One", "Column Two", "Column Three", "Column Four"]
table.add_rows([
    ["Adelaide", 1295, 1158259, 600.5],
    ["Brisbane", 5905, 1857594, 1146.4],
    ["Darwin", 112, 120900, 1714.7]
])
print(table)
