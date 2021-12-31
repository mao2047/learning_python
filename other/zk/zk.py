import sys, tempfile, os
sys.getdefaultencoding
from subprocess import call 
import yaml
from yaml.loader import SafeLoader


class Fleeting_note:
    def __init__(self):
        self.name = input("name: ")
        self.date = input("yyyy-mm-dd: ")
        self.ref = "fn" + input("cf: ")
        self.content = input("contenido de la nota\n: ")


    def __repr__(self):
        return self.content


def write_fn():
    note = Fleeting_note()
    #with open('index.yaml') as file:
    #    data_index = yaml.load(file, Loader=SafeLoader)
    #    print(data_index)
        #if note.ref in data_index:
        #    print("yes")
        #else:
        #    data_index.append(note.ref)
        #yaml.dump(data_index, file, sort_keys=True)
# Creating note
    with open(f'./notes/fn/{note.ref}.yaml', 'w') as file:
        yaml.dump(note.__dict__, file, sort_keys=False)
