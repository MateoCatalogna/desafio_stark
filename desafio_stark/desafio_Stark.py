from data_stark import lista_personajes
import os


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
    if opcion == 1:
        return personaje["altura"]
    elif opcion == 2:
        return personaje["peso"]
    elif opcion == 3:
        return personaje["genero"]
    elif opcion == 4:
        return personaje["color_ojos"]
    elif opcion == 5:
        return personaje["color_pelo"]
    elif opcion == 6:
        return personaje["fuerza"]
    elif opcion == 7:
        return personaje["inteligencia"]
    else:
        return "Dato no válido"



def nombre_genero_m(lista_de_personajes):

    lista_personajes_m = []
    for personaje in lista_de_personajes:
        if personaje["genero"] == "M":
            lista_personajes_m.append(personaje)
    return lista_personajes_m
            

def nombre_genero_f(lista_de_personajes):

    lista_personajes_f = []
    for personaje in lista_de_personajes:
        if personaje["genero"] == "F":
            lista_personajes_f.append(personaje)
    return lista_personajes_f

def mas_alto_genero_m(lista_de_personajes):
    lista_personajes_m = []
    for personaje in lista_de_personajes:
        if personaje["genero"] == "M":
            lista_personajes_m.append(personaje)
    return superheroe_mas_alto(lista_personajes_m)
        
def mas_alto_genero_f(lista_de_personajes):
    lista_personajes_f = []
    for personaje in lista_de_personajes:
        if personaje["genero"] == "F":
            lista_personajes_f.append(personaje)
    return superheroe_mas_alto(lista_personajes_f)        

def mas_bajo_genero_f(lista_de_personajes):
    lista_personajes_f = []
    for personaje in lista_de_personajes:
        if personaje["genero"] == "F":
            lista_personajes_f.append(personaje)
    return superheroe_mas_bajo(lista_personajes_f)                

def mas_bajo_genero_m(lista_de_personajes):
    lista_personajes_m = []
    for personaje in lista_de_personajes:
        if personaje["genero"] == "M":
            lista_personajes_m.append(personaje)
    return superheroe_mas_bajo(lista_personajes_m)      


def promedio_de_altura_genero_m(lista_de_personajes):
    lista_personajes_m = []
    for personaje in lista_de_personajes:
        if personaje["genero"] == "M":
            lista_personajes_m.append(personaje)
    altura_total = 0        
    numero_de_personajes = len(lista_personajes_m)
    for personaje in lista_personajes_m:
        altura_total += float(personaje["altura"])
    if numero_de_personajes > 0:
        promedio = altura_total / numero_de_personajes
        return promedio
    else:
        return 0

def promedio_de_altura_genero_f(lista_de_personajes):
    lista_personajes_f = []
    for personaje in lista_de_personajes:
        if personaje["genero"] == "F":
            lista_personajes_f.append(personaje)
    altura_total = 0        
    numero_de_personajes = len(lista_personajes_f)
    for personaje in lista_personajes_f:
        altura_total += float(personaje["altura"])
    if numero_de_personajes > 0:
        promedio = altura_total / numero_de_personajes
        return promedio
    else:
        return 0


def limpiar_consola():
    

    os.system("cls")







def obtener_dato(personaje, opcion):
    if opcion == 1:
        return personaje["altura"]
    elif opcion == 2:
        return personaje["peso"]
    elif opcion == 3:
        return personaje["genero"]
    elif opcion == 4:
        return personaje["color_ojos"]
    elif opcion == 5:
        return personaje["color_pelo"]
    elif opcion == 6:
        return personaje["fuerza"]
    elif opcion == 7:
        return personaje["inteligencia"]
    else:
        return "Dato no válido"

# Define las demás funciones que necesitas aquí, similar a las que ya has creado.

def obtener_dato_de_personaje(lista_personajes):
    while True:
        print("Menú de Opciones:")
        print("1. Obtener altura de un personaje")
        print("2. Obtener peso de un personaje")
        print("3. Obtener género de un personaje")
        print("4. Obtener color de ojos de un personaje")
        print("5. Obtener color de pelo de un personaje")
        print("6. Obtener fuerza de un personaje")
        print("7. Obtener inteligencia de un personaje")
        print("8. Obtener nombre de personajes de género M")
        print("9. Obtener nombre de personajes de género F")
        print("10. Obtener nombre de personaje más alto del género M")
        print("11. Obtener nombre de personaje más alto del género F")
        print("12. Obtener nombre de personaje más bajo del género M")
        print("13. Obtener nombre de personaje más bajo del género F")
        print("14. Obtener promedio de altura del género M")
        print("15. Obtener promedio de altura del género F")
        print("16. Salir")
        

        opcion = input("Seleccione una opción (1-16): ")

        if opcion == "16":
            print("¡Hasta luego!")
            break
        


        input("Presione Enter para ver el resultado y el menú de opciones ...")  

        if opcion in ["1", "2", "3", "4", "5", "6", "7"]:
            num_personaje = int(input("Seleccione el número del personaje del 1 al 24: "))
            if 0 < num_personaje <= len(lista_personajes):
                personaje = lista_personajes[num_personaje - 1]
                print(f"El dato seleccionado es: {obtener_dato(personaje, int(opcion))}")
            else:
                print("Número no válido")

        elif opcion == "8":
            for personaje in nombre_genero_m(lista_personajes):
                print(personaje["nombre"])        
        elif opcion == "9":
            for personaje in nombre_genero_f(lista_personajes):
                print(personaje["nombre"])
        elif opcion == "10":
            superheroe_mas_alto(nombre_genero_m(lista_personajes))
        elif opcion == "11":
            superheroe_mas_alto(nombre_genero_f(lista_personajes))
        elif opcion == "12":
            superheroe_mas_bajo(nombre_genero_m(lista_personajes))
        elif opcion == "13":
            superheroe_mas_bajo(nombre_genero_f(lista_personajes))
        if opcion == "14":
            promedio_m = promedio_de_altura_genero_m(lista_personajes)
            print(f"Promedio de altura para personajes de género masculino (M): {promedio_m:.2f} cm")
        elif opcion == "15":
            promedio_f = promedio_de_altura_genero_f(lista_personajes)
            print(f"Promedio de altura para personajes de género femenino (F): {promedio_f:.2f} cm")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1-16).")

obtener_dato_de_personaje(lista_personajes)