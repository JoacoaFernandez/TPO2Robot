# TP 02 · Programación I · TPO

**Universidad Argentina de la Empresa (UADE) — Carreras de Informática**

## Controlador de misiones: funciones, arreglos y decisiones

*Diseño Top-Down, funciones con parámetros y procesamiento de arreglos aplicados al robot Unitree Go2*

| Duración taller | Modalidad | Robot | Trabajo | Nivel |
|---|---|---|---|---|
| 2 horas | TPO — Obligatorio | Unitree Go2 | Individual o en parejas | Básico |

---

## 1. Título del Trabajo Práctico

Controlador de misiones: funciones, arreglos y decisiones

## 2. Materia

Programación I — Carreras de Informática, UADE

## 3. Duración Estimada

**Taller presencial:** 2 horas (120 minutos). El tiempo incluye presentación del problema, diseño Top-Down guiado, implementación por partes y cierre con reporte generado.

**Extensión como TP evaluable:** El alumno amplía el programa para aceptar misiones leídas desde un archivo de texto, implementar validaciones más complejas y generar un reporte detallado por cada comando.

Duración estimada de la extensión: 1 a 2 semanas fuera del horario de clase.

## 4. Fundamentación

En el TP anterior (Fundamentos de Informática) los alumnos escribieron su primera secuencia fija de comandos: un script que ejecuta siempre los mismos pasos en el mismo orden. Ese enfoque es suficiente para entender qué es un programa, pero no escala: si queremos cambiar la misión del robot, tenemos que reescribir el código.

Programación I introduce las herramientas que permiten construir programas reutilizables: funciones que encapsulan comportamiento, parámetros que les permiten recibir datos externos, arreglos que almacenan colecciones de valores, y estructuras de control que toman decisiones en tiempo de ejecución. El objetivo de este TP es que el alumno experimente directamente por qué estas herramientas son necesarias: al programar el robot para que ejecute cualquier secuencia de comandos —no una fija—, se enfrenta de manera natural a los problemas que esas herramientas resuelven.

El diseño Top-Down es el hilo conductor: antes de escribir una sola línea de código, el alumno debe descomponer el problema en funciones. Este hábito, central en la materia, se vuelve concreto y significativo cuando el "problema" es hacer que un robot ejecute una misión correctamente.

## 5. Objetivos Generales

- Aplicar el diseño Top-Down para descomponer un programa en funciones con responsabilidades claras.
- Implementar funciones con parámetros y valores de retorno, distinguiendo pasaje por valor y por referencia.
- Usar arreglos (listas en Python) para representar y procesar colecciones de datos.
- Combinar estructuras de control de flujo (bucles y condicionales) para procesar secuencias de comandos con validación.
- Generar un reporte automático a partir del historial de ejecución almacenado en un arreglo.

## 6. Objetivos Específicos

- Diseñar un esquema Top-Down del programa antes de implementarlo, identificando al menos cuatro funciones diferenciadas.
- Implementar la función `ejecutar_mision(robot, mision, historial)` que recorre un arreglo de comandos con un bucle `for` y llama a `procesar_comando()` por cada elemento.
- Implementar `procesar_comando(robot, tipo, params, historial)` que recibe el tipo de comando y sus parámetros por valor, y ejecuta la acción correspondiente.
- Validar cada comando con condiciones que combinen operadores lógicos (`and`, `not`, `in`) con precedencia explícita.
- Almacenar el historial de ejecución en una lista mutable (pasaje por referencia implícito en Python) y generar un reporte final a partir de ella.
- Usar al menos dos funciones de biblioteca estándar: `len()`, `round()`, `isinstance()` o `time.time()`.

## 7. Contenidos de la Materia que se Trabajan

