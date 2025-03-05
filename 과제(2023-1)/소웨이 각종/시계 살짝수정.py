from tkinter import *
import time
import math

tk=Tk()
canvas=Canvas(tk,width=500,height=500)
width=500
height=500
canvas.create_arc(10,10,width-10,height-10,extent=359,style=CHORD,width=2)
cx=250
cy=250
r=200
t=time.localtime()
hour=(t[3]+t[4]/60)*30
minute=(t[4]+t[5]/60)*6
second=t[5]*6

sx=r*math.sin(second/360*3.14*2)
sy=r*math.cos(second/360*3.14*2)
canvas.create_line(cx,cy,cx+sx,cx-sy,fill='Red',width=1)

mx=r*math.sin(minute/360*3.14*2)
my=r*math.cos(minute/360*3.14*2)
canvas.create_line(cx,cy,cx+mx,cx-my,fill='Green',width=5)

hx=r*math.sin(hour/360*3.14*2)
hy=r*math.cos(hour/360*3.14*2)
canvas.create_line(cx,cy,cx+hx,cx-hy,fill='Blue',width=8)

for i in range(12):
    angle=i*30
    x=cx+cx*0.7*math.cos(angle/360*3.14*2)
    y=cy+cy*0.7*math.sin(angle/360*3.14*2)
    if i==0:
        canvas.create_text(x,y,text=str(i+12))
    else:
        canvas.create_text(x,y,text=str(i))

for i in range(12):
    angle=i*math.pi/6-math.pi/2
    
    x1=cx+cx*0.9*math.cos(angle)
    y1=cy+cy*0.9*math.sin(angle)
    x2=240*math.sin(i*30/360*3.14*2)
    y2=240*math.cos(i*30/360*3.14*2)
    canvas.create_line(x1,y1,cx+x2,cx-y2,fill='Black',width=1)

canvas.create_arc(240,240,260,260,extent=359,style=CHORD,fil='Black')
    

canvas.pack()


