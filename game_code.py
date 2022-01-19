import _thread
import turtle
import time
import random
import winsound
import mysql.connector
P1=input('Enter the name of the red player:')
P2=input('Enter the name of the blue player:')
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Scores")
mydb1 = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="12345",
  database="Scores"
)
mycursor1=mydb1.cursor()
gamewin=turtle.Screen()
gamewin.title("AIFootball 2D")
gamewin.setup(width=800, height=600)
gamewin.bgcolor('green')
turtle.listen()
gamewin.bgpic('background.png')
#courtmakingturtles
painter=turtle.Turtle()
painter.pensize(5)
painter.speed(0)
painter.shape('circle')
painter.color('white','green')
painter.stamp()
painter.penup()
painter.setheading(270)
painter.forward(300)
painter.setheading(180)
painter.forward(5)
painter.setheading(90)
painter.forward(600)
painter.setheading(0)
painter.forward(10)
painter.setheading(270)
painter.forward(600)
painter.pendown()
painter.setheading(180)
painter.forward(405)
painter.right(90)
painter.forward(600)
painter.right(90)
painter.forward(800)
painter.right(90)
painter.forward(600)
painter.right(90)
painter.forward(600)
painter.penup()
#goalpostdrawing:
painter.goto(400,79)
painter.pendown()
painter.color('yellow','white')
painter.setheading(0)
painter.forward(40)
painter.right(90)
painter.forward(158)
painter.right(90)
painter.forward(40)
painter.penup()
painter.goto(-400,79)
painter.pendown()
painter.setheading(180)
painter.forward(40)
painter.left(90)
painter.forward(158)
painter.left(90)
painter.forward(40)
painter.penup()
#draws clock
painter.goto(-70,-310)
painter.pendown()
painter.color('white')
painter.setheading(0)
painter.forward(140)
painter.right(90)
painter.forward(60)
painter.setheading(180)
painter.forward(140)
painter.right(90)
painter.forward(60)
painter.hideturtle()
#leftplayer:
lp=turtle.Turtle()
lp.penup()
lp.color('red')
lp.setposition(-400,0)
lp.speed(0)
lp.shape('square')
def goup():
    if(lp.ycor()<280):
            lp.setheading(90)
            lp.forward(28)
            winsound.PlaySound("run.wav",winsound.SND_ASYNC)
def godw():
    if(lp.ycor()>-280):
            lp.setheading(270)
            lp.forward(28)
            winsound.PlaySound("run.wav",winsound.SND_ASYNC)
def gofw():
    if(lp.xcor()<-10):
            lp.setheading(0)
            lp.forward(28)
            winsound.PlaySound("run.wav",winsound.SND_ASYNC)
def gobw():
    if(lp.xcor()>-390):
            lp.setheading(180)
            lp.forward(28)
            winsound.PlaySound("run.wav",winsound.SND_ASYNC)                
turtle.onkey(goup,"w")
turtle.onkey(godw,"s")
turtle.onkey(gofw,"d")
turtle.onkey(gobw,"a")
turtle.onkey(goup,"W")
turtle.onkey(godw,"S")
turtle.onkey(gofw,"D")
turtle.onkey(gobw,"A")
#rightplayer
rp=turtle.Turtle()
rp.penup()
rp.color('blue')
rp.speed(0)
rp.setposition(400,0)
rp.shape('square')
def rgoup():
    if(rp.ycor()<280):
            rp.setheading(90)
            rp.forward(28)
            winsound.PlaySound("run.wav",winsound.SND_ASYNC)
def rgodw():
    if(rp.ycor()>-280):
            rp.setheading(270)
            rp.forward(28)
            winsound.PlaySound("run.wav",winsound.SND_ASYNC)
def rgofw():
    if(rp.xcor()>10):
            rp.setheading(180)
            rp.forward(28)
            winsound.PlaySound("run.wav",winsound.SND_ASYNC)
def rgobw():
    if(rp.xcor()<390):
            rp.setheading(0)
            rp.forward(28)
            winsound.PlaySound("run.wav",winsound.SND_ASYNC)
