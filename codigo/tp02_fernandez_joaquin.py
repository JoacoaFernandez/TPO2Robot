# =====================================================================
#  TP02 - Programacion I
#  Controlador de misiones
#
#  ESTE ES EL ARCHIVO DONDE ESCRIBIS TU PROGRAMA.
#
#  Antes de ejecutarlo:
#    1. Abri INICIAR_SIMULADOR (elegi G1 o Go2)
#    2. Espera a que aparezca la ventana con el robot
#    3. Recien ahi ejecuta este archivo
#
#  Nombre y apellido:  Joaquin Fernandez
#  Comision:           Programacion I - turno noche, jueves
# =====================================================================

import math
import sys
from pathlib import Path

try:
    from robot import ErrorDeSeguridad, Robot
    from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO
except ModuleNotFoundError:
    # Este archivo vive en TPO2Robot/codigo/. Si no esta al lado de robot.py
    # (dentro de mi_desarrollo/), lo buscamos en la carpeta de la catedra.
    # Dentro de mi_desarrollo/ este bloque no se usa.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "UadeRobotLab"
                           / "05LaboratoriosTPs" / "TP02_Programacion_I"
                           / "mi_desarrollo"))
    from robot import ErrorDeSeguridad, Robot
    from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO


# =====================================================================
#  CONSTANTES (limites de la materia, perfil "tp02" de safety.py)
# =====================================================================
VELOCIDAD_MAX = 0.20          # m/s, para avanzar
VELOCIDAD_GIRO_MAX = 0.50     # rad/s, para girar
TIEMPO_MAX = 10.0             # segundos por comando

# Cuantos datos lleva cada comando ademas del nombre
DATOS_POR_COMANDO = {
    "avanzar": 2,      # velocidad, tiempo
    "girar": 2,        # velocidad, tiempo
    "detenerse": 0,
    "saludar": 0,
}


# =====================================================================
#  PARTE 1 - Validar un comando
# =====================================================================
def es_numero(valor):
    """True si 'valor' es un int o float finito. Los bool no cuentan
    (en Python True es un int) y los textos tampoco, aunque digan "0.2"."""
    return (isinstance(valor, (int, float))
            and not isinstance(valor, bool)
            and math.isfinite(valor))


def motivo_de_rechazo(comando):
    """Revisa un comando. Devuelve un texto con el problema, o None si esta bien."""
    if not isinstance(comando, tuple) or len(comando) == 0:
        return "el comando tiene que ser una tupla no vacia"

    nombre = comando[0]
    datos = comando[1:]

    if nombre not in DATOS_POR_COMANDO:
        return f"'{nombre}' no es un comando valido"

    esperados = DATOS_POR_COMANDO[nombre]
    if len(datos) != esperados:
        return f"'{nombre}' lleva {esperados} dato(s) y recibio {len(datos)}"

    # detenerse y saludar no llevan datos: si llegamos aca, estan bien
    if esperados == 0:
        return None

    velocidad, tiempo = datos

    if not es_numero(velocidad):
        return f"la velocidad tiene que ser un numero, no {velocidad!r}"
    if not es_numero(tiempo):
        return f"el tiempo tiene que ser un numero, no {tiempo!r}"

    if tiempo <= 0:
        return f"el tiempo tiene que ser mayor a 0 (recibio {tiempo} s)"
    if tiempo > TIEMPO_MAX:
        return f"{tiempo} s supera el maximo de {TIEMPO_MAX} s por comando"

    if nombre == "avanzar" and not (0 < velocidad <= VELOCIDAD_MAX):
        return f"{velocidad} m/s esta fuera del rango (0, {VELOCIDAD_MAX}] m/s"
    if nombre == "girar" and not (0 < abs(velocidad) <= VELOCIDAD_GIRO_MAX):
        return f"{velocidad} rad/s esta fuera del rango permitido (+-{VELOCIDAD_GIRO_MAX} rad/s, distinto de 0)"

    return None


