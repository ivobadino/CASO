# Mapa definitivo de temas por parcial

> Fuente base: [[contexto_fuentes_caso]] y [[mapa_temas_videos]].
>
> Criterio: este mapa consolida lo que aparece repetidamente en videos transcritos, practicas locales, PDFs/presentaciones y carpetas historicas de parciales del Drive. Cuando un tema aparece en algunos anios dentro de otro parcial, queda marcado como zona de solapamiento.
>
> Regla de estudio: para explicar o desarrollar cualquier punto, usar primero fuentes de la boveda/Drive. Web solo con aprobacion previa.

## Primer Parcial

### 1. Introduccion a Sistemas Operativos

Entra como marco teorico inicial y como base para entender por que existen las administraciones del sistema operativo.

- Sistema operativo como interfaz entre usuario y hardware.
- Sistema operativo como administrador de recursos.
- Recursos administrados: procesador, memoria, perifericos, archivos.
- Evolucion historica:
  - operador humano / programacion directa;
  - monitor simple;
  - procesamiento por lotes;
  - multiprogramacion;
  - tiempo compartido / multiusuario;
  - sistemas de tiempo real;
  - multiprocesamiento.
- Modo usuario y modo supervisor/root.
- Instrucciones privilegiadas.
- Proteccion por privilegios/anillos.
- Servicios del sistema operativo.
- Kernel/nucleo.
- Estructuras de sistema operativo:
  - kernel monolitico;
  - microkernel;
  - kernel hibrido;
  - capas e interfaces.

Fuentes principales:

- `transcripciones/clase01.txt`
- `mapa/mapa_temas_videos.md`
- `pdfs/sitemas operativos/Cap11.pdf`
- Presentacion local `pdfs/presentaciones/intro SO.pdf`

### 2. Administracion del Procesador

Es nucleo fuerte del primer parcial.

- Concepto de proceso.
- Programa vs proceso.
- Carga de un programa en memoria.
- Recursos asociados a un proceso.
- Bloque de Control de Proceso:
  - BCP / PCB;
  - informacion del proceso;
  - registros;
  - estado;
  - recursos asociados.
- Estados de proceso:
  - comenzar / nuevo;
  - listo;
  - ejecutando;
  - bloqueado / espera;
  - terminado.
- Diagrama de transicion de estados.
- Eventos que provocan transiciones.
- Interrupciones y rutinas de atencion.
- Planificador de procesos.
- Cola de listos.
- Colas de bloqueados por recurso.
- Cambio de contexto.
- Idle / proceso ocioso.
- Multiprogramacion.
- Simultaneidad y paralelismo.
- Administraciones de procesador:
  - FIFO / FCFS;
  - Round Robin;
  - quantum;
  - mas corto primero;
  - comparacion por turnaround;
  - multicolas;
  - prioridades;
  - procesos interactivos vs batch.
- Ejercicios de cronograma:
  - CPU;
  - E/S;
  - disco/cinta;
  - interrupciones;
  - tiempos de rutinas del SO;
  - seleccion de procesos.

Fuentes principales:

- `transcripciones/clase01.txt`
- `transcripciones/clase02.txt`
- `transcripciones/clase03.txt`
- `transcripciones/clase04.txt`
- `pdfs/practicas/Practicas-2-U.pdf`
- Drive historico: `02-admproc.ppt`
- Drive historico: `Resumen Adm.Procesador.docx`
- Drive historico/local: `Cap12.pdf`

### 3. Threads

Tema asociado a administracion de procesador y al TP Linux.

- Concepto de thread/hilo.
- Diferencia entre proceso e hilo.
- Recursos compartidos entre hilos.
- Ejecucion concurrente.
- Uso de `pthreads` en contexto del TP.
- Relacion con planificacion.
- Relacion con sincronizacion.

Fuentes principales:

- `transcripciones/clase03.txt`
- `transcripciones/clase05.txt`
- `pdfs/practicas/Practicas-2-U.pdf`
- Drive historico: `Resumen Threads.docx`
- Drive historico: `TPLinux_PipesYThreads.ppt`

### 4. Concurrencia, Sincronizacion y Semaforos

