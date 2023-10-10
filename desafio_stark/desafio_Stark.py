from data_stark import lista_personajes

def nombres_personajes(lista_de_personajes):
    for personaje in lista_personajes:
         print (personaje["nombre"])

def nombre_altura_personajes(lista_de_personajes):
    print ("Nombre                                   Altura")
    print("------------------------------------------------------------------------------------------------")
    for personaje in lista_personajes:
        
        print (personaje["nombre"].ljust(20), "     " ,  f"{personaje['altura']:.6}".center(30))


def superheroe_mas_alto(lista_de_personajes):
    mas_alto = None
    altura_maxima = 0

    for personaje in lista_de_personajes:
        altura = float(personaje["altura"])

        if altura > altura_maxima:
            altura_maxima = altura
            mas_alto = personaje

    if mas_alto is not None:
        print("Superhéroe más alto:", mas_alto["nombre"])
    else:
        print("No se encontró un superhéroe más alto.")




def superheroe_mas_bajo(lista_de_personajes):
    mas_bajo = None
    altura_minima = float('inf')

    for personaje in lista_de_personajes:
        altura = float(personaje["altura"])

        if altura < altura_minima:
            altura_minima = altura
            mas_bajo = personaje

    if mas_bajo is not None:
        print("Superhéroe más bajo:", mas_bajo["nombre"])
    else:
        print("No se encontró un superhéroe más bajo.")



def promedio_de_altura_superheroes(lista_de_personajes):
    altura_total= 0
    numero_de_personajes = len(lista_personajes)
    for personaje in lista_personajes:
        altura_total += float(personaje["altura"])

    if numero_de_personajes > 0:
        promedio = altura_total / numero_de_personajes
        return promedio
    else:
        return 0  # Si la lista está vacía, el promedio es 0

    


def superheroe_mas_pesado(lista_de_personajes):
    mas_pesado = None
    peso_maximo = 0

    for personaje in lista_personajes:
        peso = float(personaje["peso"])

        if peso > peso_maximo:
            peso_maximo = peso
            mas_pesado = personaje
      

    if mas_pesado is not None:
        print("Superhéroe más pesado:", mas_pesado["nombre"])
    else:
        print("No se encontró un superhéroe más alto.")



def superheroe_menos_pesado(lista_de_personajes):
    menos_pesado = None
    peso_minimo = float('inf')

    for personaje in lista_personajes:
        peso = float(personaje["peso"])

        if peso < peso_minimo:
            peso_minimo = peso
            menos_pesado = personaje
      

    if menos_pesado is not None:
        print("Superhéroe menos pesado:", menos_pesado["nombre"])
    else:
        print("No se encontró un superhéroe más alto.")
        


def obtener_dato(personaje, opcion):
    if opcion == "1":
        return personaje["altura"]
    elif opcion == "2":
        return personaje["peso"]
    elif opcion == "3":
        return personaje["genero"]
    elif opcion == "4":
        return personaje["color_ojos"]
    elif opcion == "5":
        return personaje["color_pelo"]
    elif opcion == "6":
        return personaje["fuerza"]
    elif opcion == "7":
        return personaje["inteligencia"]
    else:
        return "Dato no válido"


def obtener_dato_de_personaje():
    import os
    while True:
        os.system("cls")
        print("Menú de Opciones:")
        print("1. Obtener altura de un personaje")
        print("2. Obtener peso de un personaje")
        print("3. Obtener género de un personaje")
        print("4. Obtener color de ojos de un personaje")
        print("5. Obtener color de pelo de un personaje")
        print("6. Obtener fuerza de un personaje")
        print("7. Obtener inteligencia de un personaje")
        print("8. Salir")

        opcion = input("Seleccione una opción (1-8): ")

        if opcion == "8":
            print("¡Hasta luego!")
            break

        if opcion in ["1", "2", "3", "4", "5", "6", "7"]:
            for i, personaje in enumerate(lista_personajes):
                print(f"{i + 1}. {personaje['nombre']}")

            num_personaje = int(input("Seleccione el número del personaje: ")) - 1

            if 0 <= num_personaje < len(lista_personajes):
                personaje_elegido = lista_personajes[num_personaje]
                if opcion == "1":
                    print(f"El dato seleccionado es: {personaje_elegido['altura']}")
                elif opcion == "2":
                    print(f"El dato seleccionado es: {personaje_elegido['peso']}")
                elif opcion == "3":
                    print(f"El dato seleccionado es: {personaje_elegido['genero']}")
                elif opcion == "4":
                    print(f"El dato seleccionado es: {personaje_elegido['color_ojos']}")
                elif opcion == "5":
                    print(f"El dato seleccionado es: {personaje_elegido['color_pelo']}")
                elif opcion == "6":
                    print(f"El dato seleccionado es: {personaje_elegido['fuerza']}")
                elif opcion == "7":
                    print(f"El dato seleccionado es: {personaje_elegido['inteligencia']}")
            else:
                print("Número de personaje no válido")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1-8).")
        

obtener_dato_de_personaje()
