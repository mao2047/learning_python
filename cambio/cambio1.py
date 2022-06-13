'''
By mao2047

Script que revisa la tasa de cambio del dólar en la
página de Banco Promerica y realiza la conversión a
lempiras y viceversa
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url = "https://www.bancopromerica.com/banca-de-empresas/banca-internacional/mesa-de-cambio/"
html = urlopen(url)
mybytes = html.read()
mystr = mybytes.decode("utf8")

#print(mystr)
#soup = BeautifulSoup(html, features="html.parser")
#soup = BeautifulSoup = (html)
#script = soup.find("")
#print(soup)
# kill all script and style elements
#print(mystr)
a = re.search('var tipoCambioCompra = (.*);', mystr)
print(a.group(1))
#for script in soup(["script"]):
#    print(script)
#    print(type(script))# rip it out
#scripts = soup.find_all('script')
# get text
#soup = BeautifulSoup(web.read(), "lxml")
#scripts = soup.find_all('script')
#text = a.find("var = tipoCambioCompra")

#print(soup)
