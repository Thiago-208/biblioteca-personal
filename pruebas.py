with open("biblioteca.json", "w", encoding="utf-8") as archivo:
    json.dump(biblioteca, archivo, indent=4, ensure_ascii=False)



    biblioteca.append(nuevo_libro)

    biblioteca =[]