import turtle 
import random

prozor = turtle.Screen() 

korni1 = turtle.Turtle() 
korni2 = turtle.Turtle()

korni1.color("Red") 
korni1.pencolor("red") 
korni2.color("Green")
korni2.pencolor("green")


brojac = 0 

while brojac <= 1000:

    korni1.setheading(random.randint(0,360))# odredi smjer kretanja kornjace
    korni1.forward(random.randint(-50,50)) # odredi udaljenost kretanja prema naprijed
    korni2.setheading(random.randint(0,360))
    korni2.forward(random.randint(-15,15))

    brojac += 1 

prozor.mainloop() 