turtle.onkey(rgoup,"Up")
turtle.onkey(rgodw,"Down")
turtle.onkey(rgofw,"Left")
turtle.onkey(rgobw,"Right")
#ball
bl=turtle.Turtle()
bl.color('black','yellow')
bl.goto(0,0)
bl.penup()
bl.speed(0)
bl.setpos(0,0)
bl.shape('circle')
ys=0
xs=0   
reai=0
reai1=0
traj=-1
rscore=0
lscore=0
#scoringturtle:
score=turtle.Turtle()
score.color('white')
score.speed(0)
score.hideturtle()
score.penup()
score.goto(0,320)
score.write("{}:0        {}:0".format(P1,P2),align="center",font=("Arial", 22, "bold"))
#timekeeper
tim=turtle.Turtle()
tim.penup()
sec=100
tim.goto(0,-374)
tim.color('white')
tim.write(sec,align="center", font=("Arial",44,"bold"))
tim.hideturtle()
restur=turtle.Turtle()
restur.hideturtle()
restur.penup()
restur.goto(0,-50)
restur.pendown()
#Gameloop
def f1():
    global lp
    global mycursor1
    global rp
    global bl
    global lscore
    global rscore
    global xs
    global ys
    global sec
    global restur
    global P1
    global P2
    while True:
        lx=lp.xcor()
        rx=rp.xcor()
        ly=lp.ycor()
        ry=rp.ycor()
        bx=bl.xcor()
        by=bl.ycor()
        def exitq():
            global gamewin
            gamewin.bye()
        turtle.onkey(exitq,'Escape')
        if(lx+20>bx and lx-20<bx and rx+20>bx and rx-20<bx):
            rp.goto(rx+15,ry)
            lp.goto(lx-15,ly)
    #AIReal(within the loop):
        def ai1():
            global reai1
            reai1=1
        kke=random.randrange(-20,40,1)
        if(reai1==1):        
            if(bx<lx):
                if(by>ly):
                    lp.goto(lx-11,ly+11)
                if(by<ly):
                    lp.goto(lx-11,ly-11)
                if(by==ly):
                    lp.goto(lx-11,ly)
            if(bx>lx):
                if(by<ly and ly>-285):
                    if(lx>-390 and lx<-10):
                        lp.goto(lx+kke,ly-11)
                    if(lx<=-390):
                        lp.goto(-380,ly-11)
                    if(lx>=-10): 
                        lp.goto(-25,ly-11)
                if(ly<=-285):
                        lp.goto(lx,ly+11)
                if(by==0 and bx==0):
                    lp.goto(lx+11,ly)
        turtle.onkey(ai1,'R')
        turtle.onkey(ai1,'r')
        def trajc():
            global traj
            traj=traj*(-1)
            bl.pendown()
            bl.pensize(4)
            
        def ai2():
            global reai
            reai=1
        kk=random.randrange(-40,20,1)
        if(reai==1):        
            if(bx>rx):
                if(by>ry):
                    rp.goto(rx+11,ry+11)
                if(by<ry):
                    rp.goto(rx+11,ry-11)
                if(by==ry):
                    rp.goto(rx+11,ry)
            if(bx<rx):
                if(by<ry and ry>-285):
                    if(rx<390 and rx>10):
                        rp.goto(rx+kk,ry-11)
                    if(rx>=390):
                        rp.goto(380,ry-11)
                    if(rx<=10): 
                        rp.goto(25,ry-11)
                if(ry<=-285):
                        rp.goto(rx,ry+11)
                if(by==0 and bx==0):
                    rp.goto(rx-11,ry)        
        if(traj==1):   
            if(bx>rx-15 and bx<rx+15 and by>ry-15 and by<ry+15):
                bl.clear()
                bl.color('blue','yellow')
            if(bx>lx-15 and bx<lx+15 and by>ly-15 and by<ly+15):
                bl.clear()
                bl.color('red','yellow')             
        turtle.onkey(trajc,'t')
        turtle.onkey(trajc,'T')
        turtle.onkey(ai2,'B')
        turtle.onkey(ai2,'b')            
        bl.goto((bx-xs),(by-ys))
        if(bx>(lx-15) and bx<(lx+15) and by>(ly-15) and by<(ly+15)):
            winsound.PlaySound("kick.wav",winsound.SND_ASYNC)
            xs=-3
            ys*=-1
            if(ys==0):
                ys=3
            if(xs==0):
                xs=3
        if(bx>(rx-15) and bx<(rx+15) and by>(ry-15) and by<(ry+15)):
            winsound.PlaySound("kick.wav",winsound.SND_ASYNC)
            xs=3
            ys*=-1
            if(ys==0):
                ys=3
            if(xs==0):
                xs=-3
        if(by>290):
            winsound.PlaySound("wall2.wav",winsound.SND_ASYNC)
            ys=3
        if(by<-290):
            winsound.PlaySound("wall2.wav",winsound.SND_ASYNC)
            ys=-3
        if(bx>390):
            winsound.PlaySound("wall2.wav",winsound.SND_ASYNC)
            xs=3
        if(bx<-390):
            winsound.PlaySound("wall2.wav",winsound.SND_ASYNC)
            xs=-3
    #goalsystem(withintheloop):
        if(bx<=-385 and by>=-77 and by<=77):
            lscore=lscore+1
            score.clear()
            score.write("{}:{}        {}:{}".format(P1,rscore,P2,lscore),align="center",font=("Arial", 22, "bold"))
            winsound.PlaySound("goalcheer.wav",winsound.SND_ASYNC)
            xs=0
            ys=0
            bl.goto(0,0)
            bl.clear()        
        if(bx>=385 and by>=-77 and by<=77):
            rscore=rscore+1
            score.clear()
            score.write("{}:{}        {}:{}".format(P1,rscore,P2,lscore),align="center",font=("Arial", 22, "bold"))
            winsound.PlaySound("goalcheer.wav",winsound.SND_ASYNC)
            xs=0
            ys=0
            bl.goto(0,0)
            bl.clear()
        if(sec==0):
            bl.penup()
            bl.clear()
            bl.goto(500,800)
            bl.hideturtle()
            if(rscore>lscore):
                restur.color('red')
                restur.write(" {} Wins by {} points".format(P1,rscore-lscore),align="center",font=("Arial", 55, "bold"))
            if(lscore>rscore):
                restur.color('blue')
                restur.write(" {} Wins by {} points".format(P2,lscore-rscore),align="center",font=("Arial", 55, "bold"))
            if(rscore==lscore):
                restur.write("  It's a Draw",align="center",font=("Arial", 55, "bold"))
            time.sleep(5)
            gamewin.bye()
def f2():
    global sec
    global tim
    while(sec>0):    
        sec=sec-1
        time.sleep(1)
        tim.clear()
        tim.write(sec,align="center", font=("Arial",44,"bold"))
_thread.start_new_thread(f1,())
_thread.start_new_thread(f2,())        
turtle.mainloop() 
gamewin.update()
turtle.done()