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




def tipo_color_ojos(lista_de_personajes):
    blue_eyes = 0
    red_eyes = 0
    brown_eyes = 0
    yellow_eyes = 0
    green_eyes = 0
    silver_eyes = 0
    hazel_eyes = 0
    for personaje in lista_de_personajes:
        color_ojos = personaje["color_ojos"]
        match color_ojos:
            case "Blue" | "blue":
                blue_eyes += 1
            case  "Red" | "red":
                red_eyes += 1
            case "Brown" | "brown":
                brown_eyes += 1
            case "Yellow" | "yellow":
                yellow_eyes += 1
            case "Green" | "green ":
                green_eyes += 1
            case "Silver" | "silver":
                silver_eyes += 1
            case "Hazel" | "hazel":
                hazel_eyes += 1
            case other:
                print("Color de ojos no registrado")
    print(f"hay {blue_eyes} suoerheroes de ojos azules, {red_eyes} superheroes de ojos rojos, {brown_eyes} superheroes de ojos marrones, {yellow_eyes} superheroes de ojos amarillos, {green_eyes} superheroes de ojos verdes, {silver_eyes} superheroes de ojos color silver, {hazel_eyes} superheroes de ojos color hazel")



def color_de_pelo_superheroes(lista_de_personajes):
    green_hair = 0
    red_hair = 0
    black_hair = 0
    yellow_hair = 0
    no_hair = 0
    blond_hair = 0
    brown_hair = 0
    white_hair = 0
    for personaje in lista_de_personajes:
        color_de_pelo = personaje["color_pelo"]
        match color_de_pelo:
            case "Green" | "green":
                green_hair += 1
            case "Red" | "red":
                red_hair += 1
            case "Black" | "black":
                black_hair += 1
            case "Yellow" | "yellow":
                yellow_hair += 1
            case "Blond" | "blond":
                blond_hair += 1
            case "Brown" | "brown":
                brown_hair += 1
            case "White" | "white":
                white_hair += 1
            case other:
                no_hair += 1
    print(f"hay {no_hair} superheroes sin pelo, {green_hair} superheores con el pelo verde, {red_hair} superheroes con pelo rojo,{black_hair} superheroes con pelo negro, {yellow_hair} superheroes con pelo amarillo, {blond_hair} superheroes rubios, {brown_hair} superheroes con el pelo marron y {white_hair} superheroes con el pelo blanco")
    


def tipo_inteligencia_superheroes(lista_de_personajes):
    average_inteligence = 0
    good_inteligence = 0
    high_inteligence = 0
    no_intelligence = 0
    for personaje in lista_de_personajes:
        inteligencia = personaje["inteligencia"]
        match inteligencia:
            case "good":
                good_inteligence += 1
            case "high":
                high_inteligence += 1
            case "average":
                average_inteligence += 1
            case other:
                no_intelligence += 1

    print(f"hay {no_intelligence} superheroes sin inteligencia, {good_inteligence} superheroes con inteligencia tipo 'good', {high_inteligence} superheroes con inteligencvia tipo 'high, {average_inteligence} superheroes con inteligencia tipo 'average'")

    
    
def lista_segun_color_ojos(lista_de_personajes):
    blue_eyes = []
    red_eyes = []
    brown_eyes = []
    yellow_eyes = []
    green_eyes = []
    silver_eyes = []
    hazel_eyes = []
    for personaje in lista_de_personajes:
        color_ojos = personaje["color_ojos"]
        match color_ojos:
            case "Blue" | "blue":
                blue_eyes.append(personaje["nombre"])
            case  "Red" | "red":
                red_eyes.append(personaje["nombre"])
            case "Brown" | "brown":
                brown_eyes.append(personaje["nombre"])
            case "Yellow" | "yellow":
                yellow_eyes.append(personaje["nombre"])
            case "Green" | "green":
                green_eyes.append(personaje["nombre"])
            case "Silver" | "silver":
                silver_eyes.append(personaje["nombre"])
            case "Hazel" | "hazel":
                hazel_eyes.append(personaje["nombre"])
            case other:
                print("Color de ojos no registrado")

    print("Los superhéroes con ojos azules son:", ", ".join(blue_eyes))
    print("Los superhéroes con ojos rojos son:", ", ".join(red_eyes))
    print("Los superhéroes con ojos marrones son:", ", ".join(brown_eyes))
    print("Los superhéroes con ojos amarillos son:", ", ".join(yellow_eyes))
    print("Los superhéroes con ojos verdes son:", ", ".join(green_eyes))
    print("Los superhéroes con ojos plateados son:", ", ".join(silver_eyes))
    print("Los superhéroes con ojos avellana son:", ", ".join(hazel_eyes))
    

def lista_segun_color_pelo(lista_de_personajes):
    green_hair = []
    red_hair = []
    black_hair = []
    yellow_hair = []
    no_hair = []
    blond_hair = []
    brown_hair = []
    white_hair = []
    for personaje in lista_de_personajes:
        color_de_pelo = personaje["color_pelo"]
        match color_de_pelo:
            case "Green" | "green":
                green_hair.append(personaje["nombre"])
            case "Red" | "red":
                red_hair.append(personaje["nombre"])
            case "Black" | "black":
                black_hair.append(personaje["nombre"])
            case "Yellow" | "yellow":
                yellow_hair.append(personaje["nombre"])
            case "Blond" | "blond":
                blond_hair.append(personaje["nombre"])
            case "Brown" | "brown":
                brown_hair.append(personaje["nombre"])
            case "White" | "white":
                white_hair.append(personaje["nombre"])
            case other:
                no_hair.append(personaje["nombre"])

    print("Los superhéroes con pelo verde son:", ", ".join(green_hair))
    print("Los superhéroes con pelo rojo son:", ", ".join(red_hair))
    print("Los superhéroes con pelo marron son:", ", ".join(brown_hair))
    print("Los superhéroes con pelo amarillo son:", ", ".join(yellow_hair))
    print("Los superhéroes rubios son:", ", ".join(blond_hair))
    print("Los superhéroes con pelo blanc son:", ", ".join(white_hair))
    print("Los superhéroes sin pelo son:", ", ".join(no_hair))


def listar_segun_inteligencia(lista_de_personajes):
    average_inteligence = []
    good_inteligence = []
    high_inteligence = []
    no_intelligence = []
    for personaje in lista_de_personajes:
        inteligencia = personaje["inteligencia"]
        match inteligencia:
            case "good":
                good_inteligence.append(personaje["nombre"])
            case "high":
                high_inteligence.append(personaje["nombre"])
            case "average":
                average_inteligence.append(personaje["nombre"])
            case other:
                no_intelligence.append(personaje["nombre"])
    
    print("Los superhéroes con inteligencia tipo 'good' son:", ", ".join(good_inteligence))
    print("Los superhéroes con inteligencia tipo 'high' son:", ", ".join(high_inteligence))
    print("Los superhéroes con inteligencia tipo 'average' son:", ", ".join(average_inteligence))
    print("Los superhéroes sin inteligencia son:", ", ".join(no_intelligence))

listar_segun_inteligencia(lista_personajes)