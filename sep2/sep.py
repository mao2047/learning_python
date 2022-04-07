#!/usr/bin/env python

"""
Stanford Encyclopedia of Philosophy aticles scrapper
By mao2047

"""

import requests
import sys
from lxml import html
from urllib.parse import urlparse
import validators

def sep(pagina=''):
    base = pagina
    try:
        pagina = html.fromstring(requests.get(pagina).text).xpath('//div[@id="article-content"]')[0]
    except:
        sys.exit(1)
    # La siguiente linea cambia ../ por la ruta original
    for imgs in pagina.xpath('//img'):
        try:
            imgs.attrib["src"]=urlparse.join(base,imgs.attrib["src"])
        except:
            continue
        for links in pagina.xpath('//a'):
            try:
                if links.attrib["href"].startswith('w'):
                    continue
                links.attrib["href"]=urlparse.urljoin(base,links.attrib["href"])
            except:
                continue
    #escritura del archivo como "out.html"
    nombre1 = sys.argv[1]
    #Se tomará el nombre de la url, luego de "entries/" y removiendo /
    nombre2 = nombre1.split("entries/",1)[1].removesuffix('/')+'.html'
    #se debe guardar wb para utilizar binarios
    archivo=open(nombre2,'wb')
    archivo.write(html.tostring(pagina))
    archivo.close()
#----------------------
if __name__ == '__main__':
    argumentos = sys.argv
    if validators.url(sys.argv[1]):
        sep(sys.argv[1])
    else:
        #añade el protocolo http:// al nombre
        if validators.domain(sys.argv[1]):
            sep('http://'+sys.argv[1])
