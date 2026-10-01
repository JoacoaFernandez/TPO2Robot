# Programación I – Orientador TP02 · Robot Unitree Go2

**Temario:** Instalación y verificación del entorno. Registro de problemas. Puesta en marcha del gemelo digital. Desarrollo del controlador de misiones. Evidencias y evaluación del proceso.

---

## 1. Propósito del Trabajo Práctico

El objetivo es desarrollar un controlador de misiones para el robot Unitree Go2 aplicando diseño Top-Down, funciones, arreglos, decisiones, iteraciones y validaciones.

En esta edición, la instalación y configuración del entorno también forman parte del Trabajo Práctico. Se evaluará el proceso completo: instalación, problemas encontrados, análisis, intentos de solución, verificación y, cuando sea posible, puesta en marcha del gemelo digital.

> **IMPORTANTE:** no se evaluará únicamente que el simulador o el programa funcionen. Los errores de instalación y su resolución constituyen evidencia obligatoria del trabajo realizado.

## 2. Material de referencia

- Repositorio UADE Robot Lab: <https://github.com/tsamaan/UadeRobotLab.git>
- Repositorio Unitree Robotics: <https://github.com/unitreerobotics>

Para realizar este TP, la fuente principal de instalación y ejecución será la carpeta `05LaboratoriosTPs/TP02_Programacion_I` del repositorio UADE. Los repositorios oficiales de Unitree se utilizarán como referencia técnica.

> **Atención:** no mezclar procedimientos de instalación. El laboratorio UADE actual está preparado para trabajar con Python y MuJoCo **sin** instalar CycloneDDS ni el SDK oficial de Unitree.

## 3. Antes de comenzar

Antes de instalar cualquier componente deberán leer:

- `INSTALACION.md`
- `LEEME_ESTUDIANTE.md`

Responder en la bitácora:

- a) ¿Qué herramientas necesita el TP?
- b) ¿Qué versión de Python se requiere?
- c) ¿Qué componentes ya están instalados en la computadora?
- d) ¿Qué componentes del repositorio oficial de Unitree no son necesarios para este laboratorio?
- e) ¿Qué diferencias observan entre el TP en PDF y la versión actual del repositorio?

## 4. Etapa 1: caracterización del entorno

Registrar el estado inicial de la computadora antes de realizar modificaciones.

| Elemento | Información obtenida |
|---|---|
| Sistema operativo | |
| Versión del sistema operativo | |
| Arquitectura | |
| Python instalado | |
| Versión de Python | |
| pip disponible | |
| Git disponible | |
| MuJoCo previamente instalado | Sí / No |
| IDE utilizado | |
| Observaciones | |

Realizar capturas de los comandos utilizados. Por ejemplo:

```bash
py -3 --version
python --version
```

No es necesario que ambos comandos funcionen. Si alguno falla, conservar el mensaje y registrarlo como evidencia.

## 5. Etapa 2: obtención del repositorio

Clonar o descargar el repositorio. Si utilizan Git:

```bash
git clone https://github.com/tsamaan/UadeRobotLab.git
```

Ingresar luego a:

```text
UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/
```

**Evidencia requerida:**

- Captura del repositorio obtenido.
- Carpeta `TP02_Programacion_I`.
- Archivos `INSTALACION.md` y `LEEME_ESTUDIANTE.md`.
- Método utilizado para obtener el material.

## 6. Etapa 3: instalación de MuJoCo

Seguir el procedimiento indicado en `INSTALACION.md`.

En Windows:

```bash
py -3 -m pip install mujoco
```

En macOS / Linux:

```bash
python3 -m pip install mujoco
```

Verificar la instalación. Por ejemplo:

```bash
py -3 -c "import mujoco; print(mujoco.__version__)"
```

Registrar obligatoriamente el comando, la salida obtenida, la versión instalada, advertencias, errores y cualquier solución aplicada.

> **Si pip presenta un error de certificados:** no copiar una solución de manera automática. Registrar el mensaje, interpretar el problema y justificar por qué la alternativa probada podría resolverlo.

## 7. Etapa 4: verificación del entorno

Antes de abrir el gemelo digital deberán verificar que el entorno pueda localizar Python, MuJoCo y los modelos del robot.

El objetivo es alcanzar un estado de verificación equivalente a:

```text
[OK] Python
[OK] MuJoCo
[OK] Modelos Unitree
Todo listo
```

