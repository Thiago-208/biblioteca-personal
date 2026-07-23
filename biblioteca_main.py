from main_biblio_def import nuevo_libro
from main_biblio_def import menu
from main_biblio_def import mostrar_libros
from main_biblio_def import buscar
from main_biblio_def import editar_libro

while True:
    menu()
    boton = int(input("Presiona un botón: "))
    if boton == 1:
        libro_nuevo = nuevo_libro()
    if boton == 2:
        mostrar_libros()
    if boton == 3:
        buscar()
    if boton == 4:
        editar_libro()