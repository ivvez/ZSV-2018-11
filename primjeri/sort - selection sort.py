# selection sort
brojevi = [5, 8, 4, 12, 9, 1]

for i in range(len(brojevi)-1,0,-1):
    najveci = 0
    for j in range(1, i+1):
        if brojevi[j] > brojevi[najveci]: # usporedi trenutnu najvecu vrijednost i sljedeci element niza
            najveci = j

    #zamjena
    brojevi[i], brojevi[najveci] = brojevi[najveci], brojevi[i]

print(brojevi)
