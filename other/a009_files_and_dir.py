from pathlib import Path

#absolute path

#relative path 
#without argumment Path will point to
# current directory
path = Path("ecommerce")
print(path.exists())

path = Path("emails")
if path.exists() is False:
    path.mkdir() #creates a dir
    print("emails dir created")
    path.rmdir()
else:
    pass

#iterate and process dirs
#search all py
path = Path('ecommerce')
for file in path.glob('*.py'):
    print(file) #prints all .py files
