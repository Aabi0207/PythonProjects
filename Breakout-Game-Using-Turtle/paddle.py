from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.goto(0, -350)

    def move_rightwards(self):
        self.setheading(0)
        self.forward(10)

    def move_leftwards(self):
        self.setheading(180)
        self.forward(10)
