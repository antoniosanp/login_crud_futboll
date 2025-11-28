from baseDatos import *

def validarStr(texto):
    print(texto)

    while True:
        name = input().strip()
        if name != "":
            return name
        print("el nombre no puede ser vacio")
        

def createNewEquipo(name:str) -> dict:
    newEquipo = {
        #["Equipo","jugados","ganados","empatados","perdidos","puntos"]
        "name": name,
        "jugados" : 0,
        "ganados" : 0,
        "empatados" : 0,
        "perdidos" : 0,
        "puntos" : 0
    }
    return newEquipo

def findEquipo(name:str) -> dict:
    for equipo in listaEquipos:
        if equipo['name'] == name:
            return equipo
    return None

def addNewEquipo(name:str) -> None:
    equipo = findEquipo(name)
    if equipo:
        print(f"ya existe el equipo: {name}")
        return
    else:
        listaEquipos.append(createNewEquipo(name))
