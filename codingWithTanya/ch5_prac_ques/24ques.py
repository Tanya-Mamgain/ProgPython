# CREATE AN EMPTY DICTINARY. ALLOW 4 FRIENDS TO ENTER THEIR FAVORAIT LANGUAGE AS A VALUE 
# AND USE KEYS AS THEIR NAMES. ASSUME THAT THE NAMES ARE UNIQUE
d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})


print(d)