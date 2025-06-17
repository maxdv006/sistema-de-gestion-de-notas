estudiantes = {}

while True:
    print("Seleccione una opcion:")
    print("1. Agregar estudiante & notas")
    print("2. Consultar notas de un estudiante")
    print("3. Ver todos los estudiantes y promedios")
    print("4. Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        notas = []

        for i in range(3):
            nota = float(input(f"Ingrese la nota {i+1}: "))
            notas.append(nota)

        estudiantes[nombre] = notas
        print("Notas guardadas exitosamente.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre in estudiantes:
            print(f"Notas de {nombre}: {estudiantes[nombre]}")
        else:
            print("Ese estudiante no esta cargado.")

    elif opcion == "3":
        if len(estudiantes) == 0:
            print("No hay estudiantes cargados.")
        else:
            for nombre, notas in estudiantes.items():
                promedio = sum(notas) / len(notas)
                print(f"{nombre} → Notas: {notas} → Promedio {promedio:.2f}")

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opcion invalida, intenta de nuevo.")
