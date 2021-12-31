#080 

def name_length():
    name = input("write ypur name: " )
    print(f"the length of {name} is {len(name)}")
    surname = input("write your surename: ")
    print(f"the length of {surname} is {len(surname)}")
    fullname = name + " " + surname
    print(f"your full name is: {fullname}\nthe length is {len(fullname)}")

#081
def name_sep():
    subject = input("what is your favourite subject at college?: ")
    for letter in subject.replace(" ", ""):
        print(letter, end='-')


#082

def uppercase_message():
    word = input("write a word in uppercase: ")
    check = False
    while check == False:
         if word.isupper():
            print(f"{word} is all in uppercase")
            return True
         else:
            print("Try again")
            word = input("write a word in uppercase: ")

#084

def postal():
    postal_code = input("type your postal code (aa000): ")
    print(f"{postal_code[:2].upper()}{postal_code[2:]}")


def vowel_count():
    arevowels = ['a', 'e', 'i', 'o', 'u']
    name = input("What is your name?: ")
    vcount = 0
    
    for char in name.lower():
        if char in arevowels:
            vcount +=1
    print(f"There are {vcount} vowels in {name}")


def password_checker():
    pass1 = input("Enter your password: ")
    pass2 = input("Enter your password again: ")

    if pass1 == pass2:
        print("Thank you")
    else:
        if pass1.lower() == pass2.lower():
            print("They must be in the same case")
        else:
            print("incorrect")


def backwards():
    word = input("introduce a word: ")
    word = word[::-1]
    for char in word:
        print(char)




backwards()
#password_checker()
#vowel_count()
#postal()
#up_mes()
#name_length()
#name_sep()
