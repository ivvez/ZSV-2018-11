# napišite funkciju koja simulira loto 6/45 i izvlaèi 7 brojeva
# funkcija vraæa listu izvucenih brojeva

import random
l = []
def loto():
    
    for i in range(7):
        a = random.randint(1,45)
        l.append(a)
        
    return l

print ('Loto brojevi:',loto())
