#!/usr/bin/env python

"""Programa que lista algo x

"""


import requests
from lxml import html
import urlparse
import sys
import validators

def sep(pagina=''):
    base=pagina
    try:
        pagina=html.fromstring(requests.get(pagina).text).xpath('//div[@id="article-content"]')[0]
    except:
        sys.exit(1)
    #Se agrega la siguiente linea para cambiar ../ por la ruta original.
    for imgs in pagina.xpath('//img'):
        try:
            imgs.attrib["src"]=urlparse.urljoin(base,imgs.attrib["src"])
        except:
            continue
    for links in pagina.xpath('//a'):
        try:
            if links.attrib["href"].startswith('#'):
                continue
            links.attrib["href"]=urlparse.urljoin(base,links.attrib["href"])
        except:
            continue
    archivo=open('out.html','w')
    archivo.write(html.tostring(pagina))
    archivo.close()
    

if __name__=='__main__':
    argumentos=sys.argv
    if validators.url(sys.argv[1]):
        sep(sys.argv[1])
    else:
        if validators.domain(sys.argv[1]):
            sep('http://'+sys.argv[1])
    #busqueda=''
    #for x in argumentos[1:]:
        #busqueda=str(x)+'+'
    #if busqueda=='':
        #listax()
    #else:
        #listax(busqueda)

