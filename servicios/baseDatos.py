import csv

def cargarEquipos(ruta = "archivosCsv/tablaEquipos.csv"):
    try:
        with open(ruta, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except:
        print("no fue posible leer el archivo")
        return []
    
listaEquipos : list = cargarEquipos()


def guardarEquipos(ruta = "archivosCsv/tablaEquipos.csv"):
    try:
        with open(ruta,"w", newline="",encoding='utf-8') as file:
            encabezado = ["Equipo","jugados","ganados","empatados","perdidos","puntos"]
            writer = csv.DictWriter(file, fieldnames=encabezado)
            writer.writeheader()
            writer.writerows(listaEquipos)
    except FileExistsError:
        print("error al guardar los datos")

#-----------------------------------------------------------------------------------


def cargarParidos(ruta = "archivosCsv/historialPartidos.csv"):
    try:
        with open(ruta, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except:
        print("no fue posible leer el archivo")
        return []
    
historialPartidos : list = cargarParidos()


def guardarPartidos(ruta = "archivosCsv/historialPartidos.csv"):
    try:
        with open(ruta,"w", newline="",encoding='utf-8') as file:
            encabezado = ["fecha","local","visitante","resultado"]
            writer = csv.DictWriter(file, fieldnames=encabezado,extrasaction="ignore")
            writer.writeheader()
            writer.writerows(historialPartidos)
    except FileExistsError:
        print("error al guardar los datos")

#----------------------------------------------------------------------------------

