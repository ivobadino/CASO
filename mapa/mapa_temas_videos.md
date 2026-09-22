# Mapa de temas vistos en los videos

> Estado: mapa parcial, basado solamente en videos/transcripciones procesadas localmente.
>
> Regla de uso: no completar silenciosamente con conocimiento general ni con PDFs. Los PDFs se relacionan solo cuando la clase/transcripcion los menciona o cuando ya este verificado el tema en video.
>
> Contexto general de la boveda y Drive historico: contexto_fuentes_caso.

## Fuente

- Carpeta principal de Drive: https://drive.google.com/drive/folders/1TbRK7ge4KKXi8W-F7y2znHhnQw3gbF0K
- Subcarpeta `TP`: https://drive.google.com/drive/folders/1mQ9YmKwZchPf8BmcmyJhCQlkDZQ9hwZg
- Clase 24: enlace en `24.txt`: https://www.youtube.com/watch?v=RaeHF1l6oCo&list=WL&index=38&t=8414s

## Estado de procesamiento

| Clase | Archivo | Estado | Evidencia local |
|---:|---|---|---|
| 1 | `1 250320.mp4` | Transcripta | `transcripciones/clase01.txt` |
| 2 | `2 300320.mp4` | Transcripta | `transcripciones/clase02.txt` |
| 3 | `3 010420.mp4` | Transcripta | `transcripciones/clase03.txt` |
| 4 | `4 060420 - semaforos.mp4` | Transcripta | `transcripciones/clase04.txt` |
| 5 | `5 080420.mp4` | Transcripta | `transcripciones/clase05.txt` |
| 6 | `6 130420.mp4` | Transcripta | `transcripciones/clase06.txt` |
| 7 | `7 150420.mp4` | Transcripta | `transcripciones/clase07.txt` |
| 8 | `8 200420.mp4` | Transcripta | `transcripciones/clase08.txt` |
| 9 | `9 220420.mp4` | Transcripcion parcial/interrumpida | `transcripciones/clase09.txt` |
| 10 | `10 240420.mp4` | Pendiente | Drive |
| 11 | `11 270420.mp4` | Pendiente | Drive |
| 12 | `12 290420 PT1.mp4` | Pendiente | Drive |
| 13 | `13 290420 PT2.mp4` | Pendiente | Drive |
| 14 | `14 040520.mp4` | Pendiente | Drive |
| 15 | `15 060520.mp4` | Pendiente | Drive |
| 16 | `16 130520.mp4` | Pendiente | Drive |
| 17 | `17 180520.mp4` | Pendiente | Drive / TP |
| 18 | `18 200520.mp4` | Pendiente | Drive |
| 19 | `19 270520.mp4` | Pendiente | Drive |
| 20 | `20 010620.mp4` | Pendiente | Drive / TP |
| 21 | `21 030620.mp4` | Pendiente | Drive |
| 22 | `22 080620.mp4` | Pendiente | Drive |
| 23 | `23 170620.mp4` | Pendiente | Drive / TP |
| 24 | `24.txt` | Pendiente, requiere tratar como YouTube | Drive / TP |
| 25 | `25 030720.mp4` | Pendiente | Drive / TP |
| 26 | `26 060720.mp4` | Pendiente | Drive / TP |
| 27 | `27 080720.mp4` | Transcripta | `transcripciones/clase27.txt` |

## Mapa verificado por ahora

### Introduccion a Sistemas Operativos

Verificado en clase 1.

- Objetivo del sistema operativo como interfaz entre usuario y maquina.
  - Timestamp aproximado: 00:03:02-00:03:44.
  - El profesor remarca que el usuario no debe tocar directamente el hardware.
- Sistema operativo como administrador de recursos.
  - Timestamp aproximado: 00:03:24-00:03:44.
  - Recursos mencionados: perifericos, memoria y microprocesador.
- Evolucion de los sistemas operativos.
  - Timestamp aproximado: 00:03:44-00:11:01.
  - Temas mencionados: operador humano/programacion directa, monitor simple, cola de trabajos, instrucciones privilegiadas, modo usuario y modo supervisor/root.
