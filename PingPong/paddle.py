from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setpos(x, y)
        self.color('white')

    def move_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)

