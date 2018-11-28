
from wghs import *
screenSize(400,400)
setBackgroundColour('white')

#mreza
def grid():
    x1=20
    x2=20
    x3=20
    x4=20

 
    for i in range(20):
        drawLine(x1,0,x2,400,'gray')
        x1=x1+20
        x2=x2+20

    for j in range(20):
        drawLine(0,x3,400,x4,'gray')
        x3=x3+20
        x4=x4+20
    
    
#koordinatni sustav
def coordinate():
    x5=20
    x6=20
    x7=20
    x8=20
    drawLine(200,20,200,380,'black',2)
    drawLine(20,200,380,200,'black',2)
    for k in range(20):
        drawLine(x5,200,x6,210,'black',1)
        x5=x5+20
        x6=x6+20
    for l in range(20):
        drawLine (200,x7,210,x8,'black',1)
        x7=x7+20
        x8=x8+20

#labele brojevi x pozitivni i x negativni
    x9=220
    t1=1
    for m in range(10):
        lbl1=makeLabel(str(t1),12,x9,210,'black')
        showLabel(lbl1)
        x9=x9+20
        t1=t1+1

    x10=175
    t2=-1
    for n in range(9):
        lbl2=makeLabel(str(t2),12,x10,210,'black')
        showLabel(lbl2)
        x10=x10-20
        t2=t2+(-1)

#labele brojevi y pozitivni i y negativni
    y11=175
    t3=1
    for o in range(9):
        lbl3=makeLabel(str(t3),12,220,y11,'black')
        showLabel(lbl3)
        y11=y11-20
        t3=t3+1


    y12=230
    t4=-2
    for o in range(8):
        lbl4=makeLabel(str(t4),12,220,y12,'black')
        showLabel(lbl4)
        y12=y12+20
        t4=t4+(-1)    
    

grid()
coordinate()
#oblici
drawEllipse(380,260,20,20,'blue')
drawEllipse(260,120,20,20,'yellow')
drawEllipse(160,160,20,20,'red')
drawEllipse(260,240,20,20,'green')
drawEllipse(140,260,20,20,'purple')
drawEllipse(60,140,20,20,'gray')
drawEllipse(100,360,20,20,'brown')

#textbox i provjera
lbl=makeLabel('Upisi koordinate plavog kruga:',14,10,5,'black')
k=1
while True:
    showLabel(lbl)
    tb=makeTextBox(10,30,80,0,'')
    textBoxInput(tb)

    if k==1: 
        if tb.text=='9,-3':
            changeLabel(lbl,'Bravo!Upisi koordinate zutog kruga','black')
            k=2
           
        else:
            changeLabel(lbl,'Netocno! Pokusaj ponovno!','red')
    elif k==2:
        if tb.text=='3,4':
            changeLabel(lbl,'Bravo!Upisi koordinate crvenog kruga','black')
            k=3
        else:
            changeLabel(lbl,'Netocno! Pokusaj ponovno!','red')
    elif k==3:
        if tb.text=='-2,2':
            changeLabel(lbl,'Bravo!Upisi koordinate zelenog kruga','black')
            k=4
        else:
            changeLabel(lbl,'Netocno! Pokusaj ponovno!','red')
    elif k==4:
        if tb.text=='3,-2':
            changeLabel(lbl,'Bravo!Upisi koordinate ljubicastog kruga','black')
            k=5
        else:
            changeLabel(lbl,'Netocno! Pokusaj ponovno!','red')
    elif k==5:
        if tb.text=='-3,-3':
            changeLabel(lbl,'Bravo!Upisi koordinate sivog kruga','black')
            k=6
        else:
            changeLabel(lbl,'Netocno! Pokusaj ponovno!','red')
    elif k==6:
        if tb.text=='-7,3':
            changeLabel(lbl,'Bravo!Upisi koordinate smedjeg kruga','black')
            k=7
        else:
            changeLabel(lbl,'Netocno! Pokusaj ponovno!','red')
    elif k==7:
        if tb.text=='-5,-8':
            changeLabel(lbl,'Bravo!Vjezba je gotova!','black')
            k=8
        else:
            changeLabel(lbl,'Netocno! Pokusaj ponovno!','red')
            
        
endWait()
