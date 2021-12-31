#b036
def RepeatName(name, number):
    for times in range(number):
        print(name)


#b037
def NameByChar(name):
    for char in name:
        print(char)


#038
def NameByCharNum(name, number):
    for times in range(number):
        for char in name:
            print(char)


#b039
def TablasMult(number):
    for times in range(1, 13):
        print(f"{number} x {times} = {number*times}")

#b040
def CountDowntoN(number):
    if number < 50:
        for times in range(number, 51):
            print((50 - times) + number)
    if number >= 50:
        print("debe ser menor a 50")
'''
cuando se cuenta (numbers, 51), el valor
times toma el primero valor de numbers
si numbers = 45, times = 45 y va times+1
hasta 51. Por lo que si times=48,50-times=2 
+ numbers = 47 y asi va cuenta atras
'''


#b041
def NamenTimes(name, number):
    if number <= 10:
        for times in range(number):
            print(name)
    else:
        print("number is too high")


#b042
def AddTotal():
    total = 0
    for times in range(5):
        valor = float(input("introduce el valor: "))
        respuesta = input("deseas agregarlo al total? (s/n): ").lower()
        if respuesta == "s":
            total = total + valor
        else:
            pass
    print(f"El total es {total}")


#b043
def UporDown():
    direccion = input("1)contar hacia arriba \n2)contar hacia abajo \n: ")
    if direccion == "1":
        ultimonum = int(input("Hasta que numero?: "))
        for times in range(1, ultimonum + 1):
            print(times, end=" ")
    elif direccion == "2":
        ultimonum = int(input("que numero menor a 20?: "))
        if ultimonum < 20:
            for times in range(ultimonum, 21):
                print((20 - times) + ultimonum, end=" ")
        else:
            print("debe ser menor a 20")
    else:
        print("no entiendo")


#b044
def PartyPeople(number):
    if number < 10:
        for times in range(number):
            guest = input("Guest's name: ")
            print(f"{guest} has been invited!")
    else:
        print("Too many people!")


#-----------------------

#name = input("como te llamas?: ")
#number = int(input("dame un numero: "))
#RepeatName(name, number)
#NameByChar(name)
#NameByCharNum(name, number)
#TablasMult(number)
#CountDowntoN(number)
#NamenTimes(name, number)
#AddTotal()
#UporDown()
#PartyPeople(number)