Si aparece algún elemento faltante, detenerse y registrar el problema antes de continuar.

## 8. Bitácora técnica obligatoria

Crear un archivo `BITACORA.md` y actualizarlo durante toda la actividad. **No deberá completarse retrospectivamente al finalizar.**

| Nº | Acción / comando | Resultado | Problema | Solución intentada | Estado |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

Estados sugeridos: **RESUELTO – PARCIAL – PENDIENTE – NUEVO ERROR**.

## 9. Registro y análisis de problemas

Cada problema significativo deberá documentarse. No alcanza con indicar «dio error».

```text
Problema N.º ___
Qué se estaba intentando hacer:
Comando ejecutado:
Resultado esperado:
Resultado obtenido:
Mensaje de error:
Interpretación del grupo:
Hipótesis sobre la causa:
Solución 1 intentada y resultado:
Solución 2 intentada y resultado:
Estado final: Resuelto / Parcial / No resuelto.
Evidencia: captura, log o salida de terminal.
```

**Secuencia esperada:** ERROR → INTERPRETACIÓN → HIPÓTESIS → PRUEBA → RESULTADO.

## 10. Etapa 5: puesta en marcha del gemelo digital

Una vez verificado el entorno, ejecutar el lanzador correspondiente.

- Windows: `INICIAR_SIMULADOR.bat`
- macOS / Linux: `INICIAR_SIMULADOR.sh`

El lanzador permite seleccionar el robot. Para este Trabajo Práctico utilizar:

```text
1 - G1
2 - Go2

Seleccionar: 2 - Go2
```

**Evidencia obligatoria:**

- Selección del robot.
- Terminal de inicio.
- Ventana de MuJoCo.
- Robot Unitree Go2 visible.
- Mensajes de estado del simulador.

## 11. Si el gemelo digital no inicia

No abandonar el Trabajo Práctico. Registrar y analizar el problema. Entre las dificultades posibles se encuentran:

- Python no reconocido.
- MuJoCo instalado en otro intérprete de Python.
- Problemas de certificados al instalar con pip.
- Falta de soporte para la ventana 3D.
- Simulador anterior todavía ejecutándose.
- Programa ejecutado antes de iniciar el simulador.
- Uso accidental de una guía antigua.
- Intento de instalar CycloneDDS o el SDK oficial sin ser necesarios para este TP.

Un grupo que no logre abrir la ventana 3D deberá documentar hasta qué punto llegó y cuáles fueron los intentos realizados. El proceso de diagnóstico será evaluado.

## 12. Arquitectura que deberán comprender

Antes de programar, explicar brevemente el circuito de comunicación utilizado por el laboratorio:

```text
mi_tp02.py
   |
   | robot.avanzar(...) / robot.girar(...) / robot.detenerse()
   v
robot.py      (puente: no se modifica)
   |
   | socket local 127.0.0.1
   v
Gemelo digital: MuJoCo + modelo Unitree Go2
```

El archivo `robot.py` funciona como puente entre el código del alumno y el simulador. **No deberá modificarse.**

## 13. Etapa 6: primer programa contra el gemelo digital

Con el simulador ya abierto, ejecutar el programa desde otra terminal.

Windows:

```bash
EJECUTAR_MI_CODIGO.bat
```

Alternativamente, desde la carpeta del TP:

```bash
python mi_desarrollo/mi_tp02.py
```

Registrar la conexión, la salida de la terminal, el movimiento observado en el robot y cualquier error.

## 14. Desarrollo del TP de Programación I

Trabajar sobre la plantilla vigente del repositorio:

```text
mi_desarrollo/mi_tp02.py
```

La resolución deberá mantener un diseño modular. La versión actual propone trabajar, entre otras, con funciones equivalentes a:

```python
comando_es_valido(comando)
ejecutar_comando(robot, comando)
ejecutar_mision(robot, mision, historial)
generar_reporte(historial)
```

Se evaluará que las funciones tengan responsabilidades claras, que la misión pueda cambiar sin reescribir toda la solución y que los comandos inválidos sean detectados, registrados y no detengan la ejecución.

## 15. Diferencia importante respecto del TP en PDF

Usar la API vigente del repositorio. La versión actual expresa los movimientos mediante **velocidad y tiempo**.

