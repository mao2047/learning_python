'''
challenges from python by example
'''


#b011
def comprobante(x, y):
    x = int(input("introduza el primer numero: "))
    y = int(input("introduza el segundo numero: "))

    multiplo = x // y
#    residuo = x % y
    print(f"{y} entra {multiplo} veces en {x}")


#b012
def largernumber():
    print("give me two numbers")
    number1, number2 = int(input(": ")), int(input(": "))

    if number1 > number2:
        print(number1, number2)
    elif number2 > number1:
        print(number2, number1)
    else:
        print("those are the same numbers")


#b013
def under20():
    number = int(input("Introduce un numero: "))

    if number <= 20:
        print("thank you")
    else:
        print("too high")


#
def askred():
    color = input("What is your favourite colour?: ").lower()

    if color == "red":
        print("I like red too")
    else:
        print(f"I don't like {color}, I prefer red")