Es nucleo fuerte del primer parcial.

- Problema de concurrencia.
- Condiciones de carrera.
- Variables compartidas.
- Memoria compartida.
- Seccion critica.
- Exclusion mutua.
- Atomicidad.
- Test and set.
- Semaforos:
  - valor del semaforo;
  - operaciones P y V;
  - bloqueo y desbloqueo;
  - inicializacion;
  - semaforos binarios y de conteo.
- Uso de semaforos para:
  - ordenar secuencias;
  - proteger zonas criticas;
  - sincronizar productores y consumidores;
  - controlar acceso a recursos compartidos.
- Patrones de ejercicios:
  - restricciones de orden entre procesos;
  - procesos que deben alternarse;
  - procesos que comparten estructuras;
  - productor/consumidor;
  - limites de lo que puede resolverse solo con semaforos.
- Errores tipicos:
  - inicializar mal el semaforo;
  - permitir entrada simultanea a zona critica;
  - bloquear procesos de mas;
  - generar interbloqueo accidental.

Fuentes principales:

- `transcripciones/clase03.txt`
- `transcripciones/clase04.txt`
- `transcripciones/clase05.txt`
- `transcripciones/clase08.txt`
- `pdfs/practicas/Practicas-2-U.pdf`
- Drive historico: `03-semaforos.ppt`
- Drive historico: `SemaforosABB.xlsx`
- Drive historico: `SemaforosResueltos.xlsx`
- Drive historico: `regla semaforos.png`

### 5. Administracion de Memoria

Es nucleo fuerte del primer parcial.

- Objetivo de la administracion de memoria.
- Memoria real/fisica vs memoria logica.
- Direccionamiento.
- Reubicacion.
- Registro base.
- Limites de memoria.
- Particiones:
  - particiones fijas;
  - particiones variables;
  - fragmentacion;
  - compactacion.
- Asignacion de memoria a procesos.
- Paginacion:
  - pagina;
  - marco/bloque de memoria real;
  - tabla de paginas;
  - TDP;
  - TDB;
  - traduccion de direcciones;
  - bit de presencia / ausencia;
  - proteccion.
- Memoria virtual:
  - pagina en memoria real;
  - pagina en almacenamiento secundario;
  - falla de pagina;
  - interrupcion por page fault;
  - carga de paginas desde disco;
  - pagina modificada;
  - reemplazo/remocion de paginas.
- Algoritmos y trazas:
  - FIFO;
  - analisis de trazas de referencias;
  - cantidad de marcos;
  - fallas de pagina.
- Segmentacion:
  - segmentos;
  - bibliotecas/codigo compartido;
  - relacion con paginacion.
- Memoria compartida:
  - paginas compartidas;
  - codigo compartido;
  - problemas de direcciones internas.
- Ejercicios de memoria:
  - traduccion de direcciones;
  - tablas;
  - trazas;
  - fallas;
  - reemplazo.

Fuentes principales:

- `transcripciones/clase06.txt`
- `transcripciones/clase07.txt`
- `transcripciones/clase08.txt`
- Drive historico/local: `04-admmem.ppt`
- Drive historico: `Resumen Adm Memoria.docx`
- Drive historico: `Resumen capitulo 13 - administracion memoria`
- Drive historico/local: `Cap13.pdf`
- Drive historico: `ejercicios memoria.txt`
- Drive historico: `direccionamiento memoria.png`

### 6. Arquitectura de Computadoras como base del primer parcial

Este bloque aparece como contexto de la materia y en PDFs locales de arquitectura. En los videos transcritos se usa como base previa para hablar de SO, memoria, procesador, bus y multiprocesamiento.

- Representacion de informacion.
- Sistemas de numeracion.
- Organizacion general del computador.
- CPU/procesador.
- Memoria.
- Entrada/salida.
- Buses.
- Interrupciones.
- Relacion procesador-memoria-perifericos.
- Multiprocesamiento como puente hacia SO.

Fuentes principales:

- `pdfs/arquitecturas/Cap01.pdf` a `pdfs/arquitecturas/Cap10.pdf`
- `pdfs/presentaciones/arquitecturas01.pdf`
- `pdfs/presentaciones/arquitecturas02.pdf`
- `pdfs/presentaciones/arquitecturas03.pdf`
- `transcripciones/clase01.txt`

