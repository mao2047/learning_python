def listas():
    num = input("Introduzca los numeros: ").replace(" ", "")
    lista_raw = num.split(",")
    lista_num = [int(item) for item in lista_raw]
    for numero in lista_num:
        print((int(((2 * 50 * numero )/30) ** 0.5)), end=" ")

listas()
