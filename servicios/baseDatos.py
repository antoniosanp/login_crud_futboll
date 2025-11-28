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
        with open(ruta,"w", newline="") as file:
            encabezado = ["Equipo","jugados","ganados","empatados","perdidos","puntos"]
            writer = csv.DictWriter(encabezado,listaEquipos)
            writer.writeheader()
            writer.writerows(listaEquipos)
    except:
        print("error al guardar los datos")