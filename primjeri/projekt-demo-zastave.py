from wghs import *
screenSize(400,400)
setBackgroundColour('white')
k=1
bod=0
lbl=makeLabel('Naziv drzave?',14,10,10,'black')

lbl1=makeLabel('Bodovi:',14,10,60,'black')
lbl2=makeLabel(str(bod),14,60,60,'black')
showLabel(lbl1)
showLabel(lbl2)

#njemacka
drawRect(40,120,320,70,'black')
drawRect(40,190,320,70,'red')
drawRect(40,260,320,70,'yellow')
while True:
    showLabel(lbl)
    tb=makeTextBox(10,30,100,0,'')
    textBoxInput(tb)

    if k==1: 
        if tb.text=='njemacka':
            bod=bod+1
            changeLabel(lbl,'Bravo!Naziv drzave?','black')
            changeLabel(lbl2,str(bod))
            clearShapes()
            k=2
            drawRect(40,120,320/3,70*3,'blue')
            drawRect(140,120,320/3,70*3,'white')
            drawRect(240,120,320/3,70*3,'red')
           
        else:
            changeLabel(lbl,'Netocno! Pokusaj ponovno!','red')
    elif k==2:
        if tb.text=='francuska':
           bod=bod+1
           changeLabel(lbl2,str(bod)) 
           changeLabel(lbl,'Bravo!Naziv drzave?','black')
           clearShapes()
           k=3
           drawRect(40,120,320/3,70*3,'#17BF36')
           drawRect(140,120,320/3,70*3,'white')
           drawRect(240,120,320/3,70*3,'red')
           
        else:
            changeLabel(lbl,'Netocno! Pokusaj ponovno!','red')
    elif k==3:
        if tb.text=='italija':
            bod=bod+1
            changeLabel(lbl2,str(bod))
            changeLabel(lbl,'Bravo!Naziv drzave?','black')
            clearShapes()
            k=4
            drawRect(40,120,320,70*3,'blue')
            drawRect(40,210,320,50,'yellow')
            drawRect(110,120,50,70*3,'yellow')
            
        else:
            changeLabel(lbl,'Netocno! Pokusaj ponovno!','red')          
        
endWait()
