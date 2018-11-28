r={
  "2345": 2000,
  "2211": 3456.23,
  "2468": 12984.12
}
a=''
br=0

def odabir():
    global o
    print ('Za pregled stanja upišite broj 1')
    print ('Za isplatu upišite broj 2')
    print ('Za promjenu PIN-a upišite broj 3')
    o=int(input('Odabir:'))

def stanje():
    print ('Stanje na računu:',r[a])
    
def isplata():
    iznos=int(input('Upišite iznos za isplatu:'))
    if iznos<=r[a]:
        print ('Preuzmite novac')
        print('Novo stanje računa:', r[a]-iznos)
    else:
        print ('Nemate dovoljno novca na računu')

def promjena():
    pin_stari=int(input('Upišite trenutni PIN'))
    pin1 = int(input('Upišite novi PIN:'))
    pin2 = int(input('Potvrdite novi PIN:'))
    if pin1==pin2:
        print ('PIN uspješno promijenjen')
        #prodji kroz rijecnik, nadji stari pin i zamijeni ga s novim
        for i in r:
            if int(i)==int(pin_stari):
                r[pin1]=r.pop(i)
    else:
        print ('Krivo upisani trenutni PIN.')
        print ('PIN nije moguće promijeniti.')
    
    
while len(a)!=4:
    a=input('Unesite PIN:')
    if len(a)!=4: 
        print ('Netočan PIN, pokušajte ponovno')
        br+=1
        if br==4:
            print ('Upisali ste krivi PIN četiri puta. Daljni rad je onemogućen')
            break
    else:
        print ('Dobro došli')
        odabir()
        if o == 1:
            stanje()
        elif o==2:
            isplata()
        elif o==3:
             promjena()

        
print (r)