- Proteccion por privilegios/anillos.
  - Timestamp aproximado: 00:08:45-00:10:32.
  - Se usa para explicar por que los programas de usuario no pueden acceder libremente al hardware.
- Multiprogramacion.
  - Timestamp aproximado: 00:11:18-00:15:00.
  - Se explica como aprovechamiento de CPU mientras otros procesos esperan entrada/salida.
- Time sharing / multipusuario.
  - Timestamp aproximado: 00:13:39-00:16:07.
  - Se presenta como reparto del tiempo de CPU entre muchos procesos/usuarios.
- Sistemas de tiempo real.
  - Timestamp aproximado: 00:16:47-00:18:06.
  - Se explica con metas temporales y ejemplo de reproduccion de audio.
- Multiprocesamiento.
  - Timestamp aproximado: 00:18:21-00:18:47.
  - Se conecta con la parte previa de arquitecturas y varias CPU interconectadas.

### Servicios y estructura del Sistema Operativo

Verificado en clase 1.

- Servicios que se van a estudiar en la materia.
  - Timestamp aproximado: 00:18:54-00:21:05.
  - Administracion de procesos, memoria, entrada/salida, sistema de archivos, accounting/metricas, planificacion y proteccion.
- Nucleo/kernel.
  - Timestamp aproximado: 00:26:21-00:30:08.
  - Diferencia entre sistema operativo completo y kernel como parte interna que brinda funcionalidad.
- Capas e interfaces.
  - Timestamp aproximado: 00:24:07-00:25:00 y 00:30:14-00:34:16.
  - El profesor ubica hardware, administracion de procesador, memoria, perifericos, sistema de archivos y capas superiores.
- Kernel monolitico, microkernel e hibrido.
  - Timestamp aproximado: 00:30:45-00:38:53.
  - Se compara modularidad, interfaces, mensajes entre modulos y llamadas directas.
- Ejemplos mencionados.
  - DOS, Linux, Windows, Android, Minix/Phoenix segun la transcripcion automatica.
  - Nota: algunos nombres pueden requerir verificacion visual/manual porque la transcripcion tiene errores.

### Puente hacia Administracion del Procesador

Verificado en clases 1, 2, 3, 4 y 5.

- Orden de cursada anunciado.
  - Timestamp aproximado: 00:41:05-00:41:24.
  - Primero administracion de procesador y semaforos; despues memoria; despues perifericos; despues file system; tambien planificador de trabajos.
- Concepto de proceso.
  - Timestamp aproximado: 01:06:05-01:10:09.
  - Un proceso se presenta como programa almacenado en disco que se carga en memoria.
- Bloque de Control de Proceso.
  - Timestamp aproximado: 01:06:48-01:07:30.
  - Se menciona una tabla de BCP/PCB como condicion para que el proceso exista dentro del SO.
- Estados iniciales de proceso.
  - Timestamp aproximado: 01:08:09-01:14:47.
  - Se trabaja la alternancia entre uso de CPU y espera por entrada/salida.
  - Estados mencionados: ejecutando, espera/bloqueado, listo, comenzar, terminado.
- Proceso como ejecucion de un programa.
  - Clase 2, timestamp aproximado: 00:27:15-00:29:20.
  - Se asocian memoria, codigo, recursos y archivos al proceso.
- Multiprogramacion, paralelismo y simultaneidad.
  - Clase 2, timestamp aproximado: 00:22:28-00:26:30.
  - Se distingue ejecucion en paralelo de ejecucion simultanea en varios procesadores.
- Planificacion y colas de listos.
  - Clase 2, timestamp aproximado: 01:40:00-fin.
  - Se trabajan FIFO/FCFS, quantum, Round Robin, mas corto primero, turnaround y comparacion de ordenes de ejecucion.
