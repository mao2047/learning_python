'''
programa para calcular
promedio de la UNAH
'''

import csv
import os
import math

uv = []
promedio = []
suma_prom = []

def suma_promedio(uv, promedio):
    '''
    la función zip trabaja con
    dos listas y sus elementos
    correlativos
    '''
    for num1, num2 in zip(uv, promedio):
        suma_prom.append(num1 * num2)
        
def promedio_periodo(uv, promedio):
    '''
    modf permite separar un float en
    (entero, decimal)
    '''
    uvt = sum(uv)
    promediot = sum(suma_prom)
    promt = promediot/uvt
    splitted = math.modf(promt)
    if splitted[0] < 5:
        print("promedio de periodo: ", math.floor(promt))
    else:
        print("promedio de periodo: ", math.ceil(promt))

def main():
    num_clases = int(input("introduzca numero de clases: "))
    for i in range(num_clases):
        uv.append(int(input("uv: ")))
        promedio. append(int(input("promedio: ")))
    suma_promedio(uv, promedio)
    promedio_periodo(uv, promedio)

print("--------------------------------------\nCaculadora de promedio de periodo UNAH\n--------------------------------------")
main()