from servicios.crudEquipos import partidoMenu, printPartidos,ordenarEquipos, modificarFechaMenu
from servicios.validateLogin import validarLogin
from servicios.baseDatos import historialPartidos


login = validarLogin()

while login:
    print("\n------------FPC-----------\n")

    print("1: Anotar Resultados ")
    print("2: Tabla de Posiciones")
    print("3: Historial de Partidos")
    print("4: Modificar fecha")
    print("5: Salir\n")

    opcion = input()

    match opcion:
        case "1":
            partidoMenu()
        case "2":
            ordenarEquipos()
        case "3":
            printPartidos()
        case "4":
            modificarFechaMenu()
        case "5":
            break
        case _: print("opción inválida")

    