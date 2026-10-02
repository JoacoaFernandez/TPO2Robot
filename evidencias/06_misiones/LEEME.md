# Evidencias — Misiones

## Pruebas sin simulador (robot falso)

| Archivo | Qué muestra |
|---|---|
| `01_prueba_parte1_validacion.txt` | Parte 1 sola: 25 casos (MISION_BASICA, MISION_CON_ERRORES y casos borde), todos con el resultado esperado |
| `02_prueba_parte2_robot_falso.txt` | Parte 2: ejecución de comandos y captura de `ErrorDeSeguridad` / `NotImplementedError` |
| `03_prueba_parte3_robot_falso.txt` | Parte 3: las 3 misiones de la cátedra y el historial completo de MISION_CON_ERRORES |
| `07_prueba_parte4_reporte_robot_falso.txt` | Parte 4: reportes comparados contra valores calculados a mano |

## Contra el simulador Go2

| Archivo | Qué muestra |
|---|---|
| `04_mision_basica_simulador.txt` | MISION_BASICA (partes 1-3) + posición final `x=+0.40 y=-0.40 rumbo=-90°` |
| `05_mision_cuadrado_simulador.txt` | MISION_CUADRADO: el robot vuelve al punto de partida |
| `06_mision_con_errores_simulador.txt` | MISION_CON_ERRORES: 4 ejecutados / 7 rechazados, sin abortar |
| `08_main_basica_con_reporte_simulador.txt` | Primer reporte generado contra el simulador (nivel 10) |
| `09_programa_completo_simulador.txt` | Programa final completo: las 4 misiones con sus reportes |
| `09b_corrida_completa_inicio.png` | Captura del programa final en curso: reporte de MISION_BASICA (4/4, 0.8 m, 90°, 7.14 s) y MISION_CON_ERRORES ejecutándose (comandos 3 a 9 RECHAZADOS), con el Go2 en la ventana de MuJoCo |
| `10_reporte_mision_con_errores.png` | **Reporte de la misión de la cátedra (MISION_CON_ERRORES):** 11 recibidos, 4 ejecutados, 7 rechazados, 0.4 m, 90°, 5.14 s, y el motivo de cada uno de los 7 rechazos. Debajo, MISION_CUADRADO completa (9/9, 1.6 m, 360°) y el inicio de MISION_PROPIA con el Go2 girando 120° |
| `11_reporte_mision_propia.png` | **Reporte de la misión propia (MISION_PROPIA, triángulo):** comandos 1-11 con los 3 rechazos (giro de 12.6 s, avance a 0.25 m/s, `'Saludar'` con mayúscula), reporte de 11 recibidos, 8 ejecutados, 3 rechazados, 1.5 m, 360°, 20.07 s, y `[OK] Desconectado.` El Go2 terminó el triángulo y saludó |
