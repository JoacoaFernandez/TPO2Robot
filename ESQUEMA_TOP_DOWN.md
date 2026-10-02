# Esquema Top-Down — Controlador de misiones

**Joaquín Fernández** · Programación I · turno noche, jueves

## Problema principal

> Hacer que el robot Go2 ejecute **cualquier** misión (una lista de comandos), rechazando los comandos inválidos sin cortar la misión, y que al final informe qué pasó.

## Descomposición

```text
                              main()
                 recorre MISIONES_A_EJECUTAR; por cada una:
                 historial nuevo -> ejecutar -> reportar
                                 │
          ┌──────────────────────┴───────────────────────┐
          ▼                                              ▼
ejecutar_mision(robot, mision, historial)     generar_reporte(historial)
 for + continue; llena el historial            cuenta, suma e imprime
 (no devuelve nada)                            (no necesita al robot)
          │
   ┌──────┴──────────────────────────┐
   ▼                                 ▼
comando_es_valido(comando)      ejecutar_comando(robot, comando)
 -> True / False                 -> (ejecutado, texto)
   │                             llama a avanzar / girar / detenerse /
   ▼                             saludar; atrapa ErrorDeSeguridad
motivo_de_rechazo(comando)
 -> texto del problema o None
   │
   ▼
es_numero(valor)
 -> True / False
```

## Contrato de cada función

| Función | Recibe | Devuelve | Responsabilidad (una sola) |
|---|---|---|---|
| `es_numero` | un valor | `bool` | ¿es un `int`/`float` finito? (no `bool`, no texto) |
| `motivo_de_rechazo` | un comando | `str` o `None` | encontrar el primer problema del comando |
| `comando_es_valido` | un comando | `bool` | decidir si se puede ejecutar |
| `ejecutar_comando` | robot, comando | `(bool, str)` | traducir el comando a una orden del robot y atrapar su rechazo |
| `ejecutar_mision` | robot, misión, historial | nada | recorrer la misión y registrar cada comando en el historial |
| `generar_reporte` | historial | nada (imprime) | resumir lo que pasó |
| `main` | — | — | conectar, correr las misiones y desconectar siempre (`finally`) |

## Datos

| Dato | Estructura | Ejemplo |
|---|---|---|
| Comando | tupla | `("avanzar", 0.2, 2.0)` · `("detenerse",)` |
| Misión | lista de tuplas | `[("avanzar", 0.2, 2.0), ("girar", -0.5, 3.14), ...]` |
| Historial | lista de diccionarios (crece en el bucle) | `{"numero": 3, "comando": (...), "ejecutado": False, "detalle": "0.9 m/s esta fuera del rango..."}` |
| Límites | constantes globales | `VELOCIDAD_MAX = 0.20`, `VELOCIDAD_GIRO_MAX = 0.50`, `TIEMPO_MAX = 10.0` |
| Comandos válidos | diccionario constante | `DATOS_POR_COMANDO = {"avanzar": 2, "girar": 2, "detenerse": 0, "saludar": 0}` |

## Flujo de un comando

```text
comando ──► ¿comando_es_valido? ──NO──► historial: rechazado + motivo ──► continue
                    │
                    SI
                    ▼
            ejecutar_comando ──► ¿el robot lo aceptó? ──NO──► detenerse + historial: rechazado
                                          │
                                          SI
                                          ▼
                                 historial: ejecutado + texto
```

Hay **dos filtros**: la validación propia (antes de mandar nada) y la del robot (`ErrorDeSeguridad`). Si algo pasa el primero por error, el segundo lo frena sin cortar la misión.