- **Programación estructurada:** solución construida exclusivamente con secuencia, decisión e iteración; sin saltos arbitrarios ni duplicación de lógica entre funciones.
- **Diseño Top-Down:** descomposición del problema "ejecutar una misión variable" en sub-problemas: `inicializar_robot()`, `procesar_comando()`, `ejecutar_mision()`, `generar_reporte()`. Cada función se diseña en papel antes de implementarse.
- **Tipos de datos y operadores:** enteros y flotantes para velocidad, distancia y ángulo; cadenas para el tipo de comando; booleanos para estado de validación; operadores de comparación (`>`, `==`, `in`) y lógicos (`and`, `not`) con precedencia explícita.
- **Constantes:** `VELOCIDAD_MAX`, `ANGULO_MAX`, `DISTANCIA_MAX` y `BATERIA_MIN` definidas al inicio del archivo como nombres en mayúscula, no como literales dispersos en el código.
- **Funciones:** definición con `def`, parámetros posicionales, parámetros con valor por defecto, retorno de valores con `return`. Separación de responsabilidades: cada función hace exactamente una cosa.
- **Declaraciones locales y globales:** las constantes son globales; las variables de estado del bucle (`cmd`, `tipo`, `resultado`) son locales a cada función; el alumno identifica y argumenta el alcance de cada variable.
- **Sentencias de control de flujo:** `for` para iterar el arreglo de misión; `if/elif/else` para despachar el tipo de comando; `continue` para saltear comandos inválidos sin interrumpir la misión.
- **Pasaje de parámetros por valor y por referencia:** los valores numéricos (velocidad, ángulo, distancia) se pasan por valor; la lista `historial` se pasa por referencia (es un objeto mutable) y se modifica dentro de las funciones sin necesidad de retornarla.
- **Arreglos:** la misión se representa como una lista de tuplas `[(tipo, param1, param2), ...]`; el historial de ejecución como una lista de diccionarios que crece en cada iteración del bucle.
- **Funciones de biblioteca:** `len()` para contar comandos, `round()` para formatear distancias, `isinstance()` para validar tipos de parámetros, `time.time()` para medir duración de la misión.
- **Compilación, vinculación y depuración:** uso del entorno de desarrollo para identificar errores de tipo (`TypeError`), errores de índice (`IndexError`) y errores lógicos en las condiciones de validación.

## 8. Descripción General de la Actividad

En este TP los alumnos construirán un programa modular que permite ejecutar cualquier misión sobre el robot Unitree Go2, no solo una secuencia fija. Una misión se representa como un arreglo de comandos, donde cada elemento indica qué debe hacer el robot y con qué parámetros. El programa recorre ese arreglo, valida cada comando y lo ejecuta si es correcto; si un comando es inválido, lo registra en el historial y continúa con el siguiente sin abortar la misión.

El proceso de trabajo sigue el diseño Top-Down: antes de escribir código, el alumno dibuja la estructura del programa identificando las funciones necesarias y las responsabilidades de cada una. Luego implementa cada función por separado y las integra en un programa principal de pocas líneas.

Al finalizar la misión, el programa genera automáticamente un reporte con las estadísticas de ejecución: comandos recibidos, ejecutados, omitidos, distancia total recorrida y duración estimada. El alumno puede cambiar el arreglo de misión sin tocar ninguna función, comprobando directamente la ventaja del diseño modular.

## 9. Modalidad de Trabajo

**Organización:** Individual o en parejas (a criterio del docente).

**Modalidad tecnológica disponible:**

- **Simulado con logs (recomendado para el taller):** Se utiliza el módulo `unitree_sdk_sim.py` provisto por la cátedra. No requiere conexión ni robot físico.
- **Con datos reales (robot encendido, sin movimiento):** Los alumnos conectan al robot en modo lectura y verifican que el estado retornado coincide con el que usaron en la simulación.
- **Robot real supervisado:** El docente ejecuta en el robot físico la misión desarrollada por el mejor equipo como demostración final. Solo bajo supervisión directa y en zona delimitada.

## 10. Recursos Necesarios

### Software

- Python 3.10 o superior instalado en la PC del alumno.
- Módulo simulador de SDK: `unitree_sdk_sim.py` (el mismo del TP01, versión 1.1 con soporte de historial).
- Editor de código: VS Code, PyCharm Community o IDLE.

### Hardware

- PC o notebook con Python 3.10+ (para modalidad simulada, no se requiere hardware adicional).
- Robot Unitree Go2 (opcional, para demostración supervisada al final del taller).
- Red Wi-Fi del laboratorio si se usa robot real.

### Archivos provistos por la cátedra

- `unitree_sdk_sim.py`: módulo simulador del SDK (versión 1.1).
- `tp02_plantilla.py`: archivo de inicio con la estructura Top-Down esbozada y los `pass` a completar.
- `tp02_misiones.py`: archivo con tres misiones de ejemplo en formato de lista de tuplas.
- `tp02_consigna.pdf`: consigna impresa para referencia durante el taller.

## 11. Desarrollo del Taller de 2 Horas

