import zk

def opciones():
    while True:
        print("1: crear nueva nota \n2: editar una nota \n3: borrar nota \n4:añadir referencia \n0: salir")
        answer = int(input(":" ))
        if answer == 1:
            zk.write_fn()
        elif answer == 0:
            break
        else:
            print("not an option, try again")


def menu():
    while True:
        print("ZettellKasten \n ¿Que desea acer?")
        print("1: Add a fleeting note \n2: Add a Literature note \n3: Add a permament note \n0: salir")
        answer = int(input(":" ))
        if answer == 1:
            opciones()
        elif answer == 0:
            break
        else:
            print("not an option, try again")

menu()