### 7. Zona de solapamiento del primer parcial

Estos temas aparecen en carpetas historicas de primer parcial de algunos anios, aunque tambien forman parte del bloque fuerte del segundo parcial. Conviene conocerlos si se estudia con modelos viejos.

- Administracion de perifericos.
- Administracion de informacion / archivos.
- File system.
- Ejercicios con perifericos o archivos dentro de modelos historicos.

Fuentes donde aparece el solapamiento:

- Drive historico `CASO 2021/Primer Parcial`
- Drive historico `CASO 2020/Primer Parcial`
- `05-admperifericos.ppt`
- `06-adminfo.ppt`
- `Cap14.pdf`
- `Cap15.pdf`

## Segundo Parcial

### 1. Administracion de Perifericos

Es nucleo fuerte del segundo parcial.

- Funcion de la administracion de perifericos.
- Dispositivos de entrada/salida.
- Perifericos lentos y rapidos.
- Canales/controladores.
- Drivers.
- Interrupciones de E/S.
- Rutinas de atencion de interrupciones.
- Buffers.
- Spooling.
- Asignacion de perifericos:
  - dedicados;
  - compartidos;
  - virtuales;
  - restringidos por usuario/proceso.
- Relacion con procesos bloqueados por E/S.
- Relacion con semaforos cuando el recurso es compartido.
- Ejercicios con disco, cinta, tiempos de E/S y colas.

Fuentes principales:

- Drive historico: `05-admperifericos.ppt`
- Drive historico: `Resumen Adm. Perifericos.docx`
- Drive historico: `Resumen admin perifericos (cap 14).docx`
- Drive historico: `ClasePerif.pdf`
- Drive historico/local: `Cap14.pdf`
- `pdfs/practicas/Practicas-2-U.pdf`

### 2. Administracion de la Informacion / Sistema de Archivos

Es nucleo fuerte del segundo parcial.

- Concepto de archivo.
- Vista del usuario:
  - archivos;
  - carpetas/directorios;
  - nombres;
  - rutas.
- Vista interna del sistema operativo:
  - directorio como archivo;
  - entradas de directorio;
  - metadatos;
  - bloques logicos y fisicos;
  - contenido del archivo.
- Administracion de espacio en disco.
- Bloques libres.
- Formateo de periferico.
- Asignacion de bloques a archivos.
- Estructuras de administracion de archivos.
- Catalogo de usuario.
- Archivos permanentes.
- Comandos de control:
  - crear archivo;
  - asignar archivo;
  - borrar archivo.
- Permisos sobre archivos:
  - lectura;
  - grabacion/escritura;
  - usuario;
  - todos;
  - ninguno.
- Ejercicios con:
  - LCA;
  - LCU;
  - listas de bloques;
  - asignacion/liberacion;
  - comandos de control;
  - permisos.

Fuentes principales:

- `transcripciones/clase08.txt`
- `pdfs/practicas/Practicas-3-U.pdf`
- Drive historico: `06-adminfo.ppt`
- Drive historico/local: `Cap15.pdf`
- Drive historico: `Practica 3 caso.pdf`
- Drive historico: `Practica 3 caso.docx`
- Drive historico: `LCA.txt`
- Drive historico: `LCU.txt`
- Drive historico: `LCU parcial.txt`

### 3. Deadlocks

Es nucleo fuerte del segundo parcial.

- Concepto de deadlock / interbloqueo.
- Recursos y procesos.
- Condiciones necesarias de deadlock:
  - exclusion mutua;
  - retencion y espera;
  - no apropiacion;
  - espera circular.
- Grafo de asignacion de recursos.
- Deteccion de deadlock.
- Prevencion.
- Evitacion.
- Recuperacion.
- Estado seguro e inseguro.
- Algoritmo del banquero:
  - recursos existentes;
  - recursos disponibles;
  - asignacion;
  - maximo declarado;
  - necesidad restante;
  - secuencia segura.
