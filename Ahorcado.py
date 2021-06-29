#paises: Camboya, Finlandia, Marruecos, Noruega, Ucrania
#frutas: Aguacate, Melocotón, Pomelo, Mango, Pistacho
#géneros musicales: Clásica, Gospel, Country, Flamenco, Punk.
#animales: Girafa, Delfín, Gorila, Jaguar, Mariposa
#películas: Los vengadores, Crepúsculo, La naranja mecánica, El conjuro, Psicosis.

from random import randint

palabras = [["CAMBOYA", "AGUACATE", "CLASICA", "GIRAFA", "LOS VENGADORES"],
            ["FINLANDIA", "MELOCOTON", "GOSPEL", "DELFIN", "CREPUSCULO"],
            ["MARRUECOS", "POMELO", "COUNTRY", "GORILA", "LA NARANJA MECANICA"],
            ["NORUEGA", "MANGO", "FLAMENCO", "JAGUAR", "EL CONJURO"],
            ["UCRANIA", "PISTACHO", "PUNK", "MARIPOSA", "PSICOSIS"]]

def seleccionar_categoría(): #devuelve un número del 1 al 5
    print("\nCATEGORÍAS\n")
    print("1. Paises\n2. Frutas\n3. Géneros musicales\n4. Animales\n5. Películas")
    opcion = str(input("Elige una opción (número): "))
    while opcion.isnumeric()==False or not(1<=int(opcion)<=5):
        print("opcion no válida")
        opcion = str(input("Elige una opción entre 1 y 5: "))
        
    opcion = int(opcion)
    return opcion

def seleccionar_palabra(matriz):
    columna = seleccionar_categoría() - 1
    fila = randint(0,4)
    palabra = palabras[fila][columna]
    return palabra

def mostrar_cantidad_de_letras(palabra):#recibe una lista o una cadena
    lista = []
    for i in range(len(palabra)):
        if palabra[i]==" ":
            lista.append(" ")
            print(" ", end=" ")
        else:
            lista.append("_")
            print("_", end=" ")
    print(" ")
    
    return lista

def mostrar_hombre(n):
    if n==10:
        print("              ")
        print("              ")
        print("              ")
        print("              ")
        print("              ")
        print("              ")
        print("  __ __       ")
    
    if n==9:
        print("              ")
        print("    |         ")
        print("    |         ")
        print("    |         ")
        print("    |         ")
        print("    |         ")
        print("  __|__       ")

    if n==8:    
        print("     ______   ")
        print("    |         ")
        print("    |         ")
        print("    |         ")
        print("    |         ")
        print("    |         ")
        print("  __|__       ")
        
    if n==7:
        print("     ______   ")
        print("    |      |  ")
        print("    |         ")
        print("    |         ")
        print("    |         ")
        print("    |         ")
        print("  __|__       ")
        
    if n==6:
        print("     ______   ")
        print("    |      |  ")
        print("    |     ( ) ")
        print("    |         ")
        print("    |         ")
        print("    |         ")
        print("  __|__       ")
        
    if n==5:
        print("     ______   ")
        print("    |      |  ")
        print("    |     ( ) ")
        print("    |      |  ")
        print("    |      |  ")
        print("    |         ")
        print("  __|__       ")
        
    if n==4:
        print("     ______   ")
        print("    |      |  ")
        print("    |     ( ) ")
        print("    |     /|  ")
        print("    |      |  ")
        print("    |         ")
        print("  __|__       ")
        
    if n==3:
        print("     ______   ")
        print("    |      |  ")
        print("    |     ( ) ")
        print("    |     /|\ ")
        print("    |      |  ")
        print("    |         ")
        print("  __|__       ")
        
    if n==2:
        print("     ______   ")
        print("    |      |  ")
        print("    |     ( ) ")
        print("    |     /|\ ")
        print("    |      |  ")
        print("    |     /   ")
        print("  __|__       ")
    
    if n==1:
        print("     ______   ")
        print("    |      |  ")
        print("    |     ( ) ")
        print("    |     /|\ ")
        print("    |      |  ")
        print("    |     / \ ")
        print("  __|__       ")
    
    if n==0:
        print("     ______   ")
        print("    |      |  ")
        print("    |    _(_)_")
        print("    |     /|\ ")
        print("    |      |  ")
        print("    |     / \ ")
        print("  __|__       ")

def adivinar_palabra(palabra):
    lista_guiones = mostrar_cantidad_de_letras(palabra)
    
    oportunidades = 11
    letras_usadas = []
    
    while oportunidades>0:
        letra = str(input("\n--> "))
        letra = letra.upper()
        if letra not in letras_usadas:
            letras_usadas.append(letra)
        
            if letra in palabra:
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        lista_guiones[i] = letra
                    print(lista_guiones[i],end=" ")
                print(" ")
                if lista_guiones == list(palabra): 
                    break
                else:
                    mostrar_hombre(oportunidades)
            else:
                for i in lista_guiones:
                    print(i,end=" ")
                oportunidades -= 1
                print(" ")
                mostrar_hombre(oportunidades)
                #print(f"  le quedan {oportunidades} oportuninades")
        
        else:
            print("ya usó esa letra\n")
            mostrar_hombre(oportunidades)
    
    return lista_guiones

def menu_final():
    opcion = str(input("Presione 1 si desea elegir otra categoría. Presione 0 si desea cerrar el juego "))
    while opcion.isnumeric()==False or not(0<=int(opcion)<=1):
        print("opción no válida")
        opcion = str(input("Presione 1 si desea elegir otra categoría. Presione 0 si desea cerrar el juego "))
    
    return opcion



while True:
    palabra = seleccionar_palabra(palabras)
    lista_guiones = adivinar_palabra(palabra)
    if list(palabra) == lista_guiones:
        print("\n¡¡¡Felicitaciones!!!\n")
        nueva_opcion = menu_final()
        
        if int(nueva_opcion) == 0:
            print("Hasta pronto!")
            break
    else:
        print("\nPartida perdida\n")
        nueva_opcion = menu_final()
        
        if int(nueva_opcion) == 0:
            print("\n¡Hasta pronto!")
            break