import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

hue = 0
n = 36  # Number of shapes

for i in range(360):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.color(color)
    t.forward(i * 3 / n + i)
    t.left(59)
    t.circle(i * 0.1)
    hue += 0.005

turtle.done()
