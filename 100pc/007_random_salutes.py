from random import randint

salutes = ["Que tal estas {name}", "Bonjour {name}, comme tas le vous?"]

def salutation(name):
    saludo = salutes[randint(0,1)]
    print(saludo.split())

name = input("inserte nombre: ")
salutation(name)
