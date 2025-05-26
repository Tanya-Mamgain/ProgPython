#DICTIONARY DEFINITION

marks = {
    "Tanya":100,
    "Gulshan":90,
    "Bullet":80
}

print(marks,type(marks))
print(marks["Tanya"])   #to print a value address it's key
print("Distionary Methods")
print(marks.items())
print("\n\n")
print(marks.keys())
print("\n\n")
print(marks.values())

#update()
marks.update({"harry":99,"Renuka":100})
print("\n\n\n\n")
print(marks)


#get()
print(marks.get("Tanya"))
print(marks["Tanya"])

print("\n\n\n")

print(marks.get("swati"))
print(marks["swati"])