def comando_es_valido(comando):
    """Decide si un comando se puede ejecutar. Devuelve True o False.

    Un comando es una tupla. El primer elemento dice que hacer:

        ("avanzar", velocidad, tiempo)    velocidad en m/s, tiempo en s
        ("girar", velocidad, tiempo)      velocidad en rad/s, tiempo en s
        ("detenerse",)
        ("saludar",)

    Cosas que conviene revisar:
      - que la tupla no este vacia
      - que el nombre del comando sea uno de los cuatro validos
      - que tenga la cantidad de datos que corresponde
        (avanzar y girar llevan dos; detenerse y saludar, ninguno)
      - que velocidad y tiempo sean numeros de verdad, no textos
      - que el tiempo no sea negativo
    """
    return motivo_de_rechazo(comando) is None


# =====================================================================
#  PARTE 2 - Ejecutar un comando
# =====================================================================
def ejecutar_comando(robot, comando):
    """Ejecuta UN comando en el robot. Devuelve un texto con lo que paso.

    Ordenes que podes usar:

        robot.avanzar(velocidad=..., tiempo=...)
        robot.girar(velocidad=..., tiempo=...)
        robot.detenerse()
        robot.saludar()

    Ojo: aunque el comando parezca valido, el robot puede rechazarlo
    igual (por ejemplo, si la velocidad supera el limite de la materia).
    Eso llega como un ErrorDeSeguridad y conviene atraparlo.

    Devuelve una tupla (ejecutado, texto):
      ejecutado  True si el robot lo hizo, False si lo rechazo
      texto      que paso, para mostrar y guardar en el historial
    """
    nombre = comando[0]

    try:
        if nombre == "avanzar":
            velocidad, tiempo = comando[1], comando[2]
            robot.avanzar(velocidad=velocidad, tiempo=tiempo)
            distancia = velocidad * tiempo
            return True, f"avanzo {distancia:.2f} m ({velocidad} m/s x {tiempo} s)"

        if nombre == "girar":
            velocidad, tiempo = comando[1], comando[2]
            robot.girar(velocidad=velocidad, tiempo=tiempo)
            grados = math.degrees(abs(velocidad * tiempo))
            sentido = "izquierda" if velocidad > 0 else "derecha"
            return True, f"giro {grados:.0f} grados a la {sentido}"

        if nombre == "detenerse":
            robot.detenerse()
            return True, "se detuvo"

        if nombre == "saludar":
            robot.saludar()
            return True, "saludo"

        return False, f"no se como ejecutar '{nombre}'"

    except ErrorDeSeguridad as error:
        # El robot lo rechazo aunque paso nuestra validacion.
        # safety.py pide dejar el robot detenido despues de un rechazo.
        robot.detenerse()
        return False, f"el robot lo rechazo: {error}"
    except NotImplementedError as error:
        # Por ejemplo: un robot que no tiene gesto de saludo.
        return False, f"el robot no puede hacerlo: {error}"


# =====================================================================
#  PARTE 3 - Recorrer la mision entera
# =====================================================================
def ejecutar_mision(robot, mision, historial):
    """Recorre la lista de comandos, uno por uno.

    Por cada comando:
      - si NO es valido, lo rechaza y sigue con el siguiente
      - si es valido, lo ejecuta
      - en los dos casos, guarda en 'historial' que fue lo que paso

    Un comando invalido NO tiene que cortar la mision.

    'historial' es una lista: se modifica aca adentro y no hace falta
    devolverla (las listas se pasan por referencia). Cada elemento es
    un diccionario:
        {"numero": 1, "comando": (...), "ejecutado": True/False, "detalle": "..."}
    """
    total = len(mision)
    print(f"\n=== Iniciando mision: {total} comando(s) ===")

    for numero, comando in enumerate(mision, start=1):
        if not comando_es_valido(comando):
            motivo = motivo_de_rechazo(comando)
            historial.append({"numero": numero, "comando": comando,
                              "ejecutado": False, "detalle": motivo})
            print(f"  [{numero}/{total}] RECHAZADO  {comando!r}: {motivo}")
            continue    # salteamos este comando y seguimos con el siguiente

        ejecutado, texto = ejecutar_comando(robot, comando)
        historial.append({"numero": numero, "comando": comando,
                          "ejecutado": ejecutado, "detalle": texto})
        estado = "OK       " if ejecutado else "RECHAZADO"
        print(f"  [{numero}/{total}] {estado}  {comando!r}: {texto}")

    print("=== Mision finalizada ===")


