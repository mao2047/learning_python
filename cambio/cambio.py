'''
By mao2047

Script que revisa la tasa de cambio del dólar en la
página de Banco Promerica y realiza la conversión a
lempiras y viceversa
'''
from urllib.request import urlopen
import re

url = "https://www.bancopromerica.com/banca-de-empresas/banca-internacional/mesa-de-cambio/"

#gets the content from url
html = urlopen(url)
mybytes = html.read()
mystr = mybytes.decode("utf8")
#search the variable tipoCambioCompra inside 
cambio = re.search('var tipoCambioCompra = (.*);', mystr)
#cambio = a.group(1)

valor = input("valor en dólares: ")
print("valor en lempiras :", float(cambio.group(1)) * float(valor))
