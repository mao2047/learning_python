#069 - 070
def countries_sel():
    countries = ("Honduras", "Cuba", "China", "Venezuela", "Rusia")
    ask = input("check a country: ")
    if ask.isdigit() is True:
        ask = int(ask) 
        if ask < len(countries):
            print(f"{countries[ask]} have index {ask}")
        else:
            print(f"There is no country with {ask} index")
    else:
        ask = ask.capitalize()
        if ask in countries:
            print(f"{ask} is number {countries.index(ask)}")
        else:
            print(f"{ask} not in the list")

#071

def fav_sport():
    sports = ["futbol", "natacion", "rugby", "ajedrez", "tennis", "baseball"]
    respuesta = input("cual es tu deporte favorito?: ")
    if respuesta not in sports:
        sports.append(respuesta)
        print(f"{respuesta} fue añadida a la lista")
        print(sports)
    else:
        print(f"Genial, {respuesta} ya esta en la lista!")

#072

def subjetcs_hate():
    subjects = ["matematicas", "quimica", "filosofia", "deporte", "fisica", "musica"]
    for item in range(len(subjects)):
        print(f"{item} : {subjects[item]}")
    respuesta = int(input("¿cual es tu materia menos favorita? \n: "))
    if respuesta in range(len(subjects)):
        print(subjects.pop(respuesta))
        print(subjects)
    else:
        print("try again")

#073

def food_picker():
    comidas = {}
    i = 1
    print("cuales son tus 4 platos favoritos?")
    while i < 5:
        plato = input("ingresa plato: ")
        comidas[i] = plato
        i += 1
    print(comidas)
    eleccion = int(input("que comida deseas eliminar?: "))
    del comidas[eleccion]
    print(comidas)


#074

def two_colours():
    colours = ['red', 'blue', 'white', 'black', 'green', 'yellow', 'purple', 'gray', 'brown', 'pink']
    a = int(input("choose a number between 0 and 4: "))
    b = int(input("choose a number betwen 5 and 9: "))
    print(colours[a:b])


#075

def three_digits():
    numberlist = [795, 403, 667, 210]
    for item in numberlist:
        print(item)
    choose = int(input("enter a 3 digit number: "))
    if choose in numberlist:
        print(numberlist.index(choose))
    else:
        print("That is not in the list")


#076-077---------------------------------------------------

def friend_list():
    friendlist = []

    def adder():
        friend = input("enter guest name: ")
        if friend == "no":
            return friend
        else:
            friendlist.append(friend)

    for friend in range(0, 3):
        adder()
    answer = input("what to add more guests? (yes/no) :")
    
    if answer == "yes":
        while friend != "no":
            friend = adder()
        print(f"you have invited {len(friendlist)} friends \n")
        answer = input("wanna uninvite someone? (yes/no): ")
        if answer == "yes":
            for item in range(len(friendlist)):
                print(f"{item} : {friendlist[item]}")
            selection = int(input("select a guess to delete: "))
            friendlist.pop(selection)
            print(friendlist)
        else:
            print(friendlist)
'''
hacer un programa completo para agregar y borrar guests
'''

#078---------------------------------------------------------------

def tv_shows():
    shows = ['Rugrats', 'the office', 'ovnis ancestrales', 'bar rescue']
    
    def shower():
        for show in range(len(shows)):
            print(f"{show} : {shows[show]}")
    
    shower()
    
    new_show = input("Agrega un show: ")
    new_pos = int(input("en que posicion?: "))
    shows.insert(new_pos, new_show)

    shower()

#079----------------------------------------------------------------

def num_chooser():
    nums = []
    i = 0
    while True:
        numero = input(": ")
        if numero == 'n':
            break
        else:
            nums.append(int(numero))
        i += 1
        if i == 3:
            answer = input("keep adding numbers? (y/n)")
            if answer == 'y':
                pass
            else:
                break
    print(nums)

#

#countries_sel()
#fav_sport()
#subjetcs_hate()
#food_picker()
#two_colours()
#three_digits()
#friend_list()
#tv_shows()
num_chooser()
