#Esta es una calculadora hecha con clases nada mas

class Calculadora():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):
        print(self.a + self.b)
    
    def resta(self):
        print(self.a - self.b)

    def mult(self):
        print(self.a * self.b)

    def div(self):
        print(self.a / self.b)

#-------------------#

x, y = input("ingresa dos valores separados por espacio: ").split()

miCalculadora = Calculadora(int(x), int(y))

miCalculadora.suma()
miCalculadora.resta()
miCalculadora.mult()
miCalculadora.div()

