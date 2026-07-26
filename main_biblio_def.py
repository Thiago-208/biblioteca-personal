import json

def menu():
    print("=========BIBLIOTECA=========")
    print("1.Agregar Libro")
    print("2.Mostrar todos los Libros")
    print("3.Buscar Libro")
    print("4.Modificar Libro")
    print("5.Eliminar Libro")
    print("6.Estadísticas")
    print("7. Guardar y salir")

def libro():
   libro = {
    "titulo" : input("Título: "),
    "autor" : input("Autor: "),
    "año" : input("Año: "),
    "paginas": input("Páginas: "),
    "genero": input("Género: "),
    "leido" : input("Fue leído? ")
}
   return libro
#carga
def biblioteca():
    with open("biblioteca.json", "r", encoding="utf-8") as archivo:
        biblioteca = json.load(archivo)
    return biblioteca

def corroboracion (pregunta, dato):
    if pregunta.isdecimal():
       return int(pregunta)
    else:
        pregunta = None
        while True:
            pregunta =input(f"{dato}: ")
            if pregunta.isdecimal():
                return int(pregunta)
            
def booleano(dato):
    if dato.lower() == "si":
        return True
    elif dato.lower() == "no":
        return False
    else:
        while True:
            print("Escribe si o no")
            dato = input("Fue leído? ")
            if dato.lower() == "si":
                return True
            else:
                if dato.lower() == "no":
                    return False
#guarda
def guardar(biblioteca):
    with open ("biblioteca.json", "w", encoding="utf-8") as archivo:
        json.dump(biblioteca, archivo, indent=4, ensure_ascii=False)
#agrega
def nuevo_libro():
   biblioteca_ = biblioteca()
   libro_nuevo = libro()
   libro_nuevo["paginas"] = corroboracion((libro_nuevo["paginas"]), "Páginas")
   libro_nuevo["año"] = corroboracion((libro_nuevo["año"]), "Año")
   libro_nuevo["leido"] = booleano((libro_nuevo["leido"]))
   biblioteca_.append(libro_nuevo)
   guardar(biblioteca_)
   return libro_nuevo

def mostrar_libros():
    print(biblioteca())
    return mostrar_libros

def buscar(titulo):
    for libro in biblioteca():
        if titulo.lower() == libro["titulo"].lower():
            return libro
    return False
    
def editar_libro():
    libro = buscar(input("Título: "))
    biblioteca_ = biblioteca()
    for libro1 in biblioteca_:
        if libro1["titulo"] == libro["titulo"]:
            biblioteca_.remove(libro1)
    for clave in libro:
        dato = input(f"{clave} nuevo: ")
        libro[clave]= dato
    libro["paginas"] = corroboracion(libro["paginas"], "Páginas")
    libro["año"] = corroboracion(libro["año"], "año")
    libro["leido"] = booleano(libro["leido"])
    biblioteca_.append(libro)
    guardar(biblioteca_)

def borrar():
    libro = buscar(input("Título: "))
    biblioteca_ = biblioteca()
    for libro1 in biblioteca_:
        if libro1["titulo"] == libro["titulo"]:
            biblioteca_.remove(libro1)
    guardar(biblioteca_)