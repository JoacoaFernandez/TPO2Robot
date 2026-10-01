# TPO2Robot

TP02 de Programación I (UADE): un controlador de misiones para el robot Unitree Go2, probado en el gemelo digital (MuJoCo).

## Contenido

| Ruta | Qué es |
|---|---|
| `BITACORA.md` | Bitácora técnica: cada acción, su resultado y su estado |
| `PROBLEMAS.md` | Análisis detallado de cada problema encontrado |
| `CONCLUSIONES.md` | Reflexión final y nivel alcanzado |
| `codigo/` | Código fuente del controlador (`tp02_apellido.py`) |
| `evidencias/` | Salidas de terminal y capturas, por etapa |
| `enunciado/` | Consigna del TP y Orientador, pasados a Markdown |
| `UadeRobotLab/` | Repo de la cátedra (no versionado, ver abajo) |
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

Terminal 1 (simulador):
```bash
source .venv/bin/activate
./UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/INICIAR_SIMULADOR.sh   # elegir 2 - Go2
```

Terminal 2 (programa):
```bash
source .venv/bin/activate
python3 UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/mi_desarrollo/mi_tp02.py
```
