def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, clasificacion: str, hora: int, dia: str) -> dict:
    pelicula = {
        "nombre": nombre,
        "genero": genero,
        "duracion": duracion,
        "anio": anio,
        "clasificacion": clasificacion,
        "hora": hora,
        "dia": dia

    }

    return pelicula

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    bd = [p1, p2, p3, p4, p5]
    for i in bd:
        if i["nombre"] == nombre_pelicula:
            return i

    return None

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    mas_larga = p1

    if p2["duracion"] > mas_larga["duracion"]:
        mas_larga = p2

    if p3["duracion"] > mas_larga["duracion"]:
        mas_larga = p3

    if p4["duracion"] > mas_larga["duracion"]:
        mas_larga = p4

    if p5["duracion"] > mas_larga["duracion"]:
        mas_larga = p5

    return mas_larga

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    total = (
        p1["duracion"] +
        p2["duracion"] +
        p3["duracion"] +
        p4["duracion"] +
        p5["duracion"]
    )

    promedio = total // 5
    horas = promedio // 60
    minutos = promedio % 60

    if horas < 10:
        horas_formato = "0" + str(horas)
    else:
        horas_formato = str(horas)

    if minutos < 10:
        minutos_formato = "0" + str(minutos)
    else:
        minutos_formato = str(minutos)

    return horas_formato + ":" + minutos_formato

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    peliculas = [p1, p2, p3, p4, p5]
    encontrados = []

    for peli in peliculas:

        if peli["anio"] > anio:
            encontrados.append(peli["nombre"])

    if len(encontrados) == 0:
        return "Ninguna"

    return ", ".join(encontrados)

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    contador = 0
    peliculas = [p1, p2, p3, p4, p5]

    for peli in peliculas:
        if peli["clasificacion"] == "18+":
            contador += 1

    return contador

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool:
    peliculas = [p1, p2, p3, p4, p5]

    for pelicula in peliculas:
        dia_pelicula = pelicula["dia"].lower()
        if dia_pelicula == nuevo_dia and pelicula["hora"] == nueva_hora:
            return False

    if control_horario:
        genero = peli["genero"]

        if "Documental" in genero.lower() and nueva_hora >= 2200:
            return False
        elif "drama" in genero.lower() and nuevo_dia == "viernes":
            return False

        dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes"]

        if nuevo_dia in dias_semana:
            if nueva_hora >= 2300 or nueva_hora < 600:
                return False

    peli["hora"] = nueva_hora
    peli["dia"] = nuevo_dia

    return True
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:

    genero = peli["genero"]
    clasificacion = peli["clasificacion"]

    if edad_invitado <= 0:
        print("La edad debe ser positiva")
        return False

    if edad_invitado >= 100:
        print("La persona debe estar viva")
        return False

    if edad_invitado < 15 and "terror" in genero.lower():
        print("Los menores de 15 años no pueden ver películas de Terror")
        return False

    if edad_invitado <= 10 and "familiar" not in genero.lower():
        print("Los niños de 10 años o menos solo pueden ver películas Familiares")
        return False

    if "documental" in genero.lower():
        return True

    if clasificacion == "18+" and edad_invitado < 18:
        if autorizacion_padres:
            return True
        else:
            print("Se requiere autorización de los padres")
            return False

    if clasificacion == "16+" and edad_invitado < 16:
        if autorizacion_padres:
            return True
        else:
            print("Se requiere autorización de los padres")
            return False

    if clasificacion == "13+" and edad_invitado < 13:
        if autorizacion_padres:
            return True
        else:
            print("Se requiere autorización de los padres")
            return False

    if clasificacion == "7+" and edad_invitado < 7:
        if autorizacion_padres:
            return True
        else:
            print("Se requiere autorización de los padres")
            return False

    print("Invitado aceptado")
    return True