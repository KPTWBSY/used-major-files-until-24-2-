from tkinter import *
import time
tk=Tk()
canvas=Canvas(tk,width=800,height=800)
canvas.pack()
scores=[]
print('input 5 scores(0~100): ')
for k in range(5):
    score=int(input())
    scores.append(score)
i=0
for score in scores:
    x1=100
    y1=100+i
    x2=100+score*3
    y2=100+50+i
    if score>=90:
         canvas.create_rectangle(x1,y1,x2,y2,fill='green')
    elif score>=80:
         canvas.create_rectangle(x1,y1,x2,y2,fill='blue')
    elif score>=60:
        canvas.create_rectangle(x1,y1,x2,y2,fill='orange')
    elif score<60:
        canvas.create_rectangle(x1,y1,x2,y2,fill='red')
    
    canvas.create_text(x2+40,y1+20,text=str(score))
    i=i+100
    tk.update()
    time.sleep(0.5)