| Tiempo | Actividad del Docente | Actividad de los Alumnos |
|---|---|---|
| 00–10 min | Presenta el problema: "¿Cómo haríamos para que el robot ejecute misiones diferentes sin reescribir el código cada vez?" Conecta con el TP01 como punto de partida. | Recuerdan lo implementado en TP01. Reflexionan sobre las limitaciones de la secuencia fija. |
| 10–25 min | Guía el diseño Top-Down en pizarrón: dibuja el esquema de funciones con sus entradas, salidas y responsabilidades. Explica la representación de una misión como lista de tuplas. | Copian el esquema en su cuaderno o lo proponen ellos mismos. Discuten qué debería verificar la función de validación. |
| 25–40 min | Muestra el archivo plantilla proyectado: explica los `pass` a completar, la estructura de constantes globales y la función `main()` ya implementada. | Abren el archivo plantilla, leen el código y lo ejecutan. Observan que el reporte aparece vacío porque las funciones aún no hacen nada. |
| 40–65 min | Guía la implementación de `procesar_comando()` paso a paso: primero el caso "avanzar", luego "girar" y "detenerse". Detiene al grupo para discutir la validación con operadores lógicos y precedencia. | Implementan cada caso de la función, ejecutan con una misión de tres comandos y verifican los logs. Ajustan la condición para rechazar valores fuera de rango. |
| 65–85 min | Propone implementar `ejecutar_mision()` con el bucle `for` y el `continue` para comandos inválidos. Muestra la diferencia entre modificar una lista dentro de una función vs. modificar un entero. | Implementan el bucle, agregan un comando inválido a la misión de prueba y verifican que el programa lo saltea sin fallar. Analizan por qué la lista se modifica sin retornarla. |
| 85–105 min | Propone implementar `generar_reporte()` usando `len()`, `round()` y una iteración sobre el historial. Recorre los puestos y resuelve dudas. | Generan el reporte con los datos reales de la misión. Quienes terminaron prueban con la misión 2 y la misión 3 del archivo de ejemplos sin cambiar ninguna función. |
| 105–120 min | Conduce el cierre: invita a dos equipos a mostrar su reporte en pantalla. Plantea la reflexión: "¿Tuvieron que cambiar alguna función para ejecutar la misión 3?" | Muestran sus resultados. Reflexionan sobre el beneficio del diseño modular. Proponen nuevos tipos de comandos que agregarían. |

## 12. Consigna para los Alumnos

> **Trabajo Práctico N° 2 — Programación I**
>
> Implementá en Python un programa modular que permita al robot Unitree Go2 ejecutar cualquier misión representada como una lista de comandos. El programa debe seguir el diseño Top-Down discutido en clase y respetar las siguientes consignas:
>
> 1. Definí las constantes `VELOCIDAD_MAX = 0.5`, `DISTANCIA_MAX = 5.0`, `ANGULO_MAX = 180` y `BATERIA_MIN = 15` al inicio del archivo.
> 2. Implementá `inicializar_robot()`: conecta el robot y retorna `None` si la batería es insuficiente.
> 3. Implementá `procesar_comando(robot, tipo, params, historial)`: valida el tipo y los parámetros, ejecuta el comando si es válido y agrega el resultado al historial. Los parámetros numéricos llegan por valor; la lista `historial` se modifica directamente.
> 4. Implementá `ejecutar_mision(robot, mision, historial)`: recorre el arreglo `mision` con un bucle `for` y llama a `procesar_comando()` por cada elemento. Usá `continue` para saltear comandos inválidos.
> 5. Implementá `generar_reporte(historial)`: imprime el total de comandos recibidos, ejecutados y omitidos, la distancia total recorrida (redondeada a 2 decimales) y la duración estimada de la misión.
> 6. En el bloque `main()`, ejecutá la misión provista por la cátedra y luego una misión propia de al menos 5 comandos, incluyendo intencionalmente al menos un comando inválido.
>
> **Entregables:** archivo `tp02_apellido.py`, captura del reporte generado para ambas misiones, esquema Top-Down e informe de máximo una página.

## 13. Desarrollo Técnico Esperado

El programa utiliza el módulo `unitree_sdk_sim` para conectar y operar el robot (igual que en TP01). La diferencia estructural es que el programa ya no sabe de antemano qué comandos va a ejecutar: recibe la lista `mision` como parámetro y la procesa en tiempo de ejecución.

