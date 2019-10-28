from graph import *
windowSize(600,402)
def oblaka():
    penColor(153,179,183)
    brushColor(255,255,255)
    circle(120,50,10)
    circle(110,50,10)
    circle(100,50,10)
    circle(90,60,10)
    circle(105,60,10)
    circle(115,60,10)
    circle(125,60,10)
def pie():
    brushColor(186,80,5)
    circle(200,220,30)
    penColor(68,35,223)
    brushColor(68,35,223)
    rectangle(150,190,230,220)
def machta():
    penColor(0,0,0)
    brushColor(0,0,0)    
    rectangle(300,130,305,220)
    brushColor(222,213,153)
    polygon([(305,130),(320,180),(360,180)])
    polygon([(305,220),(320,180),(360,180)])

def ship():
    pie()
    penColor(68,35,223)
    brushColor(186,80,5)
    rectangle(200,250,380,220)
    polygon([(380,250),(460,220),(380,220)])
    penColor(0,0,0)
    brushColor(0,0,0)
    circle(390,232,10)
    penColor(255,255,255)
    brushColor(255,255,255)
    circle(390,232,6)
    machta()
    
def map():
   
    penColor(0,0,0)
    penSize(1)
    brushColor(161,241,255)
    rectangle(0,0,600,190)#nebo
    oblaka()
    brushColor(68,35,223)
    rectangle(0,190,600,280)#more
    brushColor(238,246,12)
    rectangle(0,280,600,400)#pesok
    penColor(238,246,12)
    circle(450,50,30)
    

map()
ship()
#pie()
run()
