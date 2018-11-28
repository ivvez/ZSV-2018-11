lista = []

while len(lista) < 5:
    ocjena = int(input('Upisi ocjenu: '))
    if ocjena < 0 or ocjena > 5:
        print ('Neispravan unos.')
        print (' Upisi ocjenu od 1-5')
        continue
    else:
        lista.append(ocjena)
       
    
print ('Ocjene:', lista)
print ('Najveca ocjena:', max(lista))
print ('Najmanja ocjena:', min(lista)) 
print ('Prosjek ocjena:', "{0:.2f}".format(sum(lista)/float(len(lista))))

                                       