La función `procesar_comando()` actúa como un despachador: recibe el tipo de comando como cadena, lo compara contra los tipos válidos y decide qué método del robot llamar. Los parámetros numéricos se validan contra las constantes globales usando condiciones compuestas; la precedencia importa: `0 < velocidad <= VELOCIDAD_MAX and isinstance(velocidad, float)` debe evaluarse correctamente para no aceptar valores de tipo erróneo.

La lista `historial` es el mecanismo de trazabilidad: cada llamada a `procesar_comando()` agrega un diccionario con el resultado de ese comando. Como las listas en Python son objetos mutables, la función puede modificar `historial` directamente sin necesidad de retornarla —ilustrando el pasaje por referencia de manera natural. La función `generar_reporte()` recorre esa lista para calcular las estadísticas finales.

## 14. Ejemplo de Estructura de Código

> Nota: en el PDF algunas líneas largas aparecen cortadas; acá se completaron de forma obvia (cierre de docstrings y strings).

```python
# TP02 - Programación I
# Controlador de misiones: funciones, arreglos y decisiones
# Módulo: unitree_sdk_sim (provisto por la cátedra)

import time
from unitree_sdk_sim import RobotSimulado

# --- Constantes globales ---
VELOCIDAD_MAX    = 0.5    # m/s
DISTANCIA_MAX    = 5.0    # metros
ANGULO_MAX       = 180    # grados
BATERIA_MIN      = 15     # porcentaje mínimo para operar
COMANDOS_VALIDOS = ("avanzar", "girar", "detenerse", "saludo")

# --- Funciones ---

def inicializar_robot():
    """Conecta el robot y retorna la instancia, o None si la batería es insuficiente."""
    robot = RobotSimulado(modelo="Go2", log=True)
    robot.conectar()
    estado = robot.verificar_estado()
    print(f"[INFO] Batería: {estado.bateria}%  |  Conexión: {estado.conexion}")
    if estado.bateria < BATERIA_MIN:
        print("[ALERTA] Batería insuficiente. Misión cancelada.")
        robot.desconectar()
        return None
    return robot


def procesar_comando(robot, tipo, params, historial):
    """Valida y ejecuta un comando; registra el resultado en historial (por referencia)."""
    registro = {"tipo": tipo, "params": params, "ejecutado": False, "motivo": ""}

    if tipo not in COMANDOS_VALIDOS:
        registro["motivo"] = f"Tipo desconocido: '{tipo}'"
        historial.append(registro)
        print(f"[OMITIDO] {registro['motivo']}")
        return

    if tipo == "avanzar":
        distancia, velocidad = params[0], params[1]
        if not (0 < distancia <= DISTANCIA_MAX and 0 < velocidad <= VELOCIDAD_MAX):
            registro["motivo"] = "Parámetros fuera de rango"
            historial.append(registro)
            print(f"[OMITIDO] avanzar({distancia}m, {velocidad}m/s) — {registro['motivo']}")
            return
        duracion = round(distancia / velocidad, 2)
        robot.avanzar(velocidad=velocidad, duracion=duracion)
        registro["distancia"] = distancia

    elif tipo == "girar":
        angulo, sentido = params[0], params[1]
        if not (0 < angulo <= ANGULO_MAX and sentido in ("izquierda", "derecha")):
            registro["motivo"] = "Parámetros fuera de rango"
            historial.append(registro)
            print(f"[OMITIDO] girar({angulo}°, {sentido}) — {registro['motivo']}")
            return
        robot.girar(angulo=angulo, sentido=sentido)

    elif tipo == "detenerse":
        robot.detenerse()

    elif tipo == "saludo":
        robot.ejecutar_pose("saludo")

    registro["ejecutado"] = True
    historial.append(registro)
    print(f"[OK] {tipo} ejecutado con params={params}")


def ejecutar_mision(robot, mision, historial):
    """Recorre el arreglo de misión y despacha cada comando."""
    print(f"\n=== Iniciando misión: {len(mision)} comando(s) ===")
    inicio = time.time()
    for cmd in mision:
        tipo   = cmd[0]
        params = cmd[1:] if len(cmd) > 1 else ()
        procesar_comando(robot, tipo, params, historial)
    historial.append({"_duracion": round(time.time() - inicio, 2)})
    print("=== Misión finalizada ===\n")


def generar_reporte(historial):
    """Genera e imprime las estadísticas finales de la misión."""
    ejecutados = sum(1 for r in historial if r.get("ejecutado"))
    omitidos   = sum(1 for r in historial if "tipo" in r and not r.get("ejecutado"))
    distancia  = round(sum(r.get("distancia", 0) for r in historial), 2)
    duracion   = next((r["_duracion"] for r in historial if "_duracion" in r), 0)

    print("=" * 35)
    print("        REPORTE DE MISIÓN")
    print("=" * 35)
    print(f"  Comandos recibidos:  {ejecutados + omitidos}")
    print(f"  Comandos ejecutados: {ejecutados}")
    print(f"  Comandos omitidos:   {omitidos}")
    print(f"  Distancia recorrida: {distancia} m")
    print(f"  Duración estimada:   {duracion} s")
    print("=" * 35)


def main():
    mision = [
        ("avanzar",   1.5, 0.3),
        ("girar",      90, "derecha"),
        ("avanzar",   2.0, 0.5),
        ("girar",     -45, "izquierda"),   # ángulo negativo — inválido
        ("avanzar",  10.0, 0.3),           # distancia fuera de rango — inválido
        ("detenerse",),
        ("saludo",),
    ]
    historial = []
    robot = inicializar_robot()
    if robot is None:
        return
    ejecutar_mision(robot, mision, historial)
    generar_reporte(historial)
    robot.desconectar()


if __name__ == "__main__":
    main()
```

