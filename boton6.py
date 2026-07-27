import json
from main_biblio_def import biblioteca
def estadisticas():
    print("=====ESTADISTICAS=====")
    print(f"1. Cantidad de libros: {cantidad()}")
    print(f"2. Promedio de páginas: {promedio(suma_paginas())}")
    print(f"3. Libro más largo: {libro_más_largo()} páginas")
    print(f"4. Libro más corto: {libro_más_corto()} páginas")
    print(f"5. Cantidad de leídos: {leidos()}")
    print(f"6. Cantidad de no leídos: {no_leidos()}")
    print(f"7. Porcentaje leído: {porcentaje_leido()}%")

def cantidad():
    cantidad = len(biblioteca())
    return cantidad

def suma_paginas():
    paginas = 0
    for libro in biblioteca():
        paginas = paginas+ libro["paginas"]
    return paginas

def promedio(suma_paginas):
    promedio = suma_paginas/ len(biblioteca())
    return f"{promedio:.2f}"

def ordenar():
    biblioteca_ordenada= []
    for libro in biblioteca():
        biblioteca_ordenada.append(libro["paginas"])
        biblioteca_ordenada.sort()
    return biblioteca_ordenada

def libro_más_largo():
    var = ordenar()
    return var[-1]

def libro_más_corto():
    var = ordenar()
    return var[0]


def bool():
    bool=[]
    for libro in biblioteca():
        bool.append(libro["leido"])
    return bool

def leidos():
    ver=[]
    for bul in bool():
        if bul:
            ver.append(bul)
    return len(ver)

def no_leidos():
    fal=[]
    for bul in bool():
        if not bul:
            fal.append(bul)
    return len(fal)


def porcentaje_leido():
    parte= leidos()
    total= len(bool())
    porcentaje= parte/total*100
    return f"{porcentaje:.2f}"



def porcentaje_no_leido():
    parte= no_leidos()
    total= len(bool())
    porcentaje= parte/total*100
    return int(porcentaje)