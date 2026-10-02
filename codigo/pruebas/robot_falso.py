# =====================================================================
#  Robot falso para probar mi_tp02.py SIN el simulador abierto.
#
#  Tiene los mismos metodos que el Robot de la catedra, y valida con
#  los MISMOS validadores de safety.py (perfil tp02): rechaza
#  exactamente lo mismo que el robot de verdad, pero no se mueve,
#  solo imprime lo que haria.
#
#  Uso (con el venv activado, desde TPO2Robot/):
#      python3 codigo/pruebas/robot_falso.py
# =====================================================================

import sys
from pathlib import Path

# Para poder importar mi_tp02.py, robot.py y misiones.py de la catedra
MI_DESARROLLO = (Path(__file__).resolve().parents[2]
                 / "UadeRobotLab" / "05LaboratoriosTPs"
                 / "TP02_Programacion_I" / "mi_desarrollo")
sys.path.insert(0, str(MI_DESARROLLO))

import robot  # noqa: E402,F401  (agrega entorno/ al path, como en el TP real)
from sim.safety import (perfil, validar_duracion, validar_velocidad,  # noqa: E402
                        validar_velocidad_angular)


class RobotFalso:
    def __init__(self, sabe_saludar=True):
        self.perfil = perfil("tp02")
        self.sabe_saludar = sabe_saludar
        self.ordenes = []          # lo que el robot llego a ejecutar

    def conectar(self):
        print("    [FALSO] conectado")

    def desconectar(self):
        print("    [FALSO] desconectado")

    def avanzar(self, velocidad, tiempo):
        validar_velocidad(velocidad, self.perfil)
        validar_duracion(tiempo, self.perfil)
        print(f"    [FALSO] avanzar(velocidad={velocidad}, tiempo={tiempo})")
        self.ordenes.append(("avanzar", velocidad, tiempo))

    def girar(self, velocidad, tiempo):
        validar_velocidad_angular(velocidad, self.perfil)
        validar_duracion(tiempo, self.perfil)
        print(f"    [FALSO] girar(velocidad={velocidad}, tiempo={tiempo})")
        self.ordenes.append(("girar", velocidad, tiempo))

    def detenerse(self):
        print("    [FALSO] detenerse()")
        self.ordenes.append(("detenerse",))

    def saludar(self):
        if not self.sabe_saludar:
            raise NotImplementedError("Este robot no tiene un gesto de saludo.")
        print("    [FALSO] saludar()")
        self.ordenes.append(("saludar",))


# ---------------------------------------------------------------------
#  Pruebas de la PARTE 2: ejecutar_comando()
# ---------------------------------------------------------------------
def probar_parte2():
    from mi_tp02 import ejecutar_comando
    from misiones import MISION_BASICA

    print("=== Parte 2 con MISION_BASICA (todo deberia ejecutarse) ===")
    r = RobotFalso()
    for comando in MISION_BASICA:
        print(f"  {comando!r}")
        ejecutado, texto = ejecutar_comando(r, comando)
        print(f"    -> ejecutado={ejecutado}  texto={texto!r}")

    print("\n=== Parte 2: el robot rechaza lo que se escapa de la validacion ===")
    # Se llama a ejecutar_comando SIN validar antes, a proposito,
    # para comprobar que el try/except atrapa el ErrorDeSeguridad.
    for comando in [("avanzar", 0.9, 2.0), ("girar", 3.0, 2.0),
                    ("avanzar", 0.2, 50.0), ("girar", 0.5, 3.14)]:
        print(f"  {comando!r}")
        ejecutado, texto = ejecutar_comando(r, comando)
        print(f"    -> ejecutado={ejecutado}  texto={texto!r}")

    print("\n=== Parte 2: robot que no sabe saludar ===")
    r2 = RobotFalso(sabe_saludar=False)
    ejecutado, texto = ejecutar_comando(r2, ("saludar",))
    print(f"  ('saludar',)\n    -> ejecutado={ejecutado}  texto={texto!r}")


# ---------------------------------------------------------------------
#  Pruebas de la PARTE 3: ejecutar_mision()
# ---------------------------------------------------------------------
def probar_parte3():
    from mi_tp02 import ejecutar_mision
    from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO

    for nombre, mision in [("MISION_BASICA", MISION_BASICA),
                           ("MISION_CON_ERRORES", MISION_CON_ERRORES),
                           ("MISION_CUADRADO", MISION_CUADRADO)]:
        print(f"\n##### Parte 3 con {nombre} #####")
        r = RobotFalso()
        historial = []
        resultado = ejecutar_mision(r, mision, historial)

        ejecutados = sum(1 for h in historial if h["ejecutado"])
        print(f"  -> ejecutar_mision devolvio: {resultado!r} (no hace falta devolver nada)")
        print(f"  -> historial tiene {len(historial)} registros "
              f"(la mision tenia {len(mision)}): {ejecutados} ejecutados, "
              f"{len(historial) - ejecutados} rechazados")
        print(f"  -> el robot recibio {len(r.ordenes)} ordenes (todas las que llego a ejecutar)")

    print("\n##### Historial completo de MISION_CON_ERRORES #####")
    historial = []
    ejecutar_mision(RobotFalso(), MISION_CON_ERRORES, historial)
    for registro in historial:
        print(f"  {registro}")


# ---------------------------------------------------------------------
#  Pruebas de la PARTE 4: generar_reporte()
# ---------------------------------------------------------------------
def probar_parte4():
    from mi_tp02 import ejecutar_mision, generar_reporte
    from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO

    # Valores calculados A MANO para comparar con el reporte:
    #   BASICA:      2 avanzar de 0.2x2.0 = 0.8 m | 1 giro 0.5x3.14 = 90 grados
    #                tiempo 2.0 + 3.14 + 2.0 = 7.14 s
    #   CON_ERRORES: 0.4 m | 90 grados | 5.14 s | 4 ejecutados, 7 rechazados
    #   CUADRADO:    1.6 m | 360 grados | 20.56 s
    esperado = {
        "MISION_BASICA": "4 ejecutados, 0 rechazados, 0.8 m, 90 grados, 7.14 s",
        "MISION_CON_ERRORES": "4 ejecutados, 7 rechazados, 0.4 m, 90 grados, 5.14 s",
        "MISION_CUADRADO": "9 ejecutados, 0 rechazados, 1.6 m, 360 grados, 20.56 s",
    }
    for nombre, mision in [("MISION_BASICA", MISION_BASICA),
                           ("MISION_CON_ERRORES", MISION_CON_ERRORES),
                           ("MISION_CUADRADO", MISION_CUADRADO)]:
        print(f"\n##### Parte 4 con {nombre} #####")
        print(f"  Calculado a mano: {esperado[nombre]}")
        historial = []
        ejecutar_mision(RobotFalso(), mision, historial)
        generar_reporte(historial)

    print("\n##### Parte 4 con historial vacio (mision sin comandos) #####")
    generar_reporte([])


if __name__ == "__main__":
    parte = sys.argv[1] if len(sys.argv) > 1 else "todas"
    if parte in ("2", "todas"):
        probar_parte2()
    if parte in ("3", "todas"):
        probar_parte3()
    if parte in ("4", "todas"):
        probar_parte4()
