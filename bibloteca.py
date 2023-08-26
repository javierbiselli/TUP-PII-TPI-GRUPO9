import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)


def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")


def ejemplares_prestados(codigo_libro):
    
    # completar
    return None


def eliminar_ejemplar_libro():
    # completar
    return None


def prestar_ejemplar_libro():
    codigo_libro = input('Ingrese el código del libro: ')
    libro_encontrado = None

    for libro in libros:
        if libro['cod'] == codigo_libro:
            libro_encontrado = libro
            break

    if libro_encontrado:
        print("El código de libro ha sido encontrado:")
        print("Título:", libro_encontrado["titulo"])
        print("Autor:", libro_encontrado["autor"])
        if int(libro_encontrado["cant_ej_ad"]) - int(libro_encontrado["cant_ej_pr"]) <= 0:
            print("no hay ejemplares disponibles para prestar")
        else:
            print("cantidad de ejemplares para préstamo:", int(
            libro_encontrado["cant_ej_ad"]) - int(libro_encontrado["cant_ej_pr"]))
            prestamo = input("¿Desea gestionar el préstamo de 1 unidad? (s/n): ")
            if prestamo.lower() == "s":
                libro['cant_ej_pr'] += 1
                print('Cantidad restante de ejemplares disponibles para préstamo: ', int(libro['cant_ej_ad']) - int(libro['cant_ej_pr']))
            else:
                print('no se han hecho modificaciones...')
    else:
        print("El libro no existe.")
    return None


def devolver_ejemplar_libro():
    codigo_libro = input('Ingrese el código del libro: ')
    libro_encontrado = None
    
    for libro in libros:
        if libro['cod'] == codigo_libro:
            if int(libro['cant_ej_pr']) > 0:
                libro_encontrado = libro
                print("El código del libro es válido, y hay: ",
                      libro_encontrado["cant_ej_pr"], "ejemplares prestados")
                devolucion = input("¿Desea gestionar la devolución? (s/n): ")
                if devolucion.lower() == "s":
                    libro['cant_ej_pr'] = str(int(libro['cant_ej_pr']) - 1)
                    libro['cant_ej_ad'] = str(int(libro['cant_ej_ad']) + 1)
                    print("Devolución gestionada con éxito.")
                break
            else:
                print(
                    "El código del libro es válido, pero no hay ejemplares prestados en este momento")
                break
    else:
        print("ERROR, No ha ingresado un código válido")
    return None


def nuevo_libro():
    # completar
    return None
