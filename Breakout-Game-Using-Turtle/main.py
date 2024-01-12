from turtle import Screen
from paddle import Paddle
from brick import Brick
from ball import Ball
from scoreboard import Scoreboard
import turtle
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=1020, height=800)
screen.title("BreakOut Game")
screen.tracer(0)

paddle = Paddle()
brick = Brick()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
turtle.onkeypress(paddle.move_rightwards, "Right")
turtle.onkeypress(paddle.move_leftwards, "Left")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if (ball.distance(paddle) < 80 and ball.ycor() < -340) or (ball.ycor() > 385):
        ball.bounce_y()
    if not -495 < ball.xcor() < 495:
        ball.bounce_x()
    if ball.ycor() < -400:
        scoreboard.game_over()
        game_is_on = False

    for i in brick.bricks:
        if i.distance(ball) < 45:
            i.hideturtle()
            ball.bounce_y()
            if 40 <= brick.bricks.index(i) < 50:
                scoreboard.add_score(20)
            elif 30 <= brick.bricks.index(i) < 40:
                scoreboard.add_score(15)
            elif 20 <= brick.bricks.index(i) < 30:
                scoreboard.add_score(10)
            elif 10 <= brick.bricks.index(i) < 20:
                scoreboard.add_score(5)
            else:
                scoreboard.add_score(1)

            if scoreboard.score in range(20, 511, 50):
                ball.move_speed *= 0.9
            brick.bricks.remove(i)

screen.exitonclick()
