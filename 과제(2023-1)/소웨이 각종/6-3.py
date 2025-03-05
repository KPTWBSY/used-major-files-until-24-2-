import turtle
import random

turtle.setup(width=500,height=500)
t=turtle.Pen()

t.width(3)
for i in range(0,301,8):
    color=['red','yellow','orange','green']
    t.pencolor(random.choice(color))
    t.forward(i)
    t.left(120)
