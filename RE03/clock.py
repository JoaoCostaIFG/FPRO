##!/usr/bin/env python3
import turtle

wn = turtle.Screen()
ninja = turtle.Turtle()
ninja.shape("turtle")
ninja.color("blue")
ninja.pensize(3)
wn.bgcolor("lightgreen")
ninja.penup()

for _ in range(12):
    ninja.forward(150)
    ninja.pendown()
    ninja.forward(10)
    ninja.penup()
    ninja.forward(25)
    ninja.stamp()
    ninja.setpos(0, 0)
    ninja.left(30)

wn.exitonclick()
