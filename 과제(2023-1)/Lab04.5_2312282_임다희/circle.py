import turtle
turtle.setup(width=500,height=500)
edges=50
length=600/edges
angle=360/edges
t=turtle.Pen()
t.pencolor("blue")
t.width(5)
t.speed(5)
t.penup()
t.goto(0,300/3.14)
t.pendown()

for i in range(edges):
    t.forward(length)
    t.right(angle)
