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

def guardar(libro):
    with open ("biblioteca.json", "r", encoding="utf-8") as archivo:
        biblioteca = json.load(archivo)
    with open ("biblioteca.json", "w", encoding="utf-8") as archivo:
        biblioteca.append(libro)
        json.dump(biblioteca, archivo, indent=4, ensure_ascii=False)
    with open ("biblioteca.json", "r", encoding="utf-8") as archivo:
        biblioteca = json.load(archivo)
    return biblioteca

def nuevo_libro():
   libro_nuevo = libro()
   libro_nuevo["paginas"] = corroboracion((libro_nuevo["paginas"]), "Páginas")
   libro_nuevo["año"] = corroboracion((libro_nuevo["año"]), "Año")
   libro_nuevo["leido"] = booleano((libro_nuevo["leido"]))
   guardar(libro_nuevo)
   return libro_nuevo

def mostrar_libros():
    print(biblioteca())
    return mostrar_libros

def buscar(titulo):
    biblioteca()
    for libro in biblioteca():
        if titulo.lower() == libro["titulo"]:
            return libro
        return False
    
def editar_libro():
    libro = buscar(input("Título: "))
    print(libro)
    libro["autor"] = "Hola mundo!"