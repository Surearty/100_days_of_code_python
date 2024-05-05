from turtle import Turtle

FONT = ('Courier', 40, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.right_score = 0
        self.left_score = 0
        self.update_score()
        self.color("white")

    def update_score(self):
        self.clear()
        self.write(f"{self.left_score}      "
                   f":      {self.right_score}", align='center', font=FONT)

    def l_point(self):
        self.left_score += 1
        self.update_score()

    def r_point(self):
        self.right_score += 1
        self.update_score()
