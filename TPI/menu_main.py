from funciones_principales import *

# Muestra el menú imprime pantalla. 
def menu_opciones():
    print("Menú:\n"
        "1. Mostrar país.\n"
        "2. Agregar país.\n"
        "3. Mostrar estadísticas.\n"
        "4. Ordenar países.\n"
        "5. Filtrar países.\n"
        "6. Actualizar los datos de un país.\n"
        "7. Salir.\n")

# Función principal.
def main():

    paises=cargar_paises()

    while True:

        menu_opciones()

        while True:
            try:
                opcion=int(input("Ingresar una de las opciones: ")) 
                if 1<=opcion<=7: 
                    break
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Ingresar solo el número de una de las opciones.")
        
        if opcion==1:
            if hay_paises(paises):
                mostrar_pais(paises)
                print()

        elif opcion==2:
            agregar_pais(paises)
            print()

        elif opcion==3:
            if hay_paises(paises):
                mostrar_estadisticas(paises)
                print()

        elif opcion==4:
            if hay_paises(paises):
                ordenar_paises(paises)
                print()

        elif opcion==5:
            if hay_paises(paises):
                filtrar_paises(paises)
                print()

        elif opcion==6:
            if hay_paises(paises):
                actualizar_pais(paises)
                print()

        elif opcion==7: # Para salir del menú.
            print("Saliendo del menú.")
            break

main()