- Transiciones de estados e interrupciones.
  - Clase 3, timestamp aproximado: 00:00:00-00:23:00 y 01:46:00-fin.
  - Se resuelven ejercicios con procesos, listo, ejecutando, bloqueado, entrada/salida, cinta/disco, interrupciones y rutina de atencion.
- Idle/hidle.
  - Clase 3, timestamp aproximado: 01:51:40-fin.
  - Se menciona como ciclo infinito usado para cubrir huecos y contabilizar tiempo ocioso.
- Multicolas y prioridades.
  - Clase 4, timestamp aproximado: 00:09:30-00:17:20.
  - Se diferencian listos interactivos, listos medios y listos de baja prioridad; se priorizan procesos interactivos bloqueados por consola.

### Semaforos y sincronizacion

Verificado en clases 3, 4, 5 y 8.

- Introduccion al problema de semaforos.
  - Clase 3, timestamp aproximado: 00:56:00-fin.
  - Se vincula con cambios concurrentes sobre estructuras como la tabla de bloque de control de procesos.
- Ejercicios de semaforos.
  - Clase 4 y clase 5.
  - Se trabajan resoluciones en pizarra/RG; la clase 4 no usa PPT.
- Productor/consumidor y secuencias.
  - Clase 5, timestamp aproximado: 00:00:00-00:16:00.
  - Se menciona un patron productor/consumidor y restricciones de secuencia entre procesos A y V/B.
- Zona critica y exclusion.
  - Clase 5, timestamp aproximado: 00:14:00-00:25:00.
  - Se agregan semaforos para proteger zonas donde no deben entrar procesos simultaneamente.
- Operaciones P/V y atomicidad.
  - Clase 5, timestamp aproximado: 00:24:00-00:38:00.
  - Se explica que la funcion P sobre el semaforo debe ser atomica.
- Limites de los semaforos para ciertas secuencias.
  - Clase 8, timestamp aproximado: 00:33:00-00:42:00.
  - Se menciona que algunas secuencias no pueden resolverse exactamente solo con semaforos y aparece la idea de memoria compartida/variables intermedias.

### Administracion de Memoria

Verificado en clases 6, 7 y 8.

- Inicio de administracion de memoria.
  - Clase 6, timestamp aproximado: 00:15:35.
  - Se introduce la diferencia entre memoria real y memoria que conoce el proceso.
- Carga de programas en memoria.
  - Clase 6, timestamp aproximado: 00:19:45-00:21:20.
  - Se relaciona el punto de entrada del programa con los registros del BCP.
- Registro base y reubicacion.
  - Clase 6, timestamp aproximado: 00:23:00-00:31:00.
  - Se explica sumar registro base a direcciones del proceso cuando ejecuta dentro de una particion.
- Particiones.
  - Clase 6, timestamp aproximado: 00:28:00-00:36:00.
  - Se trabaja dividir memoria en espacios para procesos y los limites de tamanos fijos.
- Paginacion, TDP/TDB y falla de pagina.
  - Clase 6, timestamp aproximado: 01:18:00-01:32:00.
  - Se menciona cargar paginas, actualizar tablas y pasar procesos de bloqueado a listo cuando se resuelve una falla de pagina.
- Trazas y algoritmos de remocion.
  - Clase 7, timestamp aproximado: 00:57:00-01:05:00.
  - Se usan trazas de paginas para evaluar que paginas suben/bajan y se menciona FIFO como algoritmo de remocion.
- Memoria compartida y paginas compartidas.
  - Clase 8, timestamp aproximado: 00:57:00-01:03:00.
  - Se analiza compartir memoria/codigo entre procesos y el problema de las direcciones internas.

### Administracion de Archivos / File System

Verificado en clase 8.

- Paso desde memoria hacia archivos.
  - Clase 8, timestamp aproximado: 01:35:00.
  - El profesor comienza a trabajar la estructura que ve el sistema operativo.
- Vista del usuario: carpetas/directorios y archivos.
  - Clase 8, timestamp aproximado: 01:39:00-01:44:00.
  - Se remarca que a nivel usuario se ven carpetas y archivos.
