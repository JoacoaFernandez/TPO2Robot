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
