# bubble sort
brojevi = [5, 8, 9, 2, 1, 4]

for i in range(len(brojevi)-1):
    for j in range((len(brojevi)-1)-i): # provjeravamo svaki element niza
        
        if brojevi[j] > brojevi[j+1]:
            brojevi[j], brojevi[j+1] = brojevi[j+1], brojevi[j] # napravi zamjenu

print(brojevi)
