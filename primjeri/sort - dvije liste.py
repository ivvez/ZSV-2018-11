l = ['anic','peric','katic']
l2 = [2009, 2005,2001]

# sortiraj po prezimenu
a = sorted(zip(l, l2))
for i,j in a:
    print (i,j)
    
print('-------')

# sortiraj po godini rodjenja
b = sorted(zip(l, l2), key=lambda x: x[1])
for i,j in b:
    print (i,j)
    
