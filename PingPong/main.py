import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
screen.listen()
score = Scoreboard()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    #detect collisions with paddles
    if (ball.distance(right_paddle) <= 50 and ball.xcor() > 320
            or ball.distance(left_paddle) <= 50 and ball.xcor() < -320):
        ball.bounce_x()
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()

screen.exitonclick()
