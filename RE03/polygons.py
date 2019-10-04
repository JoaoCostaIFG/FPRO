##!/usr/bin/env python3
import turtle

wn = turtle.Screen()
ninja = turtle.Turtle()
ninja.shape("turtle")

for i in [3, 4, 6, 8]:
    angles_amp = 360 / i
    for i in range(i):
        ninja.forward(100)
        ninja.left(angles_amp)


wn.exitonclick()

'''
# Square
ninja.color("red")
for _ in range(4):
    ninja.forward(100)
    ninja.left(90)

# Equilateral Triangle
ninja.color("green")
for _ in range(3):
    ninja.forward(100)
    ninja.left(120)

# Hexagon
ninja.color("orange")
for _ in range(6):
    ninja.forward(100)
    ninja.left(60)

# Octagon
ninja.color("blue")
for _ in range(8):
    ninja.forward(100)
    ninja.left(45)
'''