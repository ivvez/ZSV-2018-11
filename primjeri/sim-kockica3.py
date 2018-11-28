#napišite funkciju koja baca 5 kockica, sve dok kockice ne pokažu istu vrijednost
#ishode kockica zapišite u listu i ispišite
#ispišite broj pokušaja  bacanja dok kockice nisu pokazale sve istu vrijednost

import random

def pet_kockica():
    check = False
    p = 0
    while check == False:
        lista = []
        a = None
        isti = 0
        razl = 0
    
        for i in range(5):
            b = random.randint(1,6)
            lista.append(b)
            if a == b or a == None:
                isti += 1
            else:
                razl +=1
            a = b 
            
        p += 1
            
        if razl == 0:
            print (lista)
            print ('Broj pokusaja:',p)
            check = True
            break
            
pet_kockica()
