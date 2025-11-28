import csv

def leerFile():
    try:
        with open("archivosCsv/usuarios.csv", "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except:
        print("error al leer archivo")
        return []

claves = leerFile()


def validarLogin() -> bool:
    for i in range(3):
        userName = input("user name: ")
        userPassword = input("user password: ")

        for user in claves:
            if userName == user['user'] and userPassword == user['password']:
                print(f"welcome: {userName}")
                return True
            else:
                continue
        print(f"usuario o contraseña incorrectos\nintentos restantes: {2 - i}")
    print("excediste el limite de intentos")
    return False

