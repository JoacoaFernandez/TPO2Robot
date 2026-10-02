# Conclusiones — TP02 Programación I (Robot Unitree Go2)

**Joaquín Fernández** · Programación I · turno noche, jueves

## Nivel alcanzado: 10 / 10

| Nivel | Evidencia |
|---|---|
| 1–4 | `evidencias/01_entorno/`, `02_instalacion/02_verificacion_entorno.txt` (`Todo listo.`) |
| 5–6 | `evidencias/05_gemelo_digital/02_ventana_go2_parado.png` |
| 7–8 | `evidencias/06_misiones/04_mision_basica_simulador.txt` |
| 9 | `evidencias/06_misiones/06_mision_con_errores_simulador.txt` |
| 10 | `evidencias/06_misiones/10_reporte_mision_con_errores.png`, `11_reporte_mision_propia.png` |

## Respuestas de cierre

**a) ¿Cuál fue la principal dificultad de instalación?**
Instalar MuJoCo. El comando de la guía (`python3 -m pip install --user mujoco`) falló con `Could not find an activated virtualenv (required)`. Mi configuración de pip exige un entorno virtual, y además el Python de Ubuntu 26.04 está marcado como `EXTERNALLY-MANAGED` (PEP 668). (Problema 1)

**b) ¿Qué error requirió mayor investigación?**
Ese mismo. Mi primera hipótesis fue el bloqueo de PEP 668, pero el mensaje no coincidía: ese caso dice `externally-managed-environment`. Tuve que buscar de dónde salía la exigencia. Descarté una variable de entorno (`env | grep -i pip` vacío) y encontré la causa con `pip config list -v`: `require-virtualenv = true` en `~/.config/pip/pip.conf`.

**c) ¿Qué solución resultó efectiva y por qué?**
Crear un entorno virtual dentro de la carpeta del TP (`python3 -m venv .venv`) e instalar MuJoCo ahí. Funciona porque el venv tiene su propio Python y sus propios paquetes, separados del sistema. Así cumple la exigencia de pip, no choca con PEP 668 y no arriesga romper herramientas de Ubuntu. Los lanzadores de la cátedra buscan `python3` en el PATH, así que con el venv activado encuentran el que tiene MuJoCo.

**d) ¿Qué intento no funcionó y qué aprendí de él?**
- El comando de la guía tal cual no funcionó en mi máquina. Aprendí a no asumir la causa por el tipo de error que "suele" ser, sino a leer el mensaje exacto y verificar la hipótesis antes de cambiar nada. También descarté atajos como `--break-system-packages` o borrar `pip.conf`: "resuelven" el error rompiendo una protección.
- Al intentar abrir el simulador por segunda vez apareció `YA HAY UN SIMULADOR ABIERTO` (Problema 2): quedaba uno abierto de antes. La ventana abre sin barra de título por Wayland, así que no era evidente. No usé `--igualmente`, porque el propio mensaje advierte que el programa podría hablarle al robot equivocado. Cerré el anterior con Ctrl+C (`kill -INT`). Aprendí a cerrar el simulador siempre con Ctrl+C y a revisar con `pgrep` si hay otro corriendo.

**e) ¿Qué diferencia encontré entre la guía antigua y la arquitectura actual?**
El PDF del TP usa `unitree_sdk_sim.py` con `avanzar(distancia, velocidad)` y `girar(grados, "izquierda"/"derecha")`, límites de 0.5 m/s y 180°, y comandos como `"saludo"`. Las guías anteriores pedían además CycloneDDS y el SDK oficial de Unitree. La versión actual:
- se comunica con el simulador por un **socket local** (`127.0.0.1:8765`) a través de `robot.py`, que no se modifica;
- expresa todo como **velocidad × tiempo**, y en `girar` el **signo** indica el sentido (+ izquierda, − derecha);
- usa límites más bajos: 0.20 m/s, 0.50 rad/s y 10 s por orden;
- **rechaza** con `ErrorDeSeguridad` en vez de recortar en silencio.

Según el Orientador, prevalece el repositorio, y así lo implementé.

**f) ¿Hasta qué nivel logré avanzar?**
Nivel 10. Las tres misiones de la cátedra y una propia corrieron contra el gemelo digital, con reporte final. `MISION_CON_ERRORES` rechazó los 7 comandos inválidos con su motivo, sin abortar.

**g) Si tuviera que continuar, ¿cuál sería el próximo paso?**
- **Probar en el Go2 real** (Extensión 5), con supervisión. El simulador no patina ni tiene inercia: en el cuadrado ya se ve ~1° de desvío acumulado en el rumbo (−90.3° → −89.3°), y en el robot real ese error sería mayor. Habría que comparar la posición real con la calculada.
- **Leer misiones desde un archivo JSON** (Extensión 1), para cambiar la misión sin tocar el código.
- **Analizar la misión antes de ejecutarla** (Extensión 4): mostrar distancia y tiempo estimados y avisar los comandos inválidos antes de mover el robot.

## Observaciones técnicas

- La validación del robot es más permisiva que la que pide el TP: acepta `"0.2"` como número y velocidades negativas en `avanzar`. Por eso la validación propia no confía en el robot.
- Las posiciones informadas por el simulador coincidieron con las calculadas: la misión básica terminó en `x=+0.40 y=-0.40 rumbo=-90°`, y el cuadrado volvió al punto de partida.
- Para probar sin el simulador construí un robot falso (`codigo/pruebas/robot_falso.py`) que usa los mismos validadores de `safety.py`. Permitió verificar las partes 2 a 4 antes de tener el gemelo digital andando.