**Salida esperada en consola (modo simulado):**

```text
[SIM] Conectando al robot Go2...
[INFO] Batería: 91%  |  Conexión: True

=== Iniciando misión: 7 comando(s) ===
[SIM] Avanzando a 0.3 m/s durante 5.0 s
[OK] avanzar ejecutado con params=(1.5, 0.3)
[SIM] Girando 90° hacia la derecha
[OK] girar ejecutado con params=(90, 'derecha')
[SIM] Avanzando a 0.5 m/s durante 4.0 s
[OK] avanzar ejecutado con params=(2.0, 0.5)
[OMITIDO] girar(-45°, izquierda) — Parámetros fuera de rango
[OMITIDO] avanzar(10.0m, 0.3m/s) — Parámetros fuera de rango
[SIM] Deteniendo robot...
[OK] detenerse ejecutado con params=()
[SIM] Ejecutando pose: saludo
[OK] saludo ejecutado con params=()
=== Misión finalizada ===

===================================
        REPORTE DE MISIÓN
===================================
  Comandos recibidos:  7
  Comandos ejecutados: 5
  Comandos omitidos:   2
  Distancia recorrida: 3.5 m
  Duración estimada:   9.14 s
===================================
```

## 15. Entregables

- **Archivo `tp02_apellido.py`:** programa completo con las cuatro funciones implementadas, comentadas y ejecutables sin errores.
- **Captura del reporte generado:** salida de consola al ejecutar tanto la misión de la cátedra como la misión propia (mínimo 5 comandos, al menos uno inválido intencionalmente).
- **Esquema Top-Down:** fotografía del esquema dibujado en papel o diagrama digital con las funciones, sus entradas y salidas, previo a la implementación.
- **Informe breve (máx. 1 página):** explicación del diseño Top-Down aplicado, análisis de la diferencia entre pasaje por valor y por referencia observada en la práctica, y respuesta a: "¿Qué tuviste que cambiar para ejecutar tu propia misión?"

## 16. Criterios de Evaluación

- Las cuatro funciones están correctamente definidas, son independientes y tienen responsabilidades claras.
- El bucle `for` en `ejecutar_mision()` procesa todos los comandos correctamente, usando `continue` para los inválidos.
- La validación usa condiciones con operadores lógicos y respeta la precedencia correcta.
- Las constantes globales se usan en lugar de literales numéricos dispersos en el código.
- La lista `historial` refleja exactamente lo que sucedió (comandos ejecutados y omitidos con sus motivos).
- El programa ejecuta misiones distintas sin modificar ninguna función.
- El informe demuestra comprensión del diseño Top-Down y del pasaje de parámetros por referencia.

## 17. Rúbrica de Evaluación

