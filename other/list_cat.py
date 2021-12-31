list = ['1a', '2a3', '2a1c']

name2 = input("cf: ")

if name2 in list:
    print("ya esta pibe")
else:
    if name2[:-1] in list:
        print(f"{name2[:-1]} is in your box")
        list.append(name2)
        print(sorted(list))
    else:
        print("lmao")
