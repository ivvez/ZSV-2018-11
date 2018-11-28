#ucitaj modul tkinter i random
from tkinter import *
from random import randint

#prikazi graficki prozor
prozor = Tk()
prozor.title("Ljubavni kalkulator")
prozor.config(width=300, height=300)

#prikazi naslov Ljubavni kalkulator
naslov = Label(prozor,text = "Ljubavni kalkulator",fg = "red",font = ("Comic Sans MS", 16))
naslov.place(x = 60,y = 20)

#prikazi tekst Zensko ime/Musko ime
z = Label(prozor,text = "Žensko ime: ")
z.place(x = 10,y = 90)
m = Label(prozor,text = "Muško ime: ")
m.place(x = 160,y = 90)

#prikazi polja za unos teksta
z_unos = Entry(prozor,width = 20)
z_unos.place(x = 10, y = 120)
m_unos = Entry(prozor, width = 20)
m_unos.place(x = 160, y = 120)


#funkcija za generiranje nasumicnog broja       
def izracunaj():
   n = randint(1,100)
   return n

#funkcija koja provjerava je li u textbox upisano ime i ispisuje nasumican broj
#nakon klika na gumb Izracunaj
def provjeri_prikazi():
    if len(z_unos.get()) == 0 or len(m_unos.get()) ==0 :
        rez = Label(prozor,text = "Upiši ime! ",fg="red",font = ("Comic Sans MS", 26))
        rez.place(x = 70,y = 210)
        
    else:
        rez = Label(prozor,text = "   "+str(izracunaj())+"%   ",font = ("Comic Sans MS", 34))
        rez.place(x = 70,y = 210)
    
#prikazi gumb Izracunaj
gumb = Button(prozor, text = "Izračunaj", command = lambda:[provjeri_prikazi(),izracunaj()])
gumb.place(x = 120,y = 160)


prozor.mainloop()
