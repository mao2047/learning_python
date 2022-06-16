'''
Github -> mao2047

Converts a given amount of dollars into lempiras
using a real time exchange rate from a certain 
bank (Promerica in this case).

'''
#for url requesting
from urllib.request import urlopen
#RegEx library
import re
# url from where we retrieve exchange value
print("Estableciendo conexión con el servidor...")
url = "https://www.bancopromerica.com/banca-de-empresas/banca-internacional/mesa-de-cambio/"
# if there is no internet must use a try-except
#gets the content from url
html = urlopen(url)
# gets the html content
mybytes = html.read()
# converting to utf-8 readable characters
mystr = mybytes.decode("utf8")
# search the variable tipoCambioCompra inside 
print("obteniendo tasa de cambio...")
cambio = re.search('var tipoCambioCompra = (.*);', mystr)
print("\n")

def cam():
    # group converts cambio into a float
    valor = input("Valor en dólares: ")
    print("Tasa de cambio actual:", cambio.group(1))
    #prints value limited to 4 decimals
    total = float(cambio.group(1)) * float(valor)
    print("Valor en lempiras:", format(total, '.4f'),'\n')

def loop():
    respuesta = "y"
    while True:
        if not respuesta.lower() == "y":
            print("Cerrando...")
            break
        cam()
        respuesta = input("¿Hacer otro cambio? (y/n): ")

print("Convertidor de divisas para Promerica\n")
loop()
