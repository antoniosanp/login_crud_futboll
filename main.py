from servicios.crudEquipos import partidoMenu, printPartidos, printTablaEquipos
from servicios.validateLogin import validarLogin

login = validarLogin()

while login:
    print("\n------------FPC-----------\n")

    print("1: Anotar Resultados ")
    print("2: Tabla de Posiciones")
    print("3: Historial de Partidos")
    print("4: Salir\n")

    opcion = input()

    match opcion:
        case "1":
            partidoMenu()
        case "2":
            printTablaEquipos()
        case "3":
            printPartidos()
        case "4":
            break
        case _: print("opción inválida")

    