def crear_sala(filas, columnas):
    return [["L" for _ in range(filas)] for _ in range(columnas)]

def mostrar_sala(sala):
    print("\nEstado actual de la sala:\n")
    for fila in sala:
        print(" ".join(fila))
    print()


def validar_asiento(sala, f, c):
    filas = len(sala)
    columnas = len(sala[0])
    return 0 <= f < filas and 0 <= c < columnas


def reservar_asiento(sala):
    while True:
        try:
            f = int(input("Fila del asiento: ")) - 1
            c = int(input("Columna del asiento: ")) - 1
        except ValueError:
            print(" Ingresar numeros validos\n")
            continue

        if not validar_asiento(sala, f, c):
            print(" No existe asiento...")
            print("Intente de nuevo\n")
            continue

        if sala[f][c] == "X":
            print(" Ese asiento esta ocupado... Eliga otro\n")
            continue

        sala[f][c] = "X"
        print(" Asiento reservado con exito.\n")
        break


def liberar_asiento(sala):
    while True:
        try:
            f = int(input("Fila del asiento: ")) - 1
            c = int(input("Columna del asiento: ")) - 1
        except ValueError:
            print(" Ingresar numeros validos\n")
            continue

        if not validar_asiento(sala, f, c):
            print(" Ese asiento no existe...")
            print("Intenta nuevamente\n")
            continue

        if sala[f][c] == "L":
            print(" Ese asiento ya esta libre... Eliga otro\n")
            continue

        sala[f][c] = "L"
        print(" Asiento liberado exitosamente\n")
        break


def contar_asientos(sala):
    ocupados = sum(fila.count("X") for fila in sala)
    libres = sum(fila.count("L") for fila in sala)
    print(f"\n Estadísticas:")
    print(f"   Asientos ocupados: {ocupados}")
    print(f"   Asientos libres:   {libres}\n")



print(" ASIENTOS DE CINE \n")

filas = int(input("Numero de filas: "))
columnas = int(input("Numero de columnas: "))

sala = crear_sala(filas, columnas)

while True:
    print("""
------- MENU -------
1. Mostrar sala
2. Reservar asiento
3. Liberar asiento
4. Contar asientos ocupados y libres
5. Salir
""")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        mostrar_sala(sala)

    elif opcion == "2":
        reservar_asiento(sala)

    elif opcion == "3":
        liberar_asiento(sala)

    elif opcion == "4":
        contar_asientos(sala)

    elif opcion == "5":
        print("\n QUE DISFRUTE SU PELICULA\n")
        break

    else:
        print(" Opción no valida...") 
        print("Intenta nuevamente\n")