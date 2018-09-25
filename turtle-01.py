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
    pencolor('#FF940D')
    triangle(size)
    forward(size)
    triangle(size)
    left(120)
    forward(size)
    right(120)
    triangle(size)

def spiral_pattern(repeat):
    for i in range(repeat):
        forward(repeat)
        left(124)
        
# penup()
# goto(-280, -280)
# pendown()
# triforce(600)
# penup()
# goto(-280, -280)
# pendown()
# triforce(300)
# spiral_pattern(100)
triforce(150)


input()