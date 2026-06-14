import csv
from funciones_secundarias import *

# Permite buscar un país por coincidencia exacta o parcial.
def mostrar_pais(paises):
  
    encontrado=False
  
    while True:
        nombre_pais=input("Ingresar el nombre del país: ").strip().title()
  
        if validacion_input(nombre_pais):
            break

    # Resultado exacto.
    for i in paises:
        if nombre_pais==i["nombre"]:
            print(f"País: {i['nombre']} | Población: {i['poblacion']} | Superficie {i['superficie']} | Continente: {i['continente']}")
            encontrado=True
            return
    
    # Resultado parcial.
    print("Resultado parcial:")
    for i in paises:        
        if nombre_pais in i["nombre"]:
            print(f"País: {i['nombre']} | Población: {i['poblacion']} | Superficie {i['superficie']} | Continente: {i['continente']}")
            encontrado=True                        
  
    if not encontrado:
        print("No se encontró el país.")

# Agrega países junto con sus datos (población, superficie y continente).
def agregar_pais(paises):

    while True:
        nombre = input("Ingresar nombre del país: ").strip().title()

        if validacion_input(nombre):
            break

    for i in paises:
        if i["nombre"] == nombre:
            print("Ese país ya existe.")
            return

    continente=seleccionar_continente()

    while True:
        try:
            poblacion = int(input("Ingresar población: "))

            if poblacion <= 0:
                print("La población no puede ser negativa, o igual a cero.")
                continue
            
            break

        except ValueError:
            print("Solo se deben ingresar números enteros.")

    while True:
        try:
            superficie = int(input("Ingresar superficie: "))

            if superficie <= 0:
                print("La superficie no puede ser negativa, o igual a cero.")
                continue

            break

        except ValueError:
            print("Solo se deben ingresar números enteros.")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    # Se guarda en la lista
    paises.append(nuevo_pais)

    # Se guarda en el archivo.CSV
    with open("paises.csv", "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(
            archivo,
            fieldnames=["nombre", "poblacion", "superficie", "continente"]
        )
        escritor.writerow(nuevo_pais)

    print("País agregado correctamente.")

# Muestra las estadísticas.
def mostrar_estadisticas(paises):

    mayor_poblacion = paises[0]
    menor_poblacion = paises[0]

    suma_poblacion = 0
    suma_superficie = 0

    america = 0
    europa = 0
    asia = 0
    africa = 0
    oceania = 0
    antartida = 0

    for i in paises:

        suma_poblacion += i["poblacion"]
        suma_superficie += i["superficie"]

        if i["poblacion"] > mayor_poblacion["poblacion"]:
            mayor_poblacion = i

        if i["poblacion"] < menor_poblacion["poblacion"]:
            menor_poblacion = i

        if i["continente"] == "America":
            america += 1

        elif i["continente"] == "Europa":
            europa += 1

        elif i["continente"] == "Asia":
            asia += 1

        elif i["continente"] == "Africa":
            africa += 1

        elif i["continente"] == "Oceania":
            oceania += 1

        elif i["continente"] == "Antartida":
            antartida += 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print("\nESTADÍSTICAS\n")

    print(
        f"País con mayor población: "
        f"{mayor_poblacion['nombre']} "
        f"({mayor_poblacion['poblacion']} habitantes)"
    )

    print(
        f"País con menor población: "
        f"{menor_poblacion['nombre']} "
        f"({menor_poblacion['poblacion']} habitantes)"
    )

    print(
        f"Promedio de población: "
        f"{promedio_poblacion:.2f}"
    )

    print(
        f"Promedio de superficie: "
        f"{promedio_superficie:.2f}"
    )

    print("\nCantidad de países por continente:")

    print(f"América: {america}")
    print(f"Europa: {europa}")
    print(f"Asia: {asia}")
    print(f"África: {africa}")
    print(f"Oceanía: {oceania}")
    print(f"Antártida: {antartida}")

# Ordenar países.
def ordenar_paises(paises):

    print("Seleccionar criterio de ordenamiento:")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    while True:
        try:
            opcion = int(input("Opción: "))

            if opcion not in [1, 2, 3]:
                print("Debe ingresar una opción válida.")
                continue

            break

        except ValueError:
            print("Solo se deben ingresar números enteros.")

    while True:
        try:
            orden = int(input("1. Ascendente | 2. Descendente: "))

            if orden not in [1, 2]:
                print("Debe ingresar una opción válida.")
                continue

            break

        except ValueError:
            print("Solo se deben ingresar números enteros.")

    reverso = False

    if orden == 2:
        reverso = True

    if opcion == 1:
        paises_ordenados = sorted(
            paises,
            key=lambda pais: pais["nombre"],
            reverse=reverso
        )

    elif opcion == 2:
        paises_ordenados = sorted(
            paises,
            key=lambda pais: pais["poblacion"],
            reverse=reverso
        )

    elif opcion == 3:
        paises_ordenados = sorted(
            paises,
            key=lambda pais: pais["superficie"],
            reverse=reverso
        )

    print("\nListado ordenado:\n")

    for i in paises_ordenados:
        print(
            f"País: {i['nombre']} | "
            f"Población: {i['poblacion']} | "
            f"Superficie: {i['superficie']} | "
            f"Continente: {i['continente']}"
        )

