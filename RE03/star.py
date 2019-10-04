##!/usr/bin/env python3
import turtle

side_num = int(input("Number of sides?"))
angles_amp = 360 / side_num

wn = turtle.Screen()
ninja = turtle.Turtle()
ninja.shape("turtle")
wn.bgcolor("blue")
ninja.color("white")
ninja.shape("circle")
ninja.speed(10)

for _ in range(side_num):
    ninja.forward(200)
    ninja.stamp()
    ninja.setpos(0, 0)
    ninja.left(angles_amp)

wn.exitonclick()
