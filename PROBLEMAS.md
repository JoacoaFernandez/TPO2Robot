# Registro y análisis de problemas

Secuencia: ERROR → INTERPRETACIÓN → HIPÓTESIS → PRUEBA → RESULTADO

---

## Problema N.º 1 — pip se niega a instalar MuJoCo

**Qué se estaba intentando hacer:** instalar MuJoCo siguiendo el Paso 2 de `INSTALACION.md`.

**Comando ejecutado:**
```bash
python3 -m pip install --user mujoco
```

**Resultado esperado:** que pip descargara e instalara MuJoCo en el directorio del usuario.

**Resultado obtenido:** pip terminó sin instalar nada (código de salida 3).

**Mensaje de error:**
```text
ERROR: Could not find an activated virtualenv (required).
```

**Interpretación del grupo:**
pip no rechaza el paquete en sí: se niega a instalar cualquier cosa porque no hay un entorno virtual activado. El mensaje dice "(required)", o sea que algo en la configuración lo exige.

**Hipótesis sobre la causa:**
1. *(Hipótesis inicial)* El bloqueo de PEP 668 de Ubuntu, porque el Python del sistema está marcado como `EXTERNALLY-MANAGED`. Pero ese caso da otro mensaje (`error: externally-managed-environment`), así que no coincide.
2. *(Hipótesis 2)* Hay una opción de pip, `require-virtualenv`, activada por variable de entorno (`PIP_REQUIRE_VIRTUALENV`) o en un archivo `pip.conf`.

**Prueba de diagnóstico:**
```bash
env | grep -i pip            # → vacío: no es una variable de entorno
python3 -m pip config list -v
# → global.require-virtualenv='true'
cat ~/.config/pip/pip.conf
# → [global]
#   require-virtualenv = true
```
Se confirma la hipótesis 2: la configuración de pip del usuario exige un venv. Aunque se desactivara esa opción, el bloqueo de PEP 668 seguiría estando, así que instalar en el Python del sistema no es buena idea de ninguna forma.

**Solución 1 descartada:** forzar la instalación con `--break-system-packages` o borrar `pip.conf`. Se descartó porque:
- ese `pip.conf` es una protección configurada a propósito;
- mezclar paquetes de pip con los de `apt` en el Python del sistema puede romper herramientas de Ubuntu.

**Solución 2 intentada y resultado:** crear un entorno virtual **dentro de la carpeta del TP** e instalar MuJoCo ahí.
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install mujoco      # ya no hace falta --user dentro del venv
python3 -c "import mujoco; print(mujoco.__version__)"
# → 3.14.0
```
**Por qué funciona:** el venv tiene su propio Python y su propio `site-packages`, separados del sistema. Con eso se cumple `require-virtualenv` y no choca con PEP 668. Además, los lanzadores (`INICIAR_SIMULADOR.sh`, `EJECUTAR_MI_CODIGO.sh`) buscan `python3` en el PATH: con el venv activado encuentran el del venv, que tiene MuJoCo. (Si no, los scripts también prueban `~/.venvs/unitree/bin/python`, pero se eligió dejar todo dentro de la carpeta del TP.)

**Estado final:** ✅ Resuelto.

**Evidencia:**
- `evidencias/03_errores/01_pip_require_virtualenv.txt` — el error original
- `evidencias/03_errores/02_diagnostico_pip.txt` — el diagnóstico de la configuración de pip
- `evidencias/04_soluciones/01_venv_mujoco.txt` — la instalación en el venv y la verificación
- `evidencias/02_instalacion/02_verificacion_entorno.txt` — `--solo-revisar` con todo en `[OK]`

**Consecuencia práctica:** antes de abrir el simulador o correr el programa, siempre hay que activar el venv:
```bash
cd ~/Escritorio/allProject/UADE/TPO2Robot
source .venv/bin/activate
```

---

## Problema N.º 2 — "YA HAY UN SIMULADOR ABIERTO"

**Qué se estaba intentando hacer:** abrir el simulador desde una terminal propia para sacar las capturas de la ventana (niveles 5 y 6).

**Comando ejecutado:**
```bash
python3 -m sim --robot go2 --materia tp02
```

**Resultado esperado:** que se abriera la ventana de MuJoCo con el Go2.

**Resultado obtenido:** la verificación dio todo `[OK]`, pero el simulador no abrió.

**Mensaje de error:**
```text
YA HAY UN SIMULADOR ABIERTO
  Robot   : go2
  Materia : tp02
  Proceso : 227645
Los dos escuchan en el mismo puerto, asi que el segundo no
podria abrir, o peor: tu programa terminaria hablandole al
OTRO robot sin ningun error que te avise.
```

**Interpretación del grupo:**
No es un error de instalación: es una protección del simulador. Cada simulador escucha en `127.0.0.1:8765` y deja anotado su número de proceso (PID) en `/tmp/uade_simulador_activo.json`. El segundo lee ese archivo, ve que el proceso 227645 sigue vivo y se niega a arrancar.

**Hipótesis sobre la causa:**
Quedaba abierto un simulador lanzado antes en otra terminal (en segundo plano), el que se había usado para correr las misiones (acciones 19 a 22 de la bitácora). Su ventana abre sin barra de título por Wayland (ver acción 19), así que es fácil no darse cuenta de que está abierta.

**Prueba:**
```bash
ps -p 227645 -o pid,cmd
# → 227645 python3 -u -m sim --robot go2 --materia tp02
```
Se confirma: el proceso existe y es un simulador Go2/tp02.

**Solución 1 descartada:** agregar `--igualmente`. El propio mensaje advierte que el programa podría terminar hablándole al otro robot sin avisar, y los dos competirían por el puerto 8765.

**Solución 2 intentada y resultado:** cerrar el simulador anterior con `kill -INT 227645`. Equivale a apretar Ctrl+C en su terminal: le da tiempo a cerrarse ordenadamente y borrar su archivo de "activo". Resultado: `[SIM] Simulador cerrado.`, no queda ningún proceso `sim` y `/tmp/uade_simulador_activo.json` ya no existe.

**Estado final:** ✅ Resuelto.

**Evidencia:**
- `evidencias/03_errores/03_simulador_ya_abierto.txt` — el mensaje
- `evidencias/04_soluciones/02_cerrar_simulador_previo.txt` — el diagnóstico y el cierre

**Aprendizaje:** antes de abrir el simulador, revisar que no haya otro (`pgrep -af "python.*-m sim"`) y cerrarlo con Ctrl+C, no cerrando la terminal a lo bruto. Si se mata de golpe, puede quedar el archivo de "activo" huérfano (el caso que menciona `INSTALACION.md`).
