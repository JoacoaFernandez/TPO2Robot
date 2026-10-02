# Informe — TP02 Controlador de misiones

**Joaquín Fernández** · Programación I · turno noche, jueves

## 1. Diseño Top-Down aplicado

Partí del problema general, "ejecutar cualquier misión sin que un comando malo la corte", y lo dividí en cuatro sub-problemas, uno por función: **validar** un comando (`comando_es_valido`), **ejecutar** un comando (`ejecutar_comando`), **recorrer** la misión (`ejecutar_mision`) e **informar** (`generar_reporte`). El `main()` solo las combina y tiene 11 líneas.

Al implementar la validación apareció un sub-problema más: el reporte tiene que mostrar el *motivo* de cada rechazo, y un `True`/`False` no alcanza para eso. Lo resolví bajando un nivel más: `motivo_de_rechazo()` devuelve el texto del problema (o `None`), y `comando_es_valido()` queda en una línea que la reutiliza, sin duplicar lógica. Lo mismo con `es_numero()`, que encapsula la pregunta "¿esto es un número de verdad?".

Cada función se probó **sola** antes de conectarla a la siguiente. La parte 1 se probó sin robot, y las partes 2 a 4 con un robot falso que usa los mismos validadores que el real. Así, cuando llegó el turno del simulador, todo funcionó en el primer intento.

## 2. Pasaje por valor y por referencia (lo observado)

- **Por valor (inmutables):** `velocidad` y `tiempo` llegan a `ejecutar_comando()` como números. Si la función les reasignara otro valor, la tupla original de la misión no cambiaría. Además, las tuplas no se pueden modificar: la misión queda protegida.
- **Por referencia (mutable):** `historial` es una lista. `ejecutar_mision()` le hace `historial.append(...)` y **no devuelve nada** (la prueba lo muestra: devuelve `None`). Aun así, al terminar, la lista que creó `main()` tiene un registro por comando. La función y `main()` trabajan sobre **el mismo objeto**, no sobre una copia.
- Por eso `main()` crea un `historial = []` **nuevo por cada misión**. Si reutilizara la misma lista, los reportes de las misiones se mezclarían.

## 3. ¿Qué tuve que cambiar para ejecutar mi propia misión?

**Ninguna función.** Agregué la lista `MISION_PROPIA` (un triángulo de 0.5 m de lado con saludo, 11 comandos, 3 inválidos a propósito) y la sumé a `MISIONES_A_EJECUTAR`. El programa la procesó igual que las de la cátedra.

Antes de correrla calculé a mano lo esperado: 8 ejecutados, 3 rechazados, 1.5 m, 360°, 20.07 s. El reporte dio exactamente eso. Los 3 errores eran realistas: un giro de 12.6 s (más que el máximo de 10 s), una velocidad de 0.25 m/s (apenas por encima de 0.20) y `"Saludar"` con mayúscula.

## 4. Decisiones que vale la pena justificar

- **Validación más estricta que la del robot.** El robot convierte con `float()`, así que aceptaría `"0.2"` (texto) y velocidades negativas en `avanzar`. Mi validación exige el tipo correcto con `isinstance`, excluye `bool` (en Python `True` es un `int`) y pide velocidad positiva para avanzar.
- **`try/except ErrorDeSeguridad` igual.** Es la segunda red: si un comando se escapara de mi validación, el robot lo rechaza, el programa lo atrapa, frena el robot y sigue.
- **Constantes en lugar de números sueltos.** Todos los límites salen de `VELOCIDAD_MAX`, `VELOCIDAD_GIRO_MAX` y `TIEMPO_MAX`, iguales al perfil `tp02` de la cátedra.
