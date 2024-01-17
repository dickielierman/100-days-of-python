from turtle import Turtle

GRASS_COLOR = "green yellow"
RUNOFF_COLOR = "beige"
ROAD_COLOR = "gainsboro"
ROAD_STRIPE_COLOR = "DarkGoldenrod1"
NUMBER_OF_STRIPES = 5
# We're just grabbing one of these from the list. There's probably a more elegant solution, but I wanted this to be "easy" to change.
LANE_SIZE = ["small", "medium", "large"][1]

if LANE_SIZE == 'large':
    lane_height = 3
    number_of_lanes = 6
elif LANE_SIZE == 'medium':
    lane_height = 2
    number_of_lanes = 8
elif LANE_SIZE == 'small':
    lane_height = 1
    number_of_lanes = 12


class TheRoad(Turtle):
    def __init__(self, game_width, game_height):
        self.width = game_width
        self.height = game_height
        super().__init__()
        self.penup()
        self.shape('square')
        self.goto(-abs(self.width)/2, -abs(self.height)/2)
        self.pensize(10)
        self.pendown()
        for bottom_grass in range(3):
            self.solid_row(GRASS_COLOR)
        for bottom_runoff in range(1):
            self.solid_row(RUNOFF_COLOR)
        for each_lane in range(number_of_lanes - 1):
            for gray_lane in range(lane_height):
                self.solid_row(ROAD_COLOR)
            for yellow_stripes in range(1):
                self.striped_row()
        for top_lane in range(lane_height):
            self.solid_row(ROAD_COLOR)
        for top_runoff in range(1):
            self.solid_row(RUNOFF_COLOR)
        for top_grass in range(3):
            self.solid_row(GRASS_COLOR)

    def solid_row(self, color):
        self.color(color)
        self.forward(self.width)
        self.setheading(90)
        self.forward(10)
        self.setheading(180)
        self.forward(self.width)
        self.setheading(90)
        self.forward(10)
        self.setheading(0)


    def striped_row(self):
        for each_stripe in range(NUMBER_OF_STRIPES):
            stripe = (self.width/NUMBER_OF_STRIPES) / 4 * 3
            road = (self.width / NUMBER_OF_STRIPES) / 4
            self.color(ROAD_STRIPE_COLOR)
            self.forward(stripe)
            self.color(ROAD_COLOR)
            self.forward(road)
            self.color(ROAD_STRIPE_COLOR)
        self.setheading(90)
        self.forward(10)
        self.setheading(180)
        self.color(ROAD_COLOR)
        self.forward(self.width)
        self.setheading(90)
        self.forward(10)
        self.setheading(0)

