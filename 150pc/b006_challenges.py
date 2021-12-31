import random

#052
def random_number():
    return (random.randint(0,100))


#053
def random_fruit():
    frutas = ["nance", "mamones", "bananos", "guanabana", "sarsiles", "uvitas", "zapote", "fresa", "naranja"]
    return (frutas[(random.randint(0, len(frutas)-1))])


#054
def head_or_tail():
    stuff = {1:"tail", 2:"head"}
    com_choice = random.randint(1,2)
    print(stuff[com_choice])


#055
def guess_number():
    choice = int(input("choose a number: "))
    com_choice = random.choice(range(1, 6))
    if choice == com_choice:
        print("Well done")
    else:
        print("try again")
        choice = int(input("choose a number: "))
        if choice == com_choice:
            print("you win!")
        else:
            print("you lose")


#056- 057
def random_hidden():
    machine = random.choice(range(1, 11))
    while True:
        choice = int(input("choose a number: "))
        if choice == machine:
            print("you win!")
            break
        else:
            if choice >= machine:
                print("too high")
                pass
            else:
                print("too low")
                pass


#058
puntos = 0
def math_quiz():
    counter = 0
    def op():
        global puntos
        a, b = random.randint(1, 10), random.randint(1, 10)
        operandos = ("+", "-", "*", "/") # , "**")
        operacion = {"+":(a+b), "-":(a-b), "*":(a*b), "/":(a/b)} #"**":(a**b)}
        signo = operandos[random.randint(1, len(operandos)-1)]
        solucion = operacion[signo]
        if signo == "/":
            solucion = round(solucion, 2)
        respuesta = float(input(f"{a} {signo} {b} = "))
        if respuesta == solucion:
            puntos += 1
        else:
            print(f"respuesta incorrecta, es {solucion}")
            pass
#    
    while counter < 5:
        op()
        counter +=1    
    print(f"tu puntaje es {puntos}")



#    if signo == "/":
#        if b == 0:
#            a, b = b, a
# only for b = 0

   # print(f"{a} {signo} {b}")
   # print(respuesta)


    #while counter <= 5:
     #   pass


#print(random_fruit(), random_number())
#head_or_tail()
#guess_number()
#random_hidden()
math_quiz()
