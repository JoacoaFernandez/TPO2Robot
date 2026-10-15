# TPO2Robot

TP02 de Programación I (UADE): un controlador de misiones para el robot Unitree Go2, probado en el gemelo digital (MuJoCo).

## Contenido

| Ruta | Qué es |
|---|---|
| `codigo/tp02_fernandez_joaquin.py` | **El controlador (lo que se entrega).** Se ejecuta copiado como `mi_tp02.py` dentro de `mi_desarrollo/` del repo de la cátedra |
| `BITACORA.md` | Bitácora técnica: cada acción, su resultado y su estado |
| `PROBLEMAS.md` | Análisis detallado de cada problema encontrado |
| `CONCLUSIONES.md` | Reflexión final (preguntas a–g del Orientador) y nivel alcanzado |
| `INFORME.md` | Informe de una página: diseño Top-Down, valor vs. referencia, misión propia |
| `ESQUEMA_TOP_DOWN.md` | Esquema de funciones con sus entradas, salidas y responsabilidades |
| `evidencias/` | Salidas de terminal y capturas, por etapa |
| `UadeRobotLab/` | Repo de la cátedra (no versionado, ver abajo): simulador, `robot.py` y `misiones.py` |
| `.venv/` | Entorno virtual de Python con MuJoCo (no versionado) |

## Reproducir el entorno (Linux)

```bash
cd TPO2Robot
git clone https://github.com/tsamaan/UadeRobotLab.git
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install mujoco
cd UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/entorno
python3 -m sim --solo-revisar        # tiene que decir "Todo listo."
```

> Se usa un venv porque en esta PC pip exige un entorno virtual. Ver el Problema 1 en `PROBLEMAS.md`.

## Ejecutar

Terminal 1 (simulador; se cierra con Ctrl+C):
```bash
source .venv/bin/activate
cd UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/entorno
python3 -m sim --robot go2 --materia tp02      # o ../INICIAR_SIMULADOR.sh y elegir 2
```

Terminal 2 (programa: corre las 4 misiones y sus reportes). Primero se copia el controlador a la carpeta de trabajo de la cátedra, porque importa `robot.py` y `misiones.py` de ahí:
```bash
source .venv/bin/activate
cp codigo/tp02_fernandez_joaquin.py UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/mi_desarrollo/mi_tp02.py
python3 UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/mi_desarrollo/mi_tp02.py
```
