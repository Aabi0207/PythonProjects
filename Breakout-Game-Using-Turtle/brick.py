import turtle
from turtle import Turtle
import random
turtle.colormode(255)
X_COR = -460
Y_COR = 30


class Brick(Turtle):
    def __init__(self):
        self.bricks = []
        super().__init__()
        self.hideturtle()
        self.create_bricks()

    def create_bricks(self):
        for i in range(5):
            global X_COR, Y_COR
            red = random.randint(30, 255)
            green = random.randint(30, 255)
            blue = random.randint(30, 255)
            for j in range(10):
                tim = Turtle(shape="square")
                tim.penup()
                tim.color((red, green, blue))
                tim.shapesize(stretch_len=4, stretch_wid=2)
                tim.goto(X_COR, Y_COR)
                X_COR += 100
                self.bricks.append(tim)
            X_COR = -460
            Y_COR += 60
