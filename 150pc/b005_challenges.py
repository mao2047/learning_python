#b045
def SumaTotal():
    total = 0
    while total <= 50:
        valor = int(input("ingrese valor: "))
        total = total + valor
        print(f"The total is: {total}")


#b047
def SumUntil():
    value1 = int(input("ingresa el primer valor: "))
    value2 = int(input("ingresa el segundo valor: "))
    total = value1 + value2
    respuesta = input("¿deseas agregar otro numero? (y/n) \n: ")
    while respuesta == "y":
        value3 = int(input("Ingresa otro valor: "))
        total = total + value3
        respuesta = input("¿deseas agregar otro numero? (y/n) \n: ")
    print(f" el total es {total}")


#b048
def PartyCount():
    respuesta = "y"
    contador = 0
    convivio = []
            
    while respuesta == "y":
        contador +=1
        invitado = input("Ingresa nombre del invitado: ")
        convivio.append(invitado)
        print(f"{invitado} ha sido invitado a la fiesta.\n")
        respuesta = input("deseas invitar a alguien mas? (y/n) \n: ")
    
    print(f"invitaste a {contador} personas: \n{convivio}")


#b049
def GuessNumber():
    oculto = 50
    intento = 0
    while intento != oculto:
        intento = int(input("dame un numero: "))
        if intento != oculto and intento < oculto:
            print(f"{intento} es muy bajo")
        elif intento != oculto and intento > oculto:
            print(f"{intento} es muy alto")
        else:
            break
    print("lo descubriste!, saludame al diablo!")


GuessNumber()



#SumUntil()
#SumaTotal()
#PartyCount()
