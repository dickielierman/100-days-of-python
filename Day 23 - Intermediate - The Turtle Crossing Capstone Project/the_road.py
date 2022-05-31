from turtle import Turtle

class TheRoad(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.goto(-300, -300)
        self.pensize(10)
        self.pendown()
        for bottom_grass in range(3):
            self.color("green yellow")
            self.solid_row()

        for bottom_runoff in range(1):
            self.color("beige")
            self.solid_row()

        for each_lane in range(5):
            self.color("gainsboro")
            for gray_lane in range(3):
                self.solid_row()
            for yellow_stripes in range(1):
                for each_stripe in range(6):
                    self.color("DarkGoldenrod1")
                    self.forward(75)
                    self.color("gainsboro")
                    self.forward(25)
                    self.color("DarkGoldenrod1")
                self.setheading(90)
                self.forward(10)
                self.setheading(180)
                self.color("gainsboro")
                self.forward(600)
                self.setheading(90)
                self.forward(10)
                self.setheading(0)

        for top_lane in range(3):
            self.color("gainsboro")
            self.solid_row()

        for top_runoff in range(1):
            self.color("beige")
            self.solid_row()

        for top_grass in range(3):
            self.color("green yellow")
            self.solid_row()

    def solid_row(self):
        self.forward(600)
        self.setheading(90)
        self.forward(10)
        self.setheading(180)
        self.forward(600)
        self.setheading(90)
        self.forward(10)
        self.setheading(0)