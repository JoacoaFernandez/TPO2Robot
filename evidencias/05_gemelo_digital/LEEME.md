# Evidencias — Gemelo digital (Go2 en MuJoCo)

| Archivo | Qué muestra |
|---|---|
| `01_arranque_simulador.log` | Primer arranque del simulador (02/10, 13:03): verificación `[OK]`, encabezado `Robot: Unitree Go2`, `Materia: tp02-programacion-i`, límites `0.2 m/s / 0.5 rad/s / 10 s`, aviso de Wayland (`libdecor-gtk.so`) y `[LOCAL] Escuchando en 127.0.0.1:8765`. Termina con `[SIM] Simulador cerrado.` |
| `02_ventana_go2_parado.png` | **Niveles 5 y 6.** Ventana de MuJoCo abierta con el Go2 visible, parado en la escena. En la terminal de atrás se ve todo el proceso: el primer intento rechazado con `YA HAY UN SIMULADOR ABIERTO (Proceso 227645)` (Problema 2) y el segundo intento, después de cerrar el anterior, que arranca bien hasta `Escuchando en 127.0.0.1:8765`. La ventana no tiene barra de título: es el efecto del aviso `libdecor` en Wayland. |
| `03_cuadrado_a_mitad_5de9.png` | `MISION_CUADRADO` en ejecución, lanzada desde una segunda terminal. La terminal muestra `[OK] Conectado a Unitree Go2` y los comandos 1 a 5 de 9 en `OK`; el Go2 está caminando a mitad del recorrido, ya girado respecto de su posición inicial. |
| `04_cuadrado_terminado_9de9.png` | `MISION_CUADRADO` terminada: 9/9 comandos `OK`, `=== Mision finalizada ===` y `[OK] Desconectado.` El Go2 quedó quieto, de vuelta en el punto de partida y con la misma orientación inicial. |
