##!/usr/bin/env python3
import turtle

side_num = int(input("Number of sides?"))
side_len = int(input("Side length?"))
border_color = input("Border color?")
fill_color = input("Fill color?")
angles_amp = 360 / side_num

wn = turtle.Screen()
ninja = turtle.Turtle()
ninja.shape("turtle")
ninja.pen(fillcolor=fill_color, pencolor=border_color)

ninja.begin_fill()
for _ in range(side_num):
    ninja.forward(side_len)
    ninja.left(angles_amp)
ninja.end_fill()

wn.exitonclick()
