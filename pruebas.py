import json
from main_biblio_def import buscar
from main_biblio_def import guardar

def editar ():
    libro = buscar("1984")
    if libro:
        libro["titulo"] = input("Título: ")
        libro["autor"] = input("Autor: ")
        libro["año"] = input("Año: ")
        libro["pagina"] = input("Páginas: ")
        libro["genero"] = input("Género: ")
        libro["leido"] = input("Fue leido? ")
        return libro

editar()