# Filtra países segun la opción. 
def filtrar_paises(paises):
    print("Ingresar la opción de filtro:")
    print("1. Continente")
    print("2. Rango de población")
    print("3. Rango de superficie")

    while True:
        try:
            opcion_filtro = int(input("Opción: "))
            if opcion_filtro not in [1, 2, 3]:
                print("Debe ingresar una opción válida.")
                continue
            break
        except ValueError:
            print("No se deben ingresar letras o espacios vacíos. Ingrese un número.")
            
    if opcion_filtro == 1:
        
        continente=seleccionar_continente()
        
        encontrado = False
        for i in paises:
            if i["continente"].title() == continente:
                print(f"País: {i['nombre']} | Población: {i['poblacion']} | Superficie: {i['superficie']} | Continente: {i['continente']}")
                encontrado = True
        if not encontrado:
            print("No se encontraron países para ese continente.")

    elif opcion_filtro == 2:
        while True:
            try:
                poblacion_min = int(input("Ingresar población mínima: "))
                poblacion_max = int(input("Ingresar población máxima: "))
                if poblacion_min < 0 or poblacion_max < 0:
                    print("La población no puede ser negativa.")
                    continue
                if poblacion_min > poblacion_max:
                    print("La población mínima no puede ser mayor que la máxima.")
                    continue
                break
            except ValueError:
                print("Solo se deben ingresar números enteros.")
        encontrado = False
        for i in paises:
            if poblacion_min <= i["poblacion"] <= poblacion_max:
                print(f"País: {i['nombre']} | Población: {i['poblacion']} | Superficie: {i['superficie']} | Continente: {i['continente']}")
                encontrado = True
        if not encontrado:
            print("No se encontraron países en ese rango de población.")

    elif opcion_filtro == 3:
        while True:
            try:
                superficie_min = int(input("Ingresar superficie mínima: "))
                superficie_max = int(input("Ingresar superficie máxima: "))
                if superficie_min < 0 or superficie_max < 0:
                    print("La superficie no puede ser negativa.")
                    continue
                if superficie_min > superficie_max:
                    print("La superficie mínima no puede ser mayor que la máxima.")
                    continue
                break
            except ValueError:
                print("Solo se deben ingresar números enteros.")
        encontrado = False
        for i in paises:
            if superficie_min <= i["superficie"] <= superficie_max:
                print(f"País: {i['nombre']} | Población: {i['poblacion']} | Superficie: {i['superficie']} | Continente: {i['continente']}")
                encontrado = True
        if not encontrado:
            print("No se encontraron países en ese rango de superficie.")

# Actualizar los datos de un país.
def actualizar_pais(paises):

    while True:
        nombre_pais = input("Ingresar el nombre del país a actualizar: ").strip().title()

        if validacion_input(nombre_pais):
            break

    encontrado = False

    for i in paises:

        if i["nombre"] == nombre_pais:

            encontrado = True

            print("Datos actuales:")
            print(
                f"País: {i['nombre']} | "
                f"Población: {i['poblacion']} | "
                f"Superficie: {i['superficie']} | "
                f"Continente: {i['continente']}"
            )

            continente=seleccionar_continente()

            while True:
                try:
                    poblacion = int(input("Nueva población: "))

                    if poblacion < 0:
                        print("La población no puede ser negativa.")
                        continue

                    break

                except ValueError:
                    print("Solo se deben ingresar números enteros.")

            while True:
                try:
                    superficie = int(input("Nueva superficie: "))

                    if superficie < 0:
                        print("La superficie no puede ser negativa.")
                        continue

                    break

                except ValueError:
                    print("Solo se deben ingresar números enteros.")

            i["continente"] = continente
            i["poblacion"] = poblacion
            i["superficie"] = superficie

            break

    if not encontrado:
        print("No se encontró el país.")
        return

    with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:

        escritor = csv.DictWriter(
            archivo,
            fieldnames=["nombre", "poblacion", "superficie", "continente"]
        )

        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)

    print("País actualizado correctamente.")