- Ejercicios:
  - determinar si hay deadlock;
  - encontrar secuencia segura;
  - decidir si se puede conceder un pedido;
  - completar matrices/tablas.

Fuentes principales:

- Drive historico: `08-deadlock.ppt`
- Drive historico: `Sistemas-Operativos-Silberschatz-Galvin - banquero.pdf`
- Drive historico/local: `Cap17.pdf`
- Modelos historicos de segundo parcial.

### 4. Concurrencia de Procesos

Tema del segundo parcial en materiales historicos, distinto del bloque inicial de semaforos porque aparece conectado con deadlocks, recursos y modelos mas generales.

- Procesos concurrentes.
- Recursos compartidos.
- Coordinacion entre procesos.
- Esperas.
- Interacciones que pueden derivar en bloqueo.
- Relacion con semaforos.
- Relacion con deadlocks.
- Grafos/modelos de concurrencia.

Fuentes principales:

- Drive historico: `09-concurrenciaproc.ppt`
- Drive historico/local: `Cap18.pdf`
- Modelos historicos de segundo parcial.

### 5. Proteccion y Seguridad

Es nucleo fuerte del segundo parcial.

- Diferencia entre proteccion y seguridad.
- Objetos y sujetos.
- Usuarios y grupos.
- Permisos.
- Derechos de acceso.
- Matriz de acceso.
- Tablas/listas de permisos.
- Control de acceso a archivos y recursos.
- Lectura, escritura/grabacion y ejecucion cuando corresponda.
- Problemas tipicos:
  - decidir permisos validos;
  - completar tablas;
  - analizar accesos permitidos/denegados;
  - vincular permisos con usuarios o grupos.

Fuentes principales:

- Drive historico: `10-proteccionyseguridad.ppt`
- Drive historico: `Sistemas-Operativos-Silberschatz-Galvin - tablas permisos.pdf`
- Drive historico/local: `Cap19.pdf`
- `pdfs/practicas/Practicas-3-U.pdf`

### 6. Sistemas Distribuidos

Este bloque aparece en la practica local `Practicas-4-U.pdf` y en la carpeta local `pdfs/SO distribuidos/`. Conviene tratarlo como tema posible de segundo parcial o cierre de cursada, segun el anio/modelo usado.

- Introduccion a sistemas distribuidos.
- Sistemas distribuidos vs sistemas centralizados.
- Ventajas y desventajas de distribuidos.
- Multiprocesador vs multicomputadora.
- Caches y coherencia.
- Semaforos en multiprocesadores con cache coherente.
- Crossbar switch.
- Redes/topologias:
  - reticula;
  - hipercubo;
  - red omega.
- Imagen de unico sistema.
- Sistema operativo distribuido vs sistema operativo de red.
- Microkernel vs nucleo monolitico.
- Rendimiento:
  - ciclos de reloj;
  - CPI;
  - MIPS;
  - tiempo de ejecucion.

Fuentes principales:

- `pdfs/practicas/Practicas-4-U.pdf`
- `pdfs/SO distribuidos/Cap20.pdf` a `pdfs/SO distribuidos/Cap26.pdf`

### 7. Linux, Kernel, TP y Servicios

No es el nucleo teorico clasico del segundo parcial, pero si aparece como bloque de TP/cierre y puede cruzarse con final o entrega practica.

- Linux como entorno del TP.
- Maquinas virtuales.
- Instalacion/particionado.
- Comandos basicos de archivos.
- Pipes.
- Threads.
- Modulos del kernel.
- Archivos en `/proc`.
- Servicios `systemd`.
- Archivos `.service`.
- `ExecStart`.
- `ExecStop`.
- Targets.
- `multi-user.target`.
- Diferencia conceptual con esquemas previos de `init`.

Fuentes principales:

- `transcripciones/clase02.txt`
- `transcripciones/clase06.txt`
- `transcripciones/clase07.txt`
- `transcripciones/clase08.txt`
- `transcripciones/clase27.txt`
- Drive historico: `TPLinux_MODULES.pdf`
- Drive historico: `TPLinux_PipesYThreads.ppt`
- Drive historico: TPs `tp-unsam-2020-2`, `tp-unsam-2021-1`, `tp-unsam-2021-2`

