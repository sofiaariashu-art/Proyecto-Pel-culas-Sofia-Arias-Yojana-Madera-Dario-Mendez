import modulo_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict):

    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins" )
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)
    
    if (hora//100 < 10):
        hora_formato = "0"+ str(hora // 100)
    else:
        hora_formato = str(hora // 100)
    
    if (hora%100 < 10):
        min_formato = "0"+ str(hora % 100)
    else:
        min_formato = str(hora % 100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)

def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict):
    pelicula = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    print("La pelicula mas larga es:")
    mostrar_informacion_pelicula(pelicula)

def ejecutar_encontrar_pelicula(nombre_pelicula, p1, p2, p3, p4, p5):
    pelicula = mod.encontrar_pelicula(nombre_pelicula, p1, p2, p3, p4, p5)

    if pelicula is None:
        print("No se encontro la pelicula")
    else:
        mostrar_informacion_pelicula(pelicula)

def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict):
    promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    print("La duracion promedio es:", promedio)

def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict):
    anio = int(input("Ingrese el año: "))
    estrenos = mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio)
    print("Estrenos de películas encontradas:", estrenos)

def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict):
    cantidad = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    print("La cantidad de peliculas 18+ es:", cantidad)
    
def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict):
    nombre = input("Ingrese el nombre de la pelicula a reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)

    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        nueva_hora = int(input("Ingrese la nueva hora: "))
        nuevo_dia = input("Ingrese el nuevo dia: ").lower()
        control = input("Desea activar control horario? (si/no): ").lower()
        control_horario = False

        if control.strip().lower() == "si":
            control_horario = True

        reagenda = mod.reagendar_pelicula(
            pelicula,
            nueva_hora,
            nuevo_dia,
            control_horario,
            p1, p2, p3, p4, p5
        )

        if reagenda is True:
            print("La pelicula fue reagendada correctamente")
        else:
            print("No fue posible reagendar la pelicula")

def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict):
    nom_peli = input("Ingrese el nombre de la pelicula: ")
    pelicula = mod.encontrar_pelicula(nom_peli, p1, p2, p3, p4, p5)

    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        edad = input("Ingrese la edad del invitado: ")
        autorizacion = input("Tiene autorizacion de los padres? (si/no): ")
        autorizacion_padres = False

        if edad.isdigit():
            edad = int(edad)
        else:
            print("Solo se permiten números enteros")
            return

        if autorizacion.lower() == "si":
            autorizacion_padres = True
        puede_ingresar = mod.decidir_invitar(
            pelicula,
            edad,
            autorizacion_padres
        )

        if puede_ingresar is True:
            print("Se puede invitar a la persona")
        else:
            print("No se puede invitar a la persona")
  
def iniciar_aplicacion():

    p1 = mod.crear_pelicula("Shrek",  "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
    p2 = mod.crear_pelicula("Get Out",  "Suspenso, Terror", 104, 2017, '18+', 2330, "Sabado")  
    p3 = mod.crear_pelicula("Icarus",  "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
    p4 = mod.crear_pelicula("Inception",  "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
    p5 = mod.crear_pelicula("The Empire Strikes Back",  "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miercoles")

    ejecutando = True
    while ejecutando:
        print("\n\nMi agenda de peliculas para la semana de receso" +"\n"+("-"*50))
        print("Pelicula 1")
        mostrar_informacion_pelicula(p1)
        print("-"*50)
        
        print("Pelicula 2")
        mostrar_informacion_pelicula(p2)
        print("-"*50)
        
        print("Pelicula 3")
        mostrar_informacion_pelicula(p3)
        print("-"*50)
        
        print("Pelicula 4")
        mostrar_informacion_pelicula(p4)
        print("-"*50)
        
        print("Pelicula 5")
        mostrar_informacion_pelicula(p5)
        print("-"*50)
        
        ejecutando = mostrar_menu_aplicacion(p1, p2, p3, p4, p5)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4:dict, p5:dict) -> bool:
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien") 
    print(" 7 - Encontrar pelicula")   
    print(" 8 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)        
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "7":
        nombre_pelicula = input('Ingrese el nombre de la película: ')
        ejecutar_encontrar_pelicula(nombre_pelicula, p1, p2, p3, p4, p5)
    elif opcion_elegida == "8":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando

iniciar_aplicacion()
