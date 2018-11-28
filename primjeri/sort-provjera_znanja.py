#program unosi broj bodova na testu, broj ucenika i broj bodova svakog ucenika
#zatim sortira ucenike (bubble sort-broj bodova od najmanjeg) i ispisuje ih
prezimena=[]
bodovi=[]
n = int(input('Broj ucenika'))
br_bod = int(input('Broj bodova u testu'))
for i in range(n):
    prezime = input('Upisi prezime ucenika:')
    prezimena.append(prezime)
    bod = int(input('Broj bodova:'))
    bodovi.append(bod)

def sortiraj(a,b):
    for i in range(n-1):
        for j in range((n-1)-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                b[j], b[j+1] = b[j+1], b[j]

sortiraj(bodovi,prezimena)

print ('Ispis ucenika, broj bodova i postotak:')
print ('------------------------------------------')
for i in range(n):
    print (prezimena[i], bodovi[i],(int(bodovi[i])/br_bod)*100,'%')
    
    
    
