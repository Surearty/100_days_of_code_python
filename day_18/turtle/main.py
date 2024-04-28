from turtle import Turtle, Screen

tim = Turtle()
tim.shape('triangle')
tim.color('#b144bf')

# for _ in range (4):
#     tim.forward(100)
#     tim.right(90)

#CHALLANGE 3
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for i in range(3, 10):
    tim.pencolor(colors[i-3])
    dg = 360 / i
    for _ in range (i):
        tim.forward(50)
        tim.right(dg)
    i += 1






screen = Screen()
screen.exitonclick()
