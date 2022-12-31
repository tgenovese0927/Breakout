from turtle import Screen, Turtle
import time
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from blocks import Wall

ball = Ball()
bricks = Wall()
score = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('#D1D1DE')
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -280))

screen.listen()
screen.onkeypress(paddle.paddle_right, "Right")
screen.onkeypress(paddle.paddle_left, "Left")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if len(bricks.wall) == 0:
        score.end_game(win=True)
        break

    # Detect collision with walls

    if ball.xcor() < -380 or ball.xcor() > 380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.ycor() < -280:
        ball.reset_position()
        score.decrease_lives()
        if score.lives == 0:
            score.reset()
            game_on = False
            score.end_game(win=False)

    # Detect collision with paddle

    if ball.distance(paddle) < 110 and ball.ycor() < -250:
        ball.bounce_y()

    # Brick collision

    for brick in bricks.wall:
        if ball.distance(brick) < 40:
            score.increase_score()
            brick.clear()
            brick.goto(3000, 3000)
            bricks.wall.remove(brick)

            if ball.xcor() > brick.right or ball.xcor() < brick.left:
                ball.bounce_x()

            elif ball.ycor() < brick.lower or ball.ycor() > brick.upper:
                ball.bounce_y()

screen.exitonclick()
