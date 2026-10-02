# Bitácora técnica — TP02 Programación I (Robot Unitree Go2)

> Se actualiza durante la actividad, no al final.
> Estados: **RESUELTO** · **PARCIAL** · **PENDIENTE** · **NUEVO ERROR**

## Nivel máximo alcanzado: **10** — Reporte final generado

| Nivel | Evidencia | Estado |
|---|---|---|
| 1 | Python reconocido | ✅ |
| 2 | MuJoCo importado correctamente | ✅ |
| 3 | Modelos Go2 disponibles | ✅ |
| 4 | Verificación del entorno correcta | ✅ |
| 5 | Ventana MuJoCo abierta | ✅ |
| 6 | Go2 visible | ✅ |
| 7 | Programa conectado al simulador | ✅ |
| 8 | `MISION_BASICA` ejecutada | ✅ |
| 9 | `MISION_CON_ERRORES` procesada sin abortar | ✅ |
| 10 | Reporte final generado | ✅ |

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
| 10 | `./INICIAR_SIMULADOR.sh` → opción 2 (Go2) | No se pudo abrir en el primer intento (02/10) | Ver acción 19 | Lanzamiento directo sin el menú | RESUELTO (ver 19) |
| 11 | Lectura de `entorno/sim/safety.py` y `sim/robot.py` antes de programar | Límites del perfil `tp02`: 0.20 m/s, 0.50 rad/s, 10 s. El robot convierte con `float()` (acepta `"0.2"` como texto) y admite velocidad negativa en `avanzar` | La validación del robot es más permisiva que la que pide el TP | La validación propia chequea el tipo con `isinstance` y exige velocidad > 0 para avanzar | RESUELTO |
| 12 | Parte 1: `comando_es_valido()` + auxiliares `es_numero()` y `motivo_de_rechazo()` | Implementada | La plantilla pide devolver `True/False`, pero el reporte necesita el motivo | `motivo_de_rechazo()` devuelve el texto o `None`; `comando_es_valido()` la reutiliza (sin duplicar lógica) | RESUELTO |
| 13 | Prueba aislada de la parte 1 (sin simulador) con `MISION_BASICA`, `MISION_CON_ERRORES` y 14 casos borde | 25/25 casos con el resultado esperado. `MISION_CON_ERRORES`: 4 válidos, 7 inválidos, cada uno con su motivo | — | — | RESUELTO |
| 14 | Parte 2: `ejecutar_comando(robot, comando)` | Implementada con `try/except ErrorDeSeguridad` y `NotImplementedError` | La plantilla pide devolver un texto, pero la parte 3 necesita saber si se ejecutó o no | Devuelve una tupla `(ejecutado, texto)`. En el `except` llama a `robot.detenerse()`, como pide `safety.py` ("rechazar implica frenar") | RESUELTO |
| 15 | Creado `codigo/pruebas/robot_falso.py`: imita al robot usando los mismos validadores de `safety.py` (perfil tp02) | Permite probar sin el simulador abierto | El robot real exige el simulador (`NoHaySimulador`) | Robot falso con los mismos métodos y las mismas reglas de rechazo | RESUELTO |
| 16 | `python3 codigo/pruebas/robot_falso.py` | `MISION_BASICA` 4/4 ejecutados. Comandos fuera de límite mandados **sin validar**: el robot los rechaza, se atrapa el error, se frena y el programa sigue. Saludo no soportado: atrapado | — | — | RESUELTO |
| 17 | Parte 3: `ejecutar_mision(robot, mision, historial)` | Implementada: `for` + `enumerate`, `comando_es_valido()` para decidir, `continue` para saltear inválidos, un diccionario por comando en `historial` | — | — | RESUELTO |
| 18 | `python3 codigo/pruebas/robot_falso.py 3` con BASICA, CON_ERRORES y CUADRADO | BASICA 4/4 · CON_ERRORES 4 ejecutados / 7 rechazados, sin abortar · CUADRADO 9/9. En los 3 casos el historial tiene un registro por comando, y la función devuelve `None` (la lista se modifica por referencia) | — | — | RESUELTO |
| 19 | `python3 -m sim --robot go2 --materia tp02` (lo mismo que hace el lanzador al elegir 2, sin el menú interactivo), con el venv activado | Arrancó: `Robot: Unitree Go2`, `Materia: tp02-programacion-i`, `[LOCAL] Escuchando en 127.0.0.1:8765` | Aviso `Failed to load plugin 'libdecor-gtk.so'` → `falling back on no decorations`: con Wayland la ventana abre sin barra de título | No impide el funcionamiento; no requiere solución | RESUELTO |
| 20 | `python3 mi_desarrollo/mi_tp02.py` (MISION_BASICA) | `[OK] Conectado a Unitree Go2`, 4/4 OK. Posición final `x=+0.40 y=-0.40 rumbo=-90.3°`, coincide con lo calculado (0.4 m, giro 90° a la derecha, 0.4 m) | — | — | RESUELTO |
| 21 | MISION_CUADRADO contra el simulador | 9/9 OK. Volvió al punto de partida (`x=+0.40 y=-0.40`). Rumbo −90.3° → −89.3°: ~1° de deriva acumulada en 4 giros | — | — | RESUELTO |
| 22 | MISION_CON_ERRORES contra el simulador | 4 ejecutados / 7 rechazados con su motivo; la misión no se cortó. El Go2 sí ejecuta `saludar()` | — | — | RESUELTO |
| 23 | Segundo `python3 -m sim --robot go2 --materia tp02` desde otra terminal | `YA HAY UN SIMULADOR ABIERTO (Proceso 227645)` | Quedaba abierto el simulador de la acción 19. Ver **Problema 2** | `ps` para confirmar y `kill -INT 227645` (equivale a Ctrl+C) | RESUELTO |
| 24 | Simulador abierto desde una terminal propia (`python3 -m sim --robot go2 --materia tp02`) + `MISION_CUADRADO` desde una segunda terminal | Ventana de MuJoCo con el Go2 visible; el robot recorre el cuadrado y vuelve al inicio (9/9 OK) | — | — | RESUELTO |
| 25 | Capturas guardadas y descriptas en `evidencias/05_gemelo_digital/LEEME.md` | Niveles 5 y 6 con evidencia gráfica | — | — | RESUELTO |
| 26 | Parte 4: `generar_reporte(historial)` | Implementada: recorre el historial y muestra recibidos, ejecutados, rechazados (con el motivo de cada uno), distancia, total girado y duración estimada. Usa `len()`, `round()`, `abs()` y `math.degrees()` | — | — | RESUELTO |
| 27 | `python3 codigo/pruebas/robot_falso.py 4`, comparando contra valores calculados a mano | BASICA 0.8 m / 90° / 7.14 s · CON_ERRORES 4 ejec. / 7 rech. / 0.4 m / 90° / 5.14 s · CUADRADO 1.6 m / 360° / 20.56 s. Todos coinciden. Con el historial vacío no falla (todo en 0) | — | — | RESUELTO |
| 28 | `python3 mi_desarrollo/mi_tp02.py` (main de la plantilla) contra el simulador Go2 | MISION_BASICA 4/4 y reporte generado: **nivel 10** | — | — | RESUELTO |
| 29 | Encabezado con los datos del alumno, `MISION_PROPIA` (triángulo de 0.5 m de lado + saludo, 11 comandos, 3 inválidos a propósito) y `main()` definitivo que recorre `MISIONES_A_EJECUTAR` con un historial nuevo por misión (11 líneas) | Implementado | — | — | RESUELTO |
| 30 | Revisión: `mi_tp02.py` estaba dentro de `UadeRobotLab/`, que está en `.gitignore` | — | El código fuente **no estaba versionado** | Movido a `codigo/tp02_fernandez_joaquin.py`; en `mi_desarrollo/` queda `mi_tp02.py` como enlace simbólico. Un solo archivo real. Import con `try/except ModuleNotFoundError` para encontrar `robot.py` también desde `codigo/` | RESUELTO |
| 31 | Prueba de imports desde `codigo/`, desde el enlace en `mi_desarrollo/` y desde una copia suelta en `mi_desarrollo/` (como lo usaría el docente) + `robot_falso.py` completo | OK en los 4 casos | — | — | RESUELTO |
| 32 | `python3 mi_desarrollo/mi_tp02.py`: programa completo contra el simulador Go2 | BASICA 4/0 · CON_ERRORES 4/7 · CUADRADO 9/0 · PROPIA 8/3, 1.5 m, 360°, 20.07 s: **coincide con el cálculo a mano**. Ninguna misión abortó | — | — | RESUELTO |
| 33 | Capturas del programa final corriendo contra el simulador (reporte de MISION_CON_ERRORES y de MISION_PROPIA, con el Go2 visible) | Guardadas y descriptas en `evidencias/06_misiones/LEEME.md` (09b, 10 y 11) | — | — | RESUELTO |
| 34 | Borradores de `CONCLUSIONES.md`, `INFORME.md` y `ESQUEMA_TOP_DOWN.md` | Escritos a partir de la bitácora, los problemas y las corridas | — | — | PENDIENTE (revisión del alumno) |
