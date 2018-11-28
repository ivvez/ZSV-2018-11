#obicna for petlja
for i in range(10):
    if i%2==0:
        print(i+2)

#list comprehension
l = [i+2 for i in range(10) if i%2==0]
print(l)
