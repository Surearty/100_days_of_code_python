import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

left_paddle = Paddle(-350,0)
right_paddle = Paddle(350, 0)
ball = Ball()
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    if ball.distance(right_paddle) <= 50 and ball.xcor() > 320 or ball.distance(left_paddle) <= 50 and ball.xcor() < -320:
        ball.bounce_x()






screen.exitonclick()