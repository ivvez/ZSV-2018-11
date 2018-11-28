def najkraca(s):
    l = s.split()
    return min(l, key=len)
