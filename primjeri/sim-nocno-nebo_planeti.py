#ucenicki projekt
#dobra ideja, povrsna realizacija, vremenski zahtjevno
import turtle 
import random

win = turtle.Screen()
win.bgcolor("black")
turtle2 = turtle.Turtle()
turtle = turtle.Turtle()

def zvijezde():
    turtle2.speed(0)
    turtle2.color("white")
    turtle2.begin_fill()
    turtle2.circle(1) 
    turtle2.end_fill()
    turtle2.up() 
    y = random.randint(0,360)
    turtle2.seth(y) 
    if turtle2.xcor() < -300 or turtle2.xcor() > 300:
            turtle2.goto(0, 0) #vrati se na sredinu
    elif turtle2.ycor() < -300 or turtle2.ycor() > 300:
            turtle2.goto(0, 0) 
    z = random.randint(40,200)
    turtle2.forward(z) 
    turtle2.down() 

for i in range(0, 50):
	zvijezde()
while True:
    a=win.numinput("2018.g.", "Upiši mjesec:", minval=1, maxval=12)
    if int(a) == 9:
        turtle.clear()
        turtle.color("Yellow") 
        turtle.penup()
        turtle.goto(0,-155)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()

        turtle.color("red") 
        turtle.pencolor("red")
        
        turtle.penup()
        turtle.goto(-190,-35)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()

    elif int(a) == 8:
        turtle.clear()
        turtle.color("Yellow") 
        turtle.pencolor("yellow")
        
        turtle.penup()
        turtle.goto(0,-35)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()

        turtle.color("red") 
        turtle.pencolor("red")
        
        turtle.penup()
        turtle.goto(-190,-10)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()

    elif int(a) == 7:
        turtle.clear()
        turtle.color("Yellow") 
        turtle.pencolor("yellow")
        
        turtle.penup()
        turtle.goto(0,-50)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()

        turtle.color("Red") 
        turtle.pencolor("red")
        
        turtle.penup()
        turtle.goto(-190,-150)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()

    elif int(a) == 6:
        turtle.clear()
        turtle.color("Yellow") 
        turtle.pencolor("yellow")
        
        turtle.penup()
        turtle.goto(0,-150)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()

    elif int(a) == 5:
        turtle.clear()
        turtle.color("Burlywood") 
        turtle.pencolor("burlywood")
        
        turtle.penup()
        turtle.goto(170,170)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()

    elif int(a) == 1:
        turtle.clear()
        turtle.color("Blue") 
        turtle.pencolor("blue")
        
        turtle.penup()
        turtle.goto(0,10)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(3)
        turtle.end_fill()
        
win.mainloop() 
