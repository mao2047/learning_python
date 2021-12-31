def Impares(number):
    current = 0
    while current < number:
        current += 1
        if current % 2 == 0:
            continue
        print(current, end=" ")


def Climbing_Poll():
    
    def ordenador():
        lugares_ordenados = {}
        for item in set(lugares):
            lugares_ordenados[item] = lugares.count(item)
        lugares_pop = {k: v for k, v in sorted(lugares_ordenados.items(), key=lambda item: item[1], reverse=True)}
        for item, value in lugares_pop.items():
            print(f"{item}: {value}")

    afirma = 0
    lugares = []
    encuestados = []
    
    while True:
        name = input("Cual es tu nombre?: ")
        encuestados.append(name)
        respuesta = input("Te gustaria escalar alguna vez? (s/n): ")
        if respuesta == "s":
            afirma +=1
            monte = input("que montaña te gustaria escalar?: ")
            lugares.append(monte)
        else:
            print(f"muchas gracias {name}! \n")
        salida = input("deseas que otra persona llene la encuesta? (s/n): ")
        if salida == "s":
            pass
        else:
            break

    print(f"numero de personas encuestadas: {len(encuestados)}")
    print(f"Personas que desean escalar: {afirma}. \nPersonas que no desean escalar: {len(encuestados) - afirma} \n")
    print("Lugares en orden de popularidad:\n")

    ordenador()


#------------------------------------------------


Climbing_Poll()
#number = int(input(": " ))
#Impares(number)
