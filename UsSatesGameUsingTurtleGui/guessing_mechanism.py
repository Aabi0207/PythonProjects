from turtle import Turtle


class GuessingMechanism(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def place(self, guess, x_cor, y_cor):
        self.goto(x_cor, y_cor)
        self.write(arg=guess)

