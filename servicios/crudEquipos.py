from baseDatos import *

def validarStr(texto:str) -> str:
    print(texto)

    while True:
        name = input().strip()
        if name != "":
            return name
        print("el nombre no puede ser vacio")

def validarInt(text: str) -> int:
    while True:
        try:
            entero = int(input(text))
            if entero >= 0: return entero
            else: print("los goles no pueden ser negaticos")
        except ValueError:
            print("ingrese una cantidad positiva")
        
#-----------------------------------------------------------------------------------------
def createNewEquipo(name:str) -> dict:
    newEquipo = {
        #["Equipo","jugados","ganados","empatados","perdidos","puntos"]
        "Equipo": name,
        "jugados" : 0,
        "ganados" : 0,
        "empatados" : 0,
        "perdidos" : 0,
        "puntos" : 0
    }
    return newEquipo

def findEquipo(name:str) -> dict:
    for equipo in listaEquipos:
        if equipo['Equipo'] == name:
            return equipo
    return None

def addNewEquipo(name:str) -> None:
    equipo = findEquipo(name)
    if equipo:
        print(f"ya existe el equipo: {name}")
        return
    else:
        listaEquipos.append(createNewEquipo(name))
        guardarEquipos()

def addNewEquipoMenu():
    print("\n---------------Agregar nuevo equipo---------------\n")
    name = validarStr("Equipo: ")
    addNewEquipo(name)

#--------------------------------------------------------------------------------------

def printEquipo(equipo:dict):
    print(f"Equipo: {equipo['Equipo']:<10} | Paridos Jugados: {equipo['jugados']:<5} | Ganados: {equipo['ganados']:<5} | Empatados: {equipo['empatados']:<5} | Perdidos: {equipo['perdidos']:<5} | Puntos: {equipo['puntos']:<5} ")

def printTablaEquipos():
    for equipo in listaEquipos:
        printEquipo(equipo)

#-------------------------------------------------------------------------------------

def calcPatido(golesA : int, golesB: int) -> str:
    resultado = ""
    if golesA == golesB:
        resultado = "empate"
    
    else:
        resultado = "equipoA" if golesA > golesB else "equipoB"
    
    return resultado

def actualizarTabla(equipoA:dict, equipoB:dict, resultado: str):

    equipoA['jugados'] = int(equipoA['jugados']) + 1
    equipoB['jugados'] = int(equipoB['jugados']) + 1

    

    if resultado == "empate":
        equipoA['empatados'] = int(equipoA["empatados"]) + 1
        equipoB['empatados'] = int(equipoB["empatados"]) + 1
        equipoA["puntos"] = int(equipoA["puntos"]) + 1
        equipoB["puntos"] = int(equipoB["puntos"]) + 1
    
    if resultado == "equipoA":
        equipoA['ganados'] = int(equipoA["ganados"]) + 1
        equipoB['perdidos'] = int(equipoB["perdidos"]) + 1
        equipoA['puntos'] = int(equipoA["puntos"]) + 3

    if resultado == "equipoB":
        equipoB['ganados'] = int(equipoB["ganados"]) + 1
        equipoA['perdidos'] = int(equipoA["perdidos"]) + 1
        equipoB['puntos'] = int(equipoB["puntos"]) + 3
    guardarEquipos()

def partidoMenu():
    A = validarStr("Equipo local: ")
    B =  validarStr("Equipo visitante: ")

    equipoA = findEquipo(A)
    equipoB = findEquipo(B)

    if not equipoA or not equipoB:
        print(f"No existe uno de los equipos: ({A}) p ({B})")
        return
    print("\n Marcador Final: ")

    golesA = validarInt(f"Goles de {A}: ")
    golesB = validarInt(f"Goles de {B}: ")
    
    resultado = calcPatido(golesA,golesB)
    actualizarTabla(equipoA,equipoB,resultado)

#--------------------------------------------------------
printTablaEquipos()

partidoMenu()
partidoMenu()

printTablaEquipos()