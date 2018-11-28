from turtle import *

def kvadrat(a):
    color(u)
    for k in range(4):
        fd(a); rt(90)


def pravokutnik (a,b):
    color(u)
    for k in range(2):
        fd(a);rt(90)
        fd(b);rt(90)


n = textinput('Želiš li nacrtati kvadrat ili pravokutnik?','dogovor:')
if n in 'kvadratKvadratKVADRAT':
    u = textinput('Upiši boju na engleskom jeziku malim slovima','dogovor:')
    a = textinput('Upiši duljinu stranice kvadrata!','dogovor:')
    a=int(a)
    kvadrat(a)
elif n in 'pravokutnikPravokutnikPRAVOKUTNIK':
    u = textinput('Upiši boju na engleskom jeziku malim slovima','dogovor:')
    a = textinput('Upiši duljinu stranice a','dogovor:')
    a=int(a)
    b = textinput('Upiši duljinu stranice b','dogovor:')
    b=int(b)
    pravokutnik (a,b)
