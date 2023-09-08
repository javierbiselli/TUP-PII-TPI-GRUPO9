import cod_generator as cg

# Crear un diccionario para cada libro
libro1 = {
    "cod": "CRBJsAkS",
    "cant_ej_ad": 3,
    "cant_ej_pr": 1,
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
}
libro2 = {
    "cod": "QgfV4j3c",
    "cant_ej_ad": 4,
    "cant_ej_pr": 2,
    "titulo": "El Ingenioso Hidalgo Don Quijote De La Mancha",
    "autor": "Miguel DeCervantes",
}
libro3 = {
    "cod": "adOd09UE",
    "cant_ej_ad": 2,
    "cant_ej_pr": 1,
    "titulo": "Fortunata y Jacinta",
    "autor": "Benito Perez Galdos",
}


def nuevo_libro(lista, item):
    lista.append(item)
    return None


def generar_codigo():
    codigo = cg.generar()
    return codigo
