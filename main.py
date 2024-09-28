import colorgram
import turtle
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))


tim = turtle.Turtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


turtle.colormode(255)
tim.speed('fastest')

for i in range(1,101):  

    tim.color(random.choice(rgb_colors))  
    tim.dot(20)                         
    tim.forward(50)
    if i % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)                     
screen = turtle.Screen()
screen.exitonclick()
