import random
i = 0
lista = []
a = "dana"
while i < len(a):
    t = random.choice(range(0, 3))
    while t in lista:
        t = random.choice(range(0, 3))
    else:
        lista.append(t)
    i += 1


print(lista)
