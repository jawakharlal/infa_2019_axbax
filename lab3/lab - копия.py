from graph import *

penColor(0,0,0)
penSize(1)
brushColor("yellow")
circle(200,200,150) #голова
brushColor("red")
circle(140,160,35) #левый глаз
circle(260,160,26) #правый глаз
brushColor("black")
circle(140,160,15) #левый зрачок
circle(260,160,13) #правый зрачок
rectangle(140,300,260,320) #рот
polygon([(50,70),(60,58),(190,130),(180,142)])
polygon([(230,140),(220,130),(335,100),(340,110)])
elipse()
run()
