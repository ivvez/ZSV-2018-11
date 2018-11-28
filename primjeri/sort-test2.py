#program unosi broj bodova na testu, broj ucenika i broj bodova svakog ucenika
#zatim sortira ucenike po prezimenu i ispisuje ih
prezimena=[]
bodovi=[]
n = int(input('Broj ucenika'))
br_bod = int(input('Broj bodova u testu'))
for i in range(n):
    prezime = input('Upisi prezime ucenika:')
    prezimena.append(prezime)
    bod = int(input('Broj bodova:'))
    bodovi.append(bod)

prezimena, bodovi = zip(*sorted(zip(prezimena, bodovi)))


print ('Ispis ucenika, broj bodova i postotak:')
print ('------------------------------------------')
for i in range(n):
    print (prezimena[i], bodovi[i],(int(bodovi[i])/br_bod)*100,'%')
    
    
    
