from robot import ErrorDeSeguridad, Robot
from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO


VELOCIDAD_MAX = 0.20
VELOCIDAD_GIRO_MAX = 0.50
TIEMPO_MAX = 10.0
PI = 3.14159265

DATOS_POR_COMANDO = {
    "avanzar": 2,
    "girar": 2,
    "detenerse": 0,
    "saludar": 0,
}


def es_numero(valor):
    return type(valor) == int or type(valor) == float


def motivo_de_rechazo(comando):
    if type(comando) != tuple or len(comando) == 0:
        return "el comando tiene que ser una tupla no vacia"

    nombre = comando[0]
    datos = comando[1:]

    if nombre not in DATOS_POR_COMANDO:
        return "ese comando no existe"

    esperados = DATOS_POR_COMANDO[nombre]
    if len(datos) != esperados:
        return "cantidad de datos incorrecta"

    if esperados == 0:
        return ""

    velocidad, tiempo = datos

    if not es_numero(velocidad):
        return "la velocidad tiene que ser un numero"
    if not es_numero(tiempo):
        return "el tiempo tiene que ser un numero"

    if not (tiempo > 0):
        return "el tiempo tiene que ser mayor a 0"
    if not (tiempo <= TIEMPO_MAX):
        return "el tiempo supera el maximo permitido"

    if nombre == "avanzar":
        if not (velocidad > 0 and velocidad <= VELOCIDAD_MAX):
            return "la velocidad esta fuera del rango permitido"

    if nombre == "girar":
        if not (velocidad != 0 and velocidad >= -VELOCIDAD_GIRO_MAX
                and velocidad <= VELOCIDAD_GIRO_MAX):
            return "la velocidad de giro esta fuera del rango permitido"

    return ""


def comando_es_valido(comando):
    return motivo_de_rechazo(comando) == ""


def ejecutar_comando(robot, comando):
    nombre = comando[0]

    try:
        if nombre == "avanzar":
            velocidad = comando[1]
            tiempo = comando[2]
            robot.avanzar(velocidad=velocidad, tiempo=tiempo)
            return True, "avanzo"

        if nombre == "girar":
            velocidad = comando[1]
            tiempo = comando[2]
            robot.girar(velocidad=velocidad, tiempo=tiempo)
            if velocidad > 0:
                return True, "giro a la izquierda"
            else:
                return True, "giro a la derecha"

        if nombre == "detenerse":
            robot.detenerse()
            return True, "se detuvo"

        if nombre == "saludar":
            robot.saludar()
            return True, "saludo"

        return False, "no se como ejecutar ese comando"

    except ErrorDeSeguridad as error:
        robot.detenerse()
        return False, "el robot lo rechazo"
    except NotImplementedError:
        return False, "el robot no puede hacerlo"


def ejecutar_mision(robot, mision, historial):
    total = len(mision)
    print()
    print("=== Iniciando mision:", total, "comando(s) ===")

    for i in range(total):
        numero = i + 1
        comando = mision[i]

        if not comando_es_valido(comando):
            motivo = motivo_de_rechazo(comando)
            historial.append({"numero": numero, "comando": comando,
                              "ejecutado": False, "detalle": motivo})
            print("  [", numero, "/", total, "] RECHAZADO", comando, ":", motivo)
            continue

        ejecutado, texto = ejecutar_comando(robot, comando)
        historial.append({"numero": numero, "comando": comando,
                          "ejecutado": ejecutado, "detalle": texto})
        if ejecutado:
            estado = "OK       "
        else:
            estado = "RECHAZADO"
        print("  [", numero, "/", total, "]", estado, comando, ":", texto)

    print("=== Mision finalizada ===")


def generar_reporte(historial):
    ejecutados = 0
    rechazados = []
    distancia = 0.0
    radianes = 0.0
    duracion = 0.0

    for registro in historial:
        if not registro["ejecutado"]:
            rechazados.append(registro)
            continue

        ejecutados += 1
        comando = registro["comando"]
        if comando[0] == "avanzar":
            distancia += comando[1] * comando[2]
            duracion += comando[2]
        elif comando[0] == "girar":
            giro = comando[1] * comando[2]
            if giro < 0:
                giro = giro * -1
            radianes += giro
            duracion += comando[2]

    grados = radianes * 180 / PI

    print()
    print("============================================================")
    print("                     REPORTE DE MISION")
    print("============================================================")
    print("  Comandos recibidos:  ", len(historial))
    print("  Comandos ejecutados: ", ejecutados)
    print("  Comandos rechazados: ", len(rechazados))
    print("  Distancia recorrida: ", round(distancia, 2), "m")
    print("  Total girado:        ", round(grados), "grados")
    print("  Duracion estimada:   ", round(duracion, 2), "s")

    if len(rechazados) > 0:
        print("------------------------------------------------------------")
        print("  Motivo de cada rechazo:")
        for registro in rechazados:
            print("    #", registro["numero"], registro["comando"])
            print("       ->", registro["detalle"])
    print("============================================================")


MISION_PROPIA = [
    ("avanzar", 0.2, 2.5),
    ("girar", 0.5, 4.19),
    ("avanzar", 0.2, 2.5),
    ("girar", 0.5, 12.6),
    ("girar", 0.5, 4.19),
    ("avanzar", 0.25, 2.0),
    ("avanzar", 0.2, 2.5),
    ("girar", 0.5, 4.19),
    ("Saludar",),
    ("saludar",),
    ("detenerse",),
]

MISIONES_A_EJECUTAR = [
    ("MISION_BASICA", MISION_BASICA),
    ("MISION_CON_ERRORES", MISION_CON_ERRORES),
    ("MISION_CUADRADO", MISION_CUADRADO),
    ("MISION_PROPIA", MISION_PROPIA),
]


def main():
    robot = Robot()
    robot.conectar()
    try:
        for nombre, mision in MISIONES_A_EJECUTAR:
            print()
            print("################", nombre, "################")
            historial = []
            ejecutar_mision(robot, mision, historial)
            generar_reporte(historial)
    finally:
        robot.detenerse()
        robot.desconectar()


main()
