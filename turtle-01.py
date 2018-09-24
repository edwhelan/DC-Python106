from turtle import *

def square(size):
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)

def triangle(size):
    forward(size)
    right(120)
    forward(size)
    right(120)
    forward(size)
    right(120)


square(32)
right(29)
square(199)
circle(100)
triangle(200)

input()