# - napišite funkciju koja simulira bacanje N kockica
#dobivene vrijednosti spremite u listu i ispisite
import random

def kockica2(u):
    l = []
    for i in range(u):
        a = random.randint(1,6)
        l.append(a)
    return l

print (kockica2(int(input('Koliko puta zelis baciti kockicu?'))))
