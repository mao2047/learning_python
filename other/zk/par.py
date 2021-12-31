import yaml
from yaml.loader import FullLoader


with open("index.yaml") as file:
    indices = yaml.load(file, Loader=yaml.FullLoader)

print(indices)
name2 = input("cf: ")

def check(name2):
    if name2[0] in indices.keys():
        if name2 in indices[name2[0]]:
            print("already in the list")
            name2 = input("desea modificar?: ")
            check(name2)
        else:
            if name2[:-1] in indices[name2[0]]:
                indices[name2[0]].append(name2)
                print(f"{name2} added!")
    else:
        indices[name2[0]] = [name2]
        print(f"{name2} added")

#check(name2)

with open("index.yaml", "w") as file:
    yaml.dump(indices, file, sort_keys=True)
