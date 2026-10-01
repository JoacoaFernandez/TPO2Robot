# Bitácora técnica — TP02 Programación I (Robot Unitree Go2)

> Se actualiza durante la actividad, no al final.
> Estados: **RESUELTO** · **PARCIAL** · **PENDIENTE** · **NUEVO ERROR**

## Nivel máximo alcanzado hasta ahora: **4** — Verificación del entorno correcta

| Nivel | Evidencia | Estado |
|---|---|---|
| 1 | Python reconocido | ✅ |
| 2 | MuJoCo importado correctamente | ✅ |
| 3 | Modelos Go2 disponibles | ✅ |
| 4 | Verificación del entorno correcta | ✅ |
| 5 | Ventana MuJoCo abierta | ⏳ |
| 6 | Go2 visible | ⏳ |
| 7 | Programa conectado al simulador | ⏳ |
| 8 | `MISION_BASICA` ejecutada | ⏳ |
| 9 | `MISION_CON_ERRORES` procesada sin abortar | ⏳ |
| 10 | Reporte final generado | ⏳ |

---

## Etapa 1 — Caracterización del entorno (01/10/2026)

Relevado **antes** de instalar nada. Evidencia: `evidencias/01_entorno/caracterizacion_inicial.txt`

| Elemento | Información obtenida |
|---|---|
| Sistema operativo | Ubuntu (Linux) |
| Versión del sistema operativo | Ubuntu 26.04.1 LTS (Resolute Raccoon), kernel 7.0.0-34-generic |
| Arquitectura | x86_64 |
| Python instalado | Sí, `/usr/bin/python3` |
| Versión de Python | 3.14.4 (`python3` y `python` apuntan a la misma) |
| pip disponible | Sí, pip 25.1.1 (del sistema) |
| Git disponible | Sí, git 2.53.0 |
| MuJoCo previamente instalado | **No** (`ModuleNotFoundError: No module named 'mujoco'`) |
| IDE utilizado | VS Code |
| Observaciones | El Python del sistema está marcado como `EXTERNALLY-MANAGED` (PEP 668). GPU integrada Intel Arc (Mesa 26.0.8), OpenGL con aceleración por hardware. Sesión gráfica Wayland. |

Comandos usados: `python3 --version`, `python --version`, `python3 -m pip --version`, `git --version`, `python3 -c "import mujoco; ..."`, `uname -a`, `glxinfo -B`.
En Linux no existe `py -3` (es el lanzador de Windows), por eso se usó `python3`.

---

## Antes de comenzar — Lectura de documentación

Se leyeron `INSTALACION.md` y `LEEME_ESTUDIANTE.md` del repositorio de la cátedra.

**a) ¿Qué herramientas necesita el TP?**
Python 3.10+, MuJoCo (con `pip`) y la carpeta del laboratorio, que ya incluye los modelos del G1 y el Go2. Git sirve para obtener el repo, pero no es obligatorio (se puede descargar el ZIP).

**b) ¿Qué versión de Python se requiere?**
3.10 o superior. Esta PC tiene 3.14.4, que cumple.

**c) ¿Qué componentes ya están instalados en la computadora?**
Python 3.14.4, pip 25.1.1, git 2.53.0, el módulo `venv` y los drivers OpenGL (Mesa/Intel). Faltaba MuJoCo.

**d) ¿Qué componentes del repositorio oficial de Unitree no son necesarios?**
CycloneDDS y `unitree_sdk2_python`. El laboratorio se comunica con el simulador por un socket local (`127.0.0.1`). Tampoco hace falta clonar `unitree_mujoco` aparte: los modelos ya vienen recortados en `entorno/sim/unitree_mujoco/`.

**e) ¿Qué diferencias hay entre el TP en PDF y la versión actual del repositorio?**

| PDF del TP | Repositorio actual |
|---|---|
| Módulo `unitree_sdk_sim.py` / `RobotSimulado` | `robot.py` (puente por socket) / `Robot` |
| `avanzar(distancia, velocidad)` | `avanzar(velocidad, tiempo)`, con distancia = v × t |
| `girar(angulo_en_grados, "izquierda"/"derecha")` | `girar(velocidad_rad_s, tiempo)`; el signo indica el sentido (+ izquierda, − derecha) |
| Comando `"saludo"` → `ejecutar_pose("saludo")` | Comando `"saludar"` → `robot.saludar()` |
| Funciones `inicializar_robot`, `procesar_comando` | Funciones `comando_es_valido`, `ejecutar_comando` |
| Límites: VELOCIDAD_MAX 0.5 m/s, ANGULO_MAX 180°, DISTANCIA_MAX 5 m | Límites: 0.20 m/s, 0.50 rad/s de giro, 10 s por orden |
| Sin manejo de excepciones | El robot lanza `ErrorDeSeguridad` si se superan los límites |

Según el Orientador, para la implementación **prevalece el repositorio**.

---

## Registro de acciones

| Nº | Acción / comando | Resultado | Problema | Solución intentada | Estado |
|---|---|---|---|---|---|
| 1 | Relevamiento del entorno (`python3 --version`, `pip --version`, `git --version`, etc.) | Python 3.14.4, pip 25.1.1, git 2.53.0; MuJoCo no instalado | — | — | RESUELTO |
| 2 | `git clone https://github.com/tsamaan/UadeRobotLab.git` | Clonado OK dentro de `TPO2Robot/UadeRobotLab/` | — | — | RESUELTO |
| 3 | Lectura de `INSTALACION.md` y `LEEME_ESTUDIANTE.md` | Se respondieron las preguntas a–e | — | — | RESUELTO |
| 4 | `python3 -m pip install --user mujoco` (comando de la guía) | `ERROR: Could not find an activated virtualenv (required).` exit 3 | Ver **Problema 1** en `PROBLEMAS.md` | Diagnóstico de la configuración de pip | RESUELTO (ver 6) |
| 5 | `pip config list -v`, `cat ~/.config/pip/pip.conf` | `require-virtualenv = true` en la configuración de usuario | La configuración de pip prohíbe instalar fuera de un venv | — | RESUELTO |
| 6 | `python3 -m venv .venv` + `source .venv/bin/activate` + `python3 -m pip install mujoco` | Instalado `mujoco-3.14.0` (más numpy, glfw y pyopengl) | — | Entorno virtual dentro de la carpeta del TP | RESUELTO |
| 7 | `python3 -c "import mujoco; print(mujoco.__version__)"` | `3.14.0` | — | — | RESUELTO |
| 8 | `ls entorno/sim/unitree_mujoco/unitree_robots/` | `g1  go2` | — | — | RESUELTO |
| 9 | `cd entorno && python3 -m sim --solo-revisar` | `[OK] Python 3.14.4` · `[OK] MuJoCo v3.14.0` · `[OK] Modelos oficiales de Unitree` · `Todo listo.` | — | — | RESUELTO |
| 10 | `./INICIAR_SIMULADOR.sh` → opción 2 (Go2) | | | | PENDIENTE |
