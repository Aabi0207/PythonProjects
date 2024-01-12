from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def add_score(self, add_value):
        self.score += add_value
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(400, 350)
        self.write(f"Score : {self.score}", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, -30)
        self.write("GAME OVER!", align="center", font=("Courier", 30, "normal"))
