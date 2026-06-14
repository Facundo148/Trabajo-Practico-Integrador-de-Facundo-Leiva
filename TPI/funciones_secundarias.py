import csv

# Función para validar entradas de strings.
def validacion_input(nombre):
  
    if nombre=="":
        print("No se permiten campos vacíos.")
        return False
  
    elif not nombre.replace(" ", "").isalpha():
        print("Solo ingresar letras.")
        return False
  
    return True

# Verifíca si hay países cargados.
def hay_paises(paises):
    if not paises:
        print("Primero se deben agregar los países con la opción 2!\n")
        return False
    return True

#Carga el archivo.CSV y una lista.
def cargar_paises():
  
    paises = []
  
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
  
        for i in lector:
            i["poblacion"]=int(i["poblacion"])
            i["superficie"]=int(i["superficie"])
            paises.append(i)
  
    return paises

def seleccionar_continente(): 
   
    while True: 
        print("Seleccionar continente:") 
        print("1. América") 
        print("2. Europa") 
        print("3. Asia") 
        print("4. África") 
        print("5. Oceanía") 
        print("6. Antártida") 
     
        try: 
            opcion = int(input("Opción: ")) 
        
            if opcion == 1: 
                return "America" 
            elif opcion == 2: 
                return "Europa" 
            elif opcion == 3: 
                return "Asia" 
            elif opcion == 4: 
                return "Africa" 
            elif opcion == 5: 
                return "Oceania" 
            elif opcion == 6: 
                return "Antartida" 
            else: 
                print("Debe ingresar una opción válida.") 
        
        except ValueError: 
            print("Solo se deben ingresar números.")
