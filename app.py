# Trabajo Práctico I - Programación II


import os
from bibloteca import *


def menu():
    print("|--------------------------------------|")
    print("|1 - Gestionar Prestamo                |")
    print("|2 - Gestionar Devolucion              |")
    print("|3 - Registrar nuevo libro             |")
    print("|4 - Eliminar ejemplar                 |")
    print("|5 - Mostrar ejemplares prestados      |")
    print("|6 - Salir                             |")
    print("|--------------------------------------|\n")



print("Bienvenido!")
respuesta = ''

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system("cls")
    if opt.isnumeric():
        if int(opt) == 1:
            prestar_ejemplar_libro()
        elif int(opt) == 2:
            devolver_ejemplar_libro()
        elif int(opt) == 3:
            registrar_nuevo_libro()
        elif int(opt) == 4:
            eliminar_ejemplar_libro()
            print("this feature is pending...")
        elif int(opt) == 5:
           print("this feature is pending...")
        elif int(opt) == 6:
            respuesta = "salir"
        else:
            print("Ingrese una opción válida")
    else:
        print("Ingrese una opción numérica")

    input("Presione cualquier tecla para continuar....")  # Pausa
    os.system("cls")

print("--------------------------------------")
print("|        ...Hasta luego!...          |")
print("--------------------------------------")