## Resumen ultra compacto

### Primer Parcial

- Introduccion a SO.
- Kernel, servicios, capas, monolitico/microkernel/hibrido.
- Administracion del procesador.
- Procesos, BCP/PCB, estados, transiciones.
- Planificacion: FIFO, Round Robin, quantum, mas corto primero, turnaround, prioridades, multicolas.
- Interrupciones, rutinas del SO, cambio de contexto, idle.
- Threads.
- Concurrencia y semaforos.
- Seccion critica, exclusion mutua, P/V, atomicidad, productor/consumidor.
- Administracion de memoria.
- Particiones, reubicacion, paginacion, TDP/TDB, memoria virtual, page fault, reemplazo, trazas, segmentacion, memoria compartida.
- Arquitectura de computadoras como base: CPU, memoria, E/S, buses, interrupciones.
- Zona de solapamiento: perifericos y archivos aparecen en algunos modelos/carpetas de primer parcial.

### Segundo Parcial

- Administracion de perifericos.
- E/S, drivers, interrupciones, buffers, spooling, asignacion de dispositivos.
- Administracion de informacion / archivos.
- Directorios, bloques, catalogos, comandos de control, permisos, LCA/LCU.
- Deadlocks.
- Condiciones, grafos, prevencion, evitacion, deteccion, banquero, estados seguros.
- Concurrencia de procesos.
- Proteccion y seguridad.
- Matriz/listas de acceso, usuarios, grupos, permisos.
- Sistemas distribuidos como tema posible: CPI, MIPS, multiprocesadores, multicomputadoras, topologias, microkernel, SO distribuido vs SO de red.
- Linux/TP/systemd como bloque practico y de cierre.

## Fuentes por parcial

### Fuentes principales para estudiar Primer Parcial

- [[mapa_temas_videos]]
- `transcripciones/clase01.txt`
- `transcripciones/clase02.txt`
- `transcripciones/clase03.txt`
- `transcripciones/clase04.txt`
- `transcripciones/clase05.txt`
- `transcripciones/clase06.txt`
- `transcripciones/clase07.txt`
- `transcripciones/clase08.txt`
- `pdfs/practicas/Practicas-2-U.pdf`
- `pdfs/arquitecturas/`
- `pdfs/presentaciones/`
- Drive historico:
  - `02-admproc.ppt`
  - `03-semaforos.ppt`
  - `04-admmem.ppt`
  - `Resumen Adm.Procesador.docx`
  - `Resumen Threads.docx`
  - `Resumen Adm Memoria.docx`
  - `Cap12.pdf`
  - `Cap13.pdf`
  - modelos de primer parcial.

### Fuentes principales para estudiar Segundo Parcial

- [[contexto_fuentes_caso]]
- `transcripciones/clase08.txt`
- `transcripciones/clase27.txt`
- `pdfs/practicas/Practicas-3-U.pdf`
- `pdfs/practicas/Practicas-4-U.pdf`
- `pdfs/sitemas operativos/Cap14.pdf`
- `pdfs/sitemas operativos/Cap15.pdf`
- `pdfs/sitemas operativos/Cap17.pdf`
- `pdfs/sitemas operativos/Cap18.pdf`
- `pdfs/sitemas operativos/Cap19.pdf`
- `pdfs/SO distribuidos/`
- Drive historico:
  - `05-admperifericos.ppt`
  - `06-adminfo.ppt`
  - `08-deadlock.ppt`
  - `09-concurrenciaproc.ppt`
  - `10-proteccionyseguridad.ppt`
  - `ClasePerif.pdf`
  - `Practica 3 caso.pdf`
  - `LCA.txt`
  - `LCU.txt`
  - modelos de segundo parcial.

## Pendientes para volverlo 100% auditado por clase

- Completar transcripcion de clase 9.
- Transcribir/revisar clases 10 a 26.
- Revisar los modelos concretos de primer y segundo parcial para confirmar si en el anio actual perifericos/archivos entran en primero, segundo o ambos.
- Crear MOCs separados:
  - `MOC - Primer Parcial`
  - `MOC - Segundo Parcial`

