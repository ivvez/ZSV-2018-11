def dna_lanac(dna):
    parovi = { "A":"T",
               "T":"A",
               "C":"G",
               "G":"C"
                  }
    return "".join([parovi[x] for x in dna])

print (dna_lanac('TTTAAA'))
