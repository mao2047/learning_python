import math

#b027
def twodecimal():
    decnumber = float(input(": "))
    print(round(decnumber * 2, 2))


#b028
def squareroot():
    srnumber = int(input("un numero mayor a 500: "))
    if srnumber > 500:
        print(round(math.sqrt(srnumber), 2))
    else:
        print("number must be greater than 500")


#b031
def CircleArea(radius):
    return (round((math.pi * (radius ** 2)), 2))

#b032
def CilinderArea(depth, radius):
    print(CircleArea(radius) * depth)
    

#b033
def DivisionHelper():
    dividendo = int(input("ingrese dividendo: "))
    divisor = int(input("ingrese divisor: "))
    resultado, residuo = dividendo//divisor, dividendo%divisor
    print(f"{dividendo} dividido por {divisor} es {resultado} con {residuo} sobrante")


def GeometryCalc():
    while True:
        respuesta = int(input("1) cuadrado \n2) triangulo \n3) circulo \n0) salir \n: "))
        if respuesta == 1:
           ladoc = float(input("ingrese longitud del lado: "))
           print(f"El area del cuadrado es {ladoc**2} \n")
        elif respuesta == 2:
            base = float(input("ingrese base: "))
            altura = float(input("ingrese altura: "))
            print(f"el area del triangulo es {(base*altura)/2} \n")
        elif respuesta == 3:
            radius = float(input("ingrese longitud del radio: "))
            print(f"el area del circulo es {CircleArea(radius)} \n")
        elif respuesta == 0:
            print("Tu no entiende")
            break
        else:
            print("selecione una opcion valida \n")


#----------------------------

#depth = float(input("depth size: "))
#radius = float(input("radius size: "))

#CilinderArea(radius, depth)
#DivisionHelper()
#GeometryCalc()

