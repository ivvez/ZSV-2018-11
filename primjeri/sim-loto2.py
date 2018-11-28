#napišite program koji simulira loto 6/45 i izvlaci 7 brojeva
#program takoðer priva vaših 7 brojeva kao listu te ispisuje koliko brojeva ste pogodili
import random
izvuceni = []
def loto_brojevi():
    
    for i in range(0,6):
        br = random.randint(1,45)
        while br in izvuceni:
            br = random.randint(1,45)

        izvuceni.append(br)

    izvuceni.sort()
    print (izvuceni)

korisnik = []
def korisnik_brojevi():
     
    for i in range(0,6):
        br = int(input("Upišite broj od 1-45"))
        while br<1 or br>45:
            br = int(input('Pokušajte ponovno'))

        korisnik.append(br)

    korisnik.sort()
    print (korisnik)

loto_brojevi()
korisnik_brojevi()

brojac = 0
pogodak = []
for i in korisnik:
    if i in izvuceni:
        brojac+=1
        pogodak.append(i)

print ('Broj pogodataka:', brojac)



