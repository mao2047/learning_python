from random import randint

saludos = ["Bienvenido {name}, como estas?",
           "Bonjour {name} Comme tas le vous?",
           "Hola!, que tal todo {name}",
           "no te vacunaste? cagaste {name}, saludos al diablo!",
           "{name} te vacunaste? que bien!",
           "Que Dios te bendiga {name}"]

def saludo_random():
    temp = saludos[randint(0, len(saludos)-1)]
    name = input("como te llamas?: ")
    if "{name}" in temp:
        print(temp.replace("{name}", name))


saludo_random()
