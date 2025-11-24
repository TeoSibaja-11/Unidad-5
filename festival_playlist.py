nombres = []
artistas = []
duraciones = []
popularidades = []


def agregar_canciones():
    cantidad = int(input("¿Cuantas canciones deseas agregar? "))
    for _ in range(cantidad):
        nombre = input("Nombre de la cancion: ")
        artista = input("Artista: ")
        duracion = float(input("Duracion (minutos): "))
        popularidad = int(input("Popularidad (1-100): "))

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print("Canciones agregadas correctamente\n")


def ver_reportes():
    if not nombres:
        print("No hay canciones registradas\n")
        return

    total_canciones = len(nombres)
    duracion_total = sum(duraciones)

    max_pop = max(popularidades)
    min_pop = min(popularidades)
    promedio_pop = sum(popularidades) / total_canciones

    idx_max = popularidades.index(max_pop)
    idx_min = popularidades.index(min_pop)

    print("===== REPORTES =====")
    print(f"Total de canciones: {total_canciones}")
    print(f"Duración total de la playlist: {duracion_total:.2f} minutos")
    print(f"Canción mas popular: {nombres[idx_max]} ({max_pop})")
    print(f"Canción menos popular: {nombres[idx_min]} ({min_pop})")
    print(f"Promedio de popularidad: {promedio_pop:.2f}\n")


def buscar_canciones():
    if not nombres:
        print("No hay canciones registradas\n")
        return

    print("1. Buscar por artista")
    print("2. Buscar por rango de popularidad")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        artista_buscar = input("Artista a buscar: ")
        print(f"\nCanciones de {artista_buscar}:")
        encontrado = False
        for i in range(len(nombres)):
            if artistas[i].lower() == artista_buscar.lower():
                print(f"- {nombres[i]} ({popularidades[i]})")
                encontrado = True
        if not encontrado:
            print("No se encontraron canciones de ese artista")
        print()

    elif opcion == "2":
        minimo = int(input("Popularidad minima: "))
        maximo = int(input("Popularidad maxima: "))
        print(f"\nCanciones con popularidad entre {minimo} y {maximo}:")
        encontrado = False
        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                print(f"- {nombres[i]} ({popularidades[i]})")
                encontrado = True
        if not encontrado:
            print("No se encontraron canciones en ese rango")
        print()

    else:
        print("Opción no valida.\n")


def playlist_recomendada():
    if not nombres:
        print("No hay canciones registradas\n")
        return

    promedio = sum(popularidades) / len(popularidades)
    print(f"\nPlaylist recomendada (popularidad > {promedio:.2f}):")

    encontrado = False
    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            print(f"- {nombres[i]} ({popularidades[i]})")
            encontrado = True

    if not encontrado:
        print("No hay canciones con popularidad superior al promedio")
    print()


def menu():
    while True:
        print("----- MENU -----")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            agregar_canciones()
        elif opcion == "2":
            ver_reportes()
        elif opcion == "3":
            buscar_canciones()
        elif opcion == "4":
            playlist_recomendada()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida... Intenta nuevamente\n")


if __name__ == "__main__":
    menu()
