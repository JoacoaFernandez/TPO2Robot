# 07 — Corrida final del programa reescrito

`corrida_completa_simulador.txt`: salida completa de `python3 mi_desarrollo/mi_tp02.py` contra el
simulador Go2 (`python3 -m sim --robot go2 --materia tp02`), con la versión final del código
(sin f-strings ni `str()`; `round()` solo en el reporte). Entorno: Python 3.14.4, MuJoCo 3.16.0.

Resultados (coinciden con lo calculado a mano):

| Misión | Recibidos | Ejecutados | Rechazados | Distancia | Girado | Duración |
|---|---|---|---|---|---|---|
| MISION_BASICA | 4 | 4 | 0 | 0.8 m | 90° | 7.14 s |
| MISION_CON_ERRORES | 11 | 4 | 7 | 0.4 m | 90° | 5.14 s |
| MISION_CUADRADO | 9 | 9 | 0 | 1.6 m | 360° | 20.56 s |
| MISION_PROPIA | 11 | 8 | 3 | 1.5 m | 360° | 20.07 s |

Las capturas de pantalla de `06_misiones/` (09b, 10 y 11) y de `05_gemelo_digital/` son de la
versión anterior del código. Los números del reporte son los mismos; solo cambia el formato de
algunos textos (por ejemplo `0.4 m` en vez de `0.40 m`).
