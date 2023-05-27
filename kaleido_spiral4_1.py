import turtle

from itertools import cycle
colors = cycle(['red', 'blue' ,'orange', 'green', 'blue', 'purple', 'yellow'])


def draw_circle(size,angle,shift):
    turtle.bgcolor('black')
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+7, angle-6,shift-5)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(16)
draw_circle(30,0,1)
