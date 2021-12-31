'''
creador de acrósticos BASADO en frases de los
abecedarios de pasta sempai, 6ix9ine, MC Ride y Cardi B
Es una chorrada para practicar el uso de archivos YAML
por mao2047 -> github.com/mao2047
'''

import yaml
import random 
from yaml.loader import SafeLoader, FullLoader

'''
lee el archivo uganda.yaml que es una base de datos
conteniendo diccionarios, que según su orden serán
dictx, donde x es la posición del diccionario y
luego el key de cada uno. la lista diccinarios es
para mejor manejo a la hora de traer cada frase
del acróstico.
'''

with open('uganda.yaml', 'r') as file:
    db = yaml.load(file, Loader=yaml.FullLoader)
    
    dict1 = db[0]["uganda"]
    dict2 = db[1]["mix"]
    dict3 = db[2]['grips']
    diccionarios = [dict1, dict2, dict3]

'''
la función acrostico() recibe un nombre e iteriza
cada letra, buscando una linea en cualquiera de los
diccionarios, dichos diccionarios deben ser al azar
por lo que i es un num. random para elegir dict(i).
Luego de imprimir la letra y su linea, vuelve a 
randomizar i para que seleccione otr diccionario y 
sea más variado el acróstico.
'''

def acrostico(nombre):
    print("")
    i = random.choice(range(0, 3))
    for letra in nombre:
        print(f"{letra.upper()} is for: {diccionarios[i][letra]}")
        i = random.choice(range(0, 3))

'''
un simple ciclo while donde enter es para salir
'''

while True:
    nombre = input("\ndame tu nombre: ")
    if nombre == "":
        break
    else:
        acrostico(nombre)
