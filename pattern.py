#enjoy this pattern
from turtle import *
from colorsys import *
setpos(0,80)
speed(0)
bgcolor('black')
pensize(2)
h=0.71
for i in range(150):
    c=hsv_to_rgb(h,1,1)
    color(c)
    h+=.004
    circle(140-1,90)
    lt(90)
    lt(20)
    circle(140-1,90)
    lt(18)
hideturtle()
