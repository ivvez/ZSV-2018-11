def dna_lanac(dna):
    s = ''
    for i in dna:
        if i=='T':
            s += 'A'
        elif i=='A':
            s += 'T'
        elif i=='G':
            s += 'C'
        elif i=='C':
            s += 'G'

    return s


print (dna_lanac('TAATGAAC'))
