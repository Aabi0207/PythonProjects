from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from brick import Brick

screen = Screen()
screen.setup(width=920, height=700)
screen.bgcolor("black")
screen.title("Break Out")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

width = 90

row = 7
column = 10

bricks = []

starting_y = 100
for i in range(row):
    current_y = starting_y + (i * 35)
    starting_x = -408
    for j in range(column):
        current_x = starting_x + (j * 90)
        brick = Brick(current_x, current_y, 4, 1)
        bricks.append(brick)

screen.listen()
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "Left")

while True:
    screen.update()
    ball.move()
    if ball.ycor() > 320:
        ball.bounce_y()

    if ball.ycor() < -320:
        ball.bounce_y()

    if (ball.distance(paddle) < 50 and ball.ycor() < -200):
        ball.bounce_y()

    if ball.xcor() > 420:
        ball.bounce_x()

    if ball.xcor() < -420:
        ball.bounce_x()

    for brick in bricks:
        if ball.distance(brick) < 50:
            ball.bounce_y()
            brick.reset()
            bricks.remove(brick)
            scoreboard.add_score()

    if ball.ycor() < -220:
        break


    time.sleep(0.09)
screen.exitonclick()