- Vista interna del sistema operativo.
  - Clase 8, timestamp aproximado: 01:40:30-01:52:00.
  - Se explica que para el sistema operativo una carpeta tambien es un archivo, y que internamente aparecen entradas, nombres, bloques y contenido.
- Asignacion por bloques.
  - Clase 8, timestamp aproximado: 01:51:00-01:58:00.
  - Se trabaja la idea de sucesion de bloques, bloque logico/fisico, lista de bloques vacios y bloques asociados a un archivo.
- Formateo de periferico.
  - Clase 8, timestamp aproximado: 01:56:20-01:58:30.
  - Se menciona formatear el periferico para preparar la estructura de bloques/listas.

### Trabajo Practico / Virtualizacion / Linux

Verificado en clases 2, 6, 7, 8 y 27.

- VirtualBox, VMware y maquinas virtuales.
  - Clase 2, timestamp aproximado: 00:04:10-00:11:30.
  - Se explica por que usar maquina virtual para el TP: el disco virtual queda como archivo de la maquina host.
- Simulacion vs virtualizacion.
  - Clase 6, timestamp aproximado: 00:01:30-00:08:00.
  - Se comenta el uso de virtualizacion por hardware y se contrasta con simuladores completos de arquitectura.
- Instalacion/particionado de Ubuntu/Linux.
  - Clase 7, timestamp aproximado: 00:20:00-00:53:00.
  - Se mencionan particiones, disco, home, swap, boot record y preservacion de archivos de usuario.
- Comandos basicos de Linux para archivos.
  - Clase 8, timestamp aproximado: 02:10:00-fin.
  - Se mencionan comandos como editar/crear archivos, `cat` y `rm`.

### Trabajo Practico / Linux / systemd

Verificado en clase 27.

- Cierre y correccion del tema de shutdown.
  - Timestamp aproximado: 00:03:22-00:04:44.
  - Se explica que Ubuntu 16.04, 18.04 y 20.04 usan `systemd`; se contrasta con versiones anteriores.
- Archivos/scripts del TP.
  - Timestamp aproximado: 00:07:03-00:11:32.
  - Se organizan archivos del campus y se mencionan scripts/archivos para el trabajo practico.
- Archivos secuenciales en `/proc`.
  - Timestamp aproximado: 00:10:18-00:11:24.
  - Se menciona el kernel de Linux trabajando con archivos secuenciales creados en `/proc`.
- Servicios `systemd`.
  - Timestamp aproximado: 00:11:52-00:21:02.
  - Se explica crear un archivo ejecutable, definir un archivo `.service`, usar `ExecStart` y `ExecStop`, habilitar el servicio y relacionarlo con `multi-user.target`.
- Reemplazo conceptual de `init`/niveles por targets.
  - Timestamp aproximado: 00:17:07-00:23:50.
  - Se compara el esquema anterior de `init`/`rc3.d` con `systemd` y targets.
- Entrega del TP y modalidad de final.
  - Timestamp aproximado: 00:24:24-fin.
  - Se indican condiciones de entrega del trabajo practico y modalidad de evaluacion final.

## Indice invertido verificado