# =====================================================================
#  PARTE 4 - El reporte final
# =====================================================================
def generar_reporte(historial):
    """Muestra por pantalla un resumen de la mision.

    Tiene que decir, como minimo:
      - cuantos comandos se ejecutaron bien
      - cuantos se rechazaron
      - cual fue el motivo de cada rechazo

    Ademas calcula, con los comandos que SI se ejecutaron:
      - distancia recorrida  (suma de velocidad x tiempo de cada avanzar)
      - total girado         (suma de |velocidad x tiempo| de cada girar)
      - duracion estimada    (suma de los tiempos de avanzar y girar)
    """
    ejecutados = 0
    rechazados = []          # los registros que no se ejecutaron
    distancia = 0.0          # metros
    radianes = 0.0           # siempre positivo: cuanto giro, sin importar el sentido
    duracion = 0.0           # segundos

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
            radianes += abs(comando[1] * comando[2])
            duracion += comando[2]

    print()
    print("=" * 60)
    print("REPORTE DE MISION".center(60))
    print("=" * 60)
    print(f"  Comandos recibidos:   {len(historial)}")
    print(f"  Comandos ejecutados:  {ejecutados}")
    print(f"  Comandos rechazados:  {len(rechazados)}")
    print(f"  Distancia recorrida:  {round(distancia, 2)} m")
    print(f"  Total girado:         {round(math.degrees(radianes))} grados")
    print(f"  Duracion estimada:    {round(duracion, 2)} s")

    if rechazados:
        print("-" * 60)
        print("  Motivo de cada rechazo:")
        for registro in rechazados:
            print(f"    #{registro['numero']} {registro['comando']!r}")
            print(f"       -> {registro['detalle']}")
    print("=" * 60)


# =====================================================================
#  MISION PROPIA: un triangulo equilatero de 0.5 m de lado, con saludo
#  al final. 120 grados = 2.094 rad -> a 0.5 rad/s son 4.19 s.
#  Tiene 3 comandos INVALIDOS a proposito (marcados con MAL).
# =====================================================================
MISION_PROPIA = [
    ("avanzar", 0.2, 2.5),      # lado 1: 0.2 x 2.5 = 0.5 m
    ("girar", 0.5, 4.19),       # 120 grados a la izquierda
    ("avanzar", 0.2, 2.5),      # lado 2
    ("girar", 0.5, 12.6),       # MAL: una vuelta entera de una vez (12.6 s > 10 s)
    ("girar", 0.5, 4.19),       # 120 grados a la izquierda
    ("avanzar", 0.25, 2.0),     # MAL: 0.25 m/s pasa el limite de la materia (0.20)
    ("avanzar", 0.2, 2.5),      # lado 3: vuelve al punto de partida
    ("girar", 0.5, 4.19),       # 120 grados: queda mirando como al principio
    ("Saludar",),               # MAL: con mayuscula no es un comando valido
    ("saludar",),
    ("detenerse",),
]

# Misiones que ejecuta el programa, en orden: (nombre, lista de comandos)
MISIONES_A_EJECUTAR = [
    ("MISION_BASICA", MISION_BASICA),
    ("MISION_CON_ERRORES", MISION_CON_ERRORES),
    ("MISION_CUADRADO", MISION_CUADRADO),
    ("MISION_PROPIA", MISION_PROPIA),
]


# =====================================================================
#  PROGRAMA PRINCIPAL
# =====================================================================
def main():
    robot = Robot()
    robot.conectar()
    try:
        for nombre, mision in MISIONES_A_EJECUTAR:
            print(f"\n################ {nombre} ################")
            historial = []          # un historial nuevo por mision
            ejecutar_mision(robot, mision, historial)
            generar_reporte(historial)
    finally:
        robot.detenerse()
        robot.desconectar()


if __name__ == "__main__":
    main()
