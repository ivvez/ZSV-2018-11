def umnozak(n):
    if n == 1:
        return 1
    else:
        rez =  n * umnozak(n-1)
        print("Trenutni rezultat za ", n, " * faktorijel(" ,n-1, "): ",rez)
        return rez

print(umnozak(5))
