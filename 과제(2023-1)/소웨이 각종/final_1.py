from tkinter import *
import time
import math

tk=Tk()
canvas=Canvas(tk,width=500,height=500)

while 1:
    t=time.localtime()
    hour=(t[3]+t[4]/60)*15
    minute=(t[4]+t[5]/60)*6
    second=t[5]*6
    canvas.delete('all')

    canvas.create_arc(10,10,490,490,extent=359,style=CHORD,width=2)
    cx=250
    cy=250
    r=200
        
    sx=r*math.sin(second/360*3.14*2)
    sy=r*math.cos(second/360*3.14*2)
    canvas.create_line(cx,cy,cx+sx,cx-sy,fill='Red',width=1)

    mx=r*math.sin(minute/360*3.14*2)
    my=r*math.cos(minute/360*3.14*2)
    canvas.create_line(cx,cy,cx+mx,cx-my,fill='Green',width=5)

    hx=r*math.sin(hour/360*3.14*2)
    hy=r*math.cos(hour/360*3.14*2)
    canvas.create_line(cx,cy,cx+hx,cx-hy,fill='Blue',width=8)

    for i in range(24):
        angle=i*15
        x=cx+cx*0.7*math.cos(angle/360*3.14*2)
        y=cy+cy*0.7*math.sin(angle/360*3.14*2)
        if i==0:
            canvas.create_text(x,y,text=str(i+6))
        elif i>18 and i<24:
            canvas.create_text(x,y,text=str(i-18))
        else:
            canvas.create_text(x,y,text=str(i+6))

    for i in range(24):
        angle=i*15
            
        x1=cx+cx*0.9*math.cos(angle/360*3.14*2)
        y1=cy+cy*0.9*math.sin(angle/360*3.14*2)
        x2=cx+cx*0.8*math.cos(angle/360*3.14*2)
        y2=cy+cy*0.8*math.sin(angle/360*3.14*2)
        canvas.create_line(x1,y1,x2,y2,fill='Black',width=1)

    canvas.create_arc(240,240,260,260,extent=359,style=CHORD,fil='Black')
    canvas.pack()  
    
    
    time.sleep(0.01)
    tk.update()

