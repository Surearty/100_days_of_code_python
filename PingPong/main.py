from turtle import Screen
from paddle import Paddle
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

left_paddle = Paddle(-350,0)
right_paddle = Paddle(350, 0)
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
game_is_on = True

while game_is_on:
    screen.update()





screen.exitonclick()