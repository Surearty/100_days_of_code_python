from turtle import Turtle

FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.write_score()
        self.color("white")

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("The Game is over!", align='center', font=FONT)
    def update_score(self):
        self.score += 1
        self.write_score()
