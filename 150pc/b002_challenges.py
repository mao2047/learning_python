'''
challenges from python by example
'''

#b020
def namesize():
    name_to_size = input("What is your name?: ").replace(" ", "")
    print(len(name_to_size))


#b025
def smallname():
    name_to_change = input("what is your fist name?: ")

    if len(name_to_change) < 5:
        surname_to_join = (input("what is your surname?: "))
        print(f"{name_to_change.upper()}{surname_to_join.upper()}")
    else:
        print(name_to_change.lower())


#b026
def piglatin():
    message = input("enter your message: ").lower()
    mes_list = message.split()
    vowels = ("a", "e", "i", "o", "u")
    mes_pig_latin = []
    
    for word in mes_list:
        if word[0] in vowels:
            n = word[1:] + word[:1] + "way"
            mes_pig_latin.append(n)
        else:
            n = word[1:] + word[:1] + "ay"
            mes_pig_latin.append(n)

    print(' '.join(mes_pig_latin))


#smallname()
