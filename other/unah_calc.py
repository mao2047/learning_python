import json


class Clase:
    def __init__(self, name, uv, year, period, grade):
        self.name = name
        self.uv = uv
        self.year = year
        self.period = period
        self.grade = grade

    def uv_grades(self):
        return self.uv * self.grade


contador = 0
dict_clases = {}

def creador():
    answer = input("deseas crear una nueva clase? (s/n): ")
    if answer == "s":
        contador += 1
        dict_clases['clase' + contador] = c




#clase1 = Clase("filosofia general", 3, 2016, 2, 85)
#clase2 = Clase("introducción a la metafisica", 3, 2016, 2, 90)



db_clases = open('db_clases', 'w')

db_clases.close()


#print(clase1.name)
#print(clase1.uv_grades())
