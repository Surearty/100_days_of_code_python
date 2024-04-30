
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 212), (86, 77, 208), (86, 225, 235), (250, 8, 14), (242, 166, 157), (177, 180, 224), (36, 243, 159), (6, 81, 115), (11, 55, 248)]
tim = Turtle()
tim.speed(2)
color_num = 0
y = -200
tim.penup()
tim.hideturtle()
for i in range(10):
    tim.setpos(-200, i*50 + y)
    for _ in range (10):
        tim.dot(20, color_list[color_num])
        color_num+=1
        if color_num >= len(color_list):
            color_num = 0
        tim.forward(50)

screen = Screen()
screen.exitonclick()



