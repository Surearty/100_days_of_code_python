import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_bet = screen.textinput('Make your bet',
                            'Wich turtle win the race? Enter the color:')
is_race_on = False
turtles = []
for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-200, -100 + i * 30)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            win_color = turtle.pencolor()
            is_race_on = False
            if user_bet == win_color:
                print("You win!!!! ")
            else:
                print(f"You lose!!! Sorry {win_color} turtle wins the game")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
