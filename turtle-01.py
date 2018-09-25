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
penup()
goto(-280, -280)
pendown()
start_loc = position()          


def triforce(size):
    pencolor('#FF940D')
    triangle_start1 = position()
    penup()
    goto(triangle_start1)
    pendown()
    triangle(size)
  
    forward(size)
    triangle_start2 = position()
    penup()
    goto(triangle_start2)
    pendown()
    triangle(size)
    left(120)
    forward(size)
    right(120)
    triangle_start3 = position()
    penup()
    goto(triangle_start3)
    pendown()
    triangle(size)
    triforce(size / 2)

def spiral_pattern(repeat):
    for i in range(repeat):
        forward(repeat)
        left(124)


triforce(300)
penup()
goto(current_loc)
pendown()
triforce(150)
# penup()
# goto(-280, -280)
# pendown()
# triforce(300)
# spiral_pattern(100)
triforce(150)


input()