| Tema | Clase | Timestamp aproximado | Material relacionado |
|---|---:|---|---|
| Objetivo del SO | 1 | 00:03:02-00:03:44 | Cap. 11 mencionado |
| SO como administrador de recursos | 1 | 00:03:24-00:03:44 | Cap. 11 mencionado |
| Monitor simple | 1 | 00:07:56-00:08:45 | Cap. 11 mencionado |
| Instrucciones privilegiadas | 1 | 00:08:45-00:10:32 | Cap. 11 mencionado |
| Multiprogramacion | 1 | 00:11:18-00:15:00 | Cap. 11 mencionado |
| Time sharing / multipusuario | 1 | 00:13:39-00:16:07 | Cap. 11 mencionado |
| Sistemas de tiempo real | 1 | 00:16:47-00:18:06 | Cap. 11 mencionado |
| Multiprocesamiento | 1 | 00:18:21-00:18:47 | Arquitecturas previas mencionadas |
| Kernel | 1 | 00:26:21-00:30:08 | Cap. 11 mencionado |
| Microkernel / monolitico / hibrido | 1 | 00:30:45-00:38:53 | Cap. 11 mencionado |
| Proceso | 1 | 01:06:05-01:10:09 | Cap. 12 mencionado |
| BCP / PCB | 1 | 01:06:48-01:07:30 | Cap. 12 mencionado |
| Estados de proceso | 1 | 01:08:09-01:14:47 | Cap. 12 mencionado |
| Proceso como ejecucion de un programa | 2 | 00:27:15-00:29:20 | Administracion del procesador |
| Multiprogramacion/paralelismo/simultaneidad | 2 | 00:22:28-00:26:30 | Administracion del procesador |
| FIFO/FCFS con quantum | 2 | 01:40:00-01:43:00 | Administracion del procesador |
| Round Robin | 2, 3 | Clase 2 01:40:00-01:43:00; clase 3 00:03:20-00:04:00 | Administracion del procesador |
| Mas corto primero / turnaround | 2 | 01:41:00-fin | Administracion del procesador |
| Transiciones de estados | 3, 4 | Clase 3 inicio y cierre; clase 4 00:08:00-00:17:20 | Administracion del procesador |
| Multicolas/prioridades | 4 | 00:09:30-00:17:20 | Administracion del procesador |
| Semaforos | 3, 4, 5, 8 | Varios tramos | Administracion del procesador / sincronizacion |
| Productor/consumidor | 5 | 00:01:30-00:06:00 | Semaforos |
| Zona critica/exclusion | 5 | 00:14:00-00:25:00 | Semaforos |
| Atomicidad de P/V | 5 | 00:24:00-00:38:00 | Semaforos |
| Administracion de memoria | 6, 7, 8 | Varios tramos | Capitulo de memoria mencionado |
| Particiones de memoria | 6 | 00:28:00-00:36:00 | Administracion de memoria |
| Paginacion | 6, 7, 8 | Varios tramos | Administracion de memoria |
| Falla de pagina | 6 | 01:18:00-01:32:00 | Administracion de memoria |
| TDP/TDB | 6 | 01:18:00-01:32:00 | Administracion de memoria |
| Trazas de paginas | 7 | 00:57:00-01:05:00 | Administracion de memoria |
| Memoria compartida | 8 | 00:57:00-01:03:00 | Administracion de memoria |
| Maquinas virtuales / VirtualBox | 2, 6, 7 | Varios tramos | TP |
| Instalacion Linux/Ubuntu | 7 | 00:20:00-00:53:00 | TP |
| Sistema de archivos | 8 | 01:35:00-fin | Administracion de archivos |
| systemd | 27 | 00:03:42-00:24:49 | TP |
| `multi-user.target` | 27 | 00:17:27-00:21:02 | TP |
| `ExecStart` / `ExecStop` | 27 | 00:14:47-00:23:50 | TP |
| archivos en `/proc` | 27 | 00:10:18-00:11:24 | TP |

## Pendiente para completar el mapa real

- Transcribir y auditar clases 10 a 23, 25 y 26.
- Revisar manualmente clase 9, porque quedo solo una transcripcion parcial.
- Tratar clase 24 aparte porque el Drive solo contiene un enlace de YouTube.
- Revisar visualmente frames cuando la transcripcion mencione pizarron, RG, diapositivas o comandos.
- Rehacer el mapa conceptual final solo con temas confirmados en las clases.

## Notas tecnicas

- Se instalo `ffmpeg-static` para inspeccionar y procesar video local.
- Se instalo `faster-whisper` y se uso el modelo `tiny` en CPU.
- La clase 9 quedo parcial porque se interrumpio el pipeline mientras estaba procesando esa clase. El script fue ajustado para guardar segmentos incrementalmente en futuras corridas.