```python
robot.avanzar(velocidad, tiempo)  # m/s, segundos
robot.girar(velocidad, tiempo)    # rad/s, segundos
```

Por lo tanto:

- distancia = velocidad × tiempo
- ángulo = velocidad × tiempo
- en `girar()`, el signo de la velocidad angular indica el sentido: **positivo = izquierda; negativo = derecha**.

No mezclar esta modalidad con ejemplos anteriores expresados como distancia/velocidad o ángulo/sentido. **Para la implementación, prevalece la plantilla actual del repositorio.**

## 16. Pruebas obligatorias

La solución deberá probarse progresivamente con las misiones incluidas en el repositorio:

- `MISION_BASICA`
- `MISION_CON_ERRORES`
- `MISION_CUADRADO`

`MISION_CON_ERRORES` contiene errores deliberados. El objetivo es verificar que el programa pueda:

1. **DETECTAR** el comando incorrecto
2. **RECHAZARLO**
3. **REGISTRAR** el motivo
4. **CONTINUAR** con el resto de la misión

Además deberán crear una misión propia y documentar su ejecución.

## 17. Niveles de avance y evidencia

Al finalizar, indicar claramente el máximo nivel alcanzado:

| Nivel | Evidencia esperada |
|---|---|
| 1 | Python reconocido |
| 2 | MuJoCo importado correctamente |
| 3 | Modelos Go2 disponibles |
| 4 | Verificación del entorno correcta |
| 5 | Ventana MuJoCo abierta |
| 6 | Go2 visible |
| 7 | Programa conectado al simulador |
| 8 | `MISION_BASICA` ejecutada |
| 9 | `MISION_CON_ERRORES` procesada sin abortar |
| 10 | Reporte final generado |

No alcanzar el nivel 10 no implica automáticamente desaprobar. El equipo deberá demostrar hasta dónde llegó y qué proceso de diagnóstico realizó.

## 18. Organización de la entrega

Organizar el material de manera que pueda reconstruirse el proceso realizado. Estructura sugerida:

```text
TP02_Apellido/
|-- README.md
|-- BITACORA.md
|-- PROBLEMAS.md
|-- codigo/
|   `-- tp02_apellido.py
|-- evidencias/
|   |-- 01_entorno/
|   |-- 02_instalacion/
|   |-- 03_errores/
|   |-- 04_soluciones/
|   |-- 05_gemelo_digital/
|   `-- 06_misiones/
`-- CONCLUSIONES.md
```

Las capturas deberán ser legibles y estar acompañadas por una explicación breve. No incluir capturas sin contexto.

## 19. Criterios de evaluación

| Criterio | Puntaje |
|---|---|
| Caracterización inicial del entorno y análisis de documentación | 10 |
| Instalación y verificación reproducible del entorno | 20 |
| Identificación, análisis y resolución de problemas | 20 |
| Puesta en marcha y evidencia del gemelo digital | 15 |
| Resolución del controlador de misiones de Programación I | 25 |
| Bitácora, evidencias y conclusión técnica | 10 |
| **TOTAL** | **100** |

Para obtener el puntaje máximo no será suficiente mostrar el gemelo digital funcionando. Deberá existir evidencia del proceso que permitió llegar a ese resultado.

Del mismo modo, un grupo que alcance una etapa intermedia podrá obtener una evaluación favorable si presenta un diagnóstico técnico serio, pruebas coherentes y documentación suficiente.

## 20. Cierre y reflexión

Responder al finalizar:

- a) ¿Cuál fue la principal dificultad de instalación?
- b) ¿Qué error requirió mayor investigación?
- c) ¿Qué solución resultó efectiva y por qué?
- d) ¿Qué intento no funcionó y qué aprendieron de él?
- e) ¿Qué diferencia encontraron entre una guía antigua y la arquitectura actual?
- f) ¿Hasta qué nivel lograron avanzar?
- g) Si tuvieran que continuar trabajando, ¿cuál sería el próximo paso?

## Actividad para el Portfolio

Entregar:

- URL del repositorio del trabajo.
- `BITACORA.md` completa.
- Evidencias de instalación y verificación.
- Registro de los problemas detectados y las soluciones intentadas.
- Código fuente del controlador de misiones.
- Capturas de las misiones ejecutadas.
- Evidencia del gemelo digital, si se logró la puesta en marcha.
- Conclusión/reflexión final.
