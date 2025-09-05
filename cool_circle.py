import turtle
import random
screen = turtle.Screen()
turtle.speed(0)
turtle.width(3)
turtle.colormode(255)

for p in range (23):
    turtle.pencolor(random.randint(60,255),random.randint(10,20),random.randint(45,255))
    turtle.rt(125)
    for s in range (36):
        turtle.lt(10)
        turtle.fd(20)

screen.exitonclick()
