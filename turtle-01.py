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
    left(120)
    forward(size)
    left(120)
    forward(size)
    left(120)


def triforce(size):
    triangle(size)
    forward(size / 2)
    left(120)
    triangle(size / 2)
    right(120)
    triangle(size / 2)
    left(120)
    forward(size / 2)
    right(120)
    forward(size / 2)
    # triangle(size / 2)
    # triangle(size / 2)


triforce(250)
# triangle(250)

input()