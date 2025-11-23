estudiantes = int(input("Numero de estudiantes: "))
materias = int(input("¿Cuantas materias lleva cada estudiante? "))

matriz = []
print("\n Captura de calificaciones ")
for i in range(estudiantes):
    fila = []
    print(f"\nEstudiante {i+1}:")
    for j in range(materias):
        cal = float(input(f" Calificacion en la materia {j+1}: "))
        fila.append(cal)
    matriz.append(fila)

pro_estudiante = [sum(fila)/materias for fila in matriz]

pro_materia = []
for j in range(materias):
    col = [matriz[i][j] for i in range(estudiantes)]
    pro_materia.append(sum(col)/estudiantes)

todas = [cal for fila in matriz for cal in fila]
maxima = max(todas)
minima = min(todas)

print("\n Resultados ")
for i, pro in enumerate(pro_estudiante):
    print(f"Promedio del estudiante {i+1}: {pro:.2f}")

print()
for j, pro in enumerate(pro_materia):
    print(f"Promedio de las materias {j+1}: {pro:.2f}")

print(f"\ncalificacion mas alta: {maxima}")
print(f"calificación mas baja: {minima}")
