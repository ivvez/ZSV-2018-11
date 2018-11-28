brojevi = [5, 6, 2, 1, 8, 6]
print(sorted(brojevi)) # Izlaz: [1, 2, 5, 6, 6, 8]
print(sorted(brojevi, reverse = True)) # Izlaz: [8, 6, 6, 5, 2, 1]

voce = ['mango', 'kivi', 'lubenica', 'banana', 'jagoda']
print(sorted(voce)) # Izlaz: ['ananas', 'banana', 'jabuka', 'jagoda', 'kruska']
print(sorted(voce, key = len)) # Izlaz: ['jabuka', 'kruska', 'ananas', 'banana', 'jagoda']

x = "python"
print(sorted(x)) # Izlaz: ['h', 'n', 'o', 'p', 't', 'y']