| Criterio | Indicadores de logro | Puntaje máximo |
|---|---|---|
| Diseño Top-Down | Entrega el esquema previo a la implementación. Las cuatro funciones tienen responsabilidades claramente diferenciadas. La función `main()` tiene menos de 15 líneas. | 20 |
| Implementación de funciones | `procesar_comando()` cubre todos los tipos de comando válidos. `ejecutar_mision()` itera correctamente con `for`. `generar_reporte()` produce estadísticas correctas. Sin errores en ejecución. | 30 |
| Validación y control de flujo | Comandos inválidos son omitidos con `continue` y registrados en el historial. Las condiciones usan operadores lógicos con precedencia correcta. El programa no falla ante entradas inesperadas. | 20 |
| Arreglos y pasaje de parámetros | La misión es una lista de tuplas. El historial se modifica dentro de las funciones sin ser retornado. Se usan al menos dos funciones de biblioteca (`len()`, `round()`, etc.). | 15 |
| Misión propia y reporte | La misión propia tiene al menos 5 comandos incluyendo uno intencionalmente inválido. El reporte de ambas misiones coincide con la ejecución real observada en la captura de pantalla. | 15 |
| | **TOTAL** | **100** |

## 18. Medidas de Seguridad

**Modalidad simulada (sin robot físico):** No hay riesgos físicos. Toda la actividad transcurre en la PC del alumno. La constante `VELOCIDAD_MAX = 0.5` m/s está definida en el código como restricción de diseño aunque no haya robot real.

**Si se usa el robot físico (demostración final supervisada):**

- El robot solo puede encenderse con el docente presente y habilitado por él.
- Debe delimitarse una zona de trabajo de al menos 2 m × 2 m libre de personas y objetos.
- La velocidad máxima está limitada por la constante `VELOCIDAD_MAX`; el docente verifica que el valor no sea modificado antes de la demostración.
- Los alumnos no tocan el robot mientras está en movimiento.
- El ángulo de giro no puede exceder 180° por comando; valores mayores son rechazados por la función de validación.
- Ante cualquier comportamiento inesperado, el docente activa la parada de emergencia manual.

## 19. Posibles Extensiones del TP

- **Extensión 1 — Lectura desde archivo:** La misión se lee desde un archivo de texto o JSON. El alumno implementa `cargar_mision(ruta)` usando `open()` y `json.load()`.
- **Extensión 2 — Parámetros con valor por defecto:** La función `procesar_comando()` acepta parámetros opcionales con valores por defecto para velocidad y sentido, usando la sintaxis `def procesar_comando(..., velocidad=0.3, sentido="derecha")`.
- **Extensión 3 — Misiones repetibles:** Un bucle en `main()` pregunta al usuario si desea ejecutar otra misión usando `input()`. El historial se reinicia en cada ejecución.
- **Extensión 4 — Análisis previo de misión:** Antes de ejecutar, `analizar_mision(mision)` muestra un resumen de los comandos planificados, la distancia estimada y el tiempo estimado sin ejecutar ninguna acción.
- **Extensión 5 (robot real):** Con supervisión docente, ejecutar la misión propia en el Go2 físico y comparar el comportamiento real con el reporte del simulador.

## 20. Resultado Esperado

Al finalizar el taller, cada alumno habrá implementado un programa modular en Python capaz de procesar cualquier misión representada como un arreglo de comandos. El programa demostrará de manera concreta los conceptos centrales de Programación I: el diseño Top-Down como metodología de trabajo previo a la codificación, las funciones como unidades de reutilización con contratos claros, el pasaje de parámetros por valor y por referencia, los arreglos como estructura de datos para colecciones variables, y las estructuras de control para tomar decisiones y procesar secuencias. El reporte generado automáticamente evidencia que el programa funciona correctamente y que puede adaptarse a misiones distintas sin modificar su estructura interna.

## 21. Cierre y Reflexión para los Alumnos

> En el TP01 escribieron un script que siempre hace lo mismo. En este TP escribieron un programa que puede hacer cosas distintas dependiendo de los datos que recibe. Esa diferencia —entre código rígido y código flexible— es una de las ideas más importantes de la programación.
>
> Las funciones no son solo una forma de organizar el código: son la manera en que los programadores construyen herramientas reutilizables. Una función bien diseñada hace exactamente una cosa, recibe exactamente lo que necesita y retorna exactamente lo que promete. Cuando todas las funciones cumplen ese contrato, el programa entero se vuelve predecible y fácil de modificar.
>
> ¿Tuvieron que modificar alguna función para ejecutar su misión propia? Si la respuesta es no, diseñaron bien. Si la respuesta es sí, vale la pena preguntarse qué suposición incorrecta hicieron en el diseño inicial y cómo corregirla la próxima vez. Ese análisis —entender por qué algo no funcionó— es exactamente lo que hace un programador profesional.

---

*Universidad Argentina de la Empresa (UADE) | Carreras de Informática | TP02 — Programación I | Ciclo 2025–2026*
