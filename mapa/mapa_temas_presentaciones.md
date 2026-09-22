# Mapa de temas segun presentaciones

> Fuente unica de este mapa: archivos PDF ubicados en `src/pdfs/presentaciones/`.
>
> Criterio: no se usaron videos, transcripciones, practicas, capitulos de libros ni busquedas web. Este mapa resume solamente los temas que aparecen en las presentaciones dadas por los profesores.
>
> Nota tecnica: algunas diapositivas son principalmente graficas o imagenes y no tienen texto extraible. En esos casos se toma el bloque tematico del archivo y de las diapositivas cercanas.

## Presentaciones usadas

- `src/pdfs/presentaciones/intro SO.pdf`
- `src/pdfs/presentaciones/admin del procesador.pdf`
- `src/pdfs/presentaciones/threads.pdf`
- `src/pdfs/presentaciones/semaforos.pdf`
- `src/pdfs/presentaciones/admin de memoria.pdf`
- `src/pdfs/presentaciones/admin de la info.pdf`
- `src/pdfs/presentaciones/arquitecturas01.pdf`
- `src/pdfs/presentaciones/arquitecturas02.pdf`
- `src/pdfs/presentaciones/arquitecturas03.pdf`

## Mapa consolidado

### 1. Introduccion a Sistemas Operativos

Fuente principal: `intro SO.pdf`.

Temas:

- Objetivos de un sistema operativo.
- Sistema operativo como interfaz entre usuario y maquina.
- Sistema operativo como administrador de recursos.
- Programa de control.
- Evolucion de los sistemas operativos:
  - primeros sistemas;
  - programador como operador;
  - bibliotecas de drivers;
  - compiladores;
  - monitor simple;
  - batch sencillo;
  - batch sofisticado;
  - multiprogramacion;
  - time sharing;
  - sistemas de tiempo real;
  - multiprocesamiento;
  - sistemas operativos distribuidos.
- Instrucciones privilegiadas.
- Modo maestro/supervisor y modo esclavo/usuario.
- Buffering.
- Operacion off-line.
- Spooling.
- Planificacion de CPU en tiempo compartido.
- Intercambio de contexto.
- Dumps y debug estatico.
- Tiempo de respuesta en sistemas de tiempo real.
- Multiprocesamiento con varias CPU.
- CPU coordinadora / host.
- Servicios del sistema operativo:
  - ejecucion de procesos;
  - operaciones de entrada/salida;
  - sistema de archivos;
  - deteccion de errores;
  - administracion y asignacion de recursos;
  - accounting;
  - proteccion entre procesos.
- Estructura de sistemas operativos.
- Modulos e interfaces.
- Diseno en capas.
- Ejemplos de sistemas:
  - DOS;
  - UNIX;
  - AIX;
  - THE;
  - OS/2;
  - Windows NT;
  - Linux;
  - Android OS;
  - Chrome OS;
  - Firefox OS.
- Kernel Linux:
  - kernel monolitico;
  - modulos;
  - subsistemas;
  - `kernel/`;
  - `mm/`;
  - `fs/`;
  - `net/`;
  - `drivers/`;
  - interfaz con usuario;
  - construcciones virtuales;
  - bridges;
  - logica;
  - interfaz con hardware.
- Vista preliminar del diagrama de estados de un proceso.

### 2. Arquitectura, Paralelismo y Plataformas

Fuentes principales:

- `arquitecturas01.pdf`
- `arquitecturas02.pdf`
- `arquitecturas03.pdf`

#### 2.1 Vocabulario y arquitectura de sistemas

Temas:

- Relacion entre sistemas operativos, arquitecturas y paralelismo.
- Sistema operativo como administrador de recursos.
- Maquina virtual.
- Comunicacion usuario-maquina.
- Funciones del sistema operativo:
  - secuenciar tareas;
  - interpretar lenguaje de control;
  - administrar recursos;
  - manejar concurrencia;
  - compartir recursos;
  - almacenamiento a largo plazo.
- Monoprocesador.
- Monoprogramacion / monotarea.
- Multiprogramacion / multitarea.
- Multiprocesador.
- Procesadores independientes.
- Cores.
- Dual core / multiples cores.
- Hyper Threading.
- Memoria unica.
- Memoria distribuida.
- Sistemas fuertemente acoplados.
- Sistemas debilmente acoplados.
- Memorias:
  - UMA;
  - NUMA;
  - NORMA;
  - COMA;
  - ccNUMA;
  - SMP.
- Cache:
  - bus compartido;
  - snoopy;
  - write-through;
  - estados de consistencia;
  - TLB.
- Sistemas distribuidos:
  - cooperar;
  - compartir;
  - MPI;
  - PVM;
  - DSM.
- Buses y dispositivos:
  - PCI;
  - PCI Express;
  - switch;
  - link layer.
- Ejemplos de hardware/plataformas:
  - Intel S5000PAL;
  - Intel Core i7;
  - AMD Opteron 6000;
  - Motherboard Tyan;
  - Intel 5520 IOH;
  - Xeon 7500;
  - GPUs para calculo;
  - Xeon Phi;
  - Larabee;
  - MIC.

#### 2.2 Cluster, Grid y Cloud

Temas:

- Cluster.
- Nodo.
- Cluster Sheldon.
- ISAAC.
- Red InfiniBand.
- Red Gigabit Ethernet.
- Grid.
- Cloud.
- Proxy en cloud.
- Sistemas operativos:
  - monoliticos;
  - modulares;
  - centralizados;
  - en red;
  - distribuidos.
- Microkernel.
- Comparacion de paradigmas de sistemas operativos.

#### 2.3 Arquitectura de computadores

Temas:

- Arquitectura como estructura abstracta con set fijo de instrucciones.
- Componentes de una arquitectura.
- Interconexion entre componentes.
- Relacion entre arquitectura y sistema operativo.
- Procesador de un bus.
- Registros asociados a memoria:
  - RDM;
  - RBM.
- Procesador multibus.
- Unidad de control.
- Decodificacion de codigo de operacion.
- Niveles de arquitectura:
  - exoarquitectura;
  - arquitectura;
  - microarquitectura.
- Arquitecturas secuenciales.
- Von Neumann.
- Harvard.
- Programa almacenado.
- Datos almacenados.
- Unidades funcionales.
- Estructura bus.
- Dos buses.
- Procesador.
- Canales.
- Colisiones.
- Robo de ciclos.
- Etapas de una instruccion:
  - generar direccion de proxima instruccion;
  - buscar instruccion;
  - decodificar instruccion;
  - generar direccion de operandos;
  - buscar operandos;
  - ejecutar instruccion;
  - almacenar resultados.
- Clasificacion de Flynn:
  - SISD;
  - SIMD;
  - MISD;
  - MIMD.
- Flujos de datos e instrucciones.
- Memoria para accesos multiples.
- Intercalacion de direcciones.
- Paradigmas:
  - control flow;
  - data flow;
  - Von Neumann;
  - Harvard;
  - dinamica.

#### 2.4 Paralelismo y pipelines

Temas:

- Concurrencia, paralelismo, simultaneidad y pipelining.
- Sucesos paralelos.
- Sucesos simultaneos.
- Sucesos pipeline.
- Niveles de paralelismo:
  - multiprogramacion;
  - multiprocesamiento;
  - tarea/procedimiento;
  - interinstrucciones;
  - intrainstrucciones.
- Condiciones de Bernstein.
- Dependencias transitivas.
- Grafos de precedencia.
- Pipeline:
  - paralelismo temporal;
  - paralelismo espacial;
  - ciclo de ejecucion;
  - pipeline de instrucciones;
  - pipeline aritmetico;
  - pipeline de procesador;
  - pipeline unifuncional/multifuncional;
  - pipeline estatico/dinamico;
  - pipeline escalar/vectorial.
- Tablas de reserva.
- Latencia.
- Aceleracion.
- Pipelines voraces y no voraces.
- Latencia optima.
- Vector de colisiones.
- Pipeline con salto incondicional.
- Pipeline sumador de punto flotante.
- Pipeline vectorial.
- Problemas de pipeline:
  - RAW;
  - WAR;
  - WAW;
  - condiciones de salto.
- Prediccion de saltos:
  - estatica;
  - dinamica;
  - nunca salta;
  - siempre salta;
  - casos TNTN;
  - ejemplos Intel i486, Sun SuperSparc, DEC Alpha 21064, Intel Pentium.

### 3. Administracion del Procesador

Fuente principal: `admin del procesador.pdf`.

Temas:

- Concepto de administracion del procesador.
- Asignacion del control de CPU a procesos.
- Metricas:
  - throughput;
  - turnaround.
- Tiempos consumidos por el sistema operativo.
- Monoprogramacion.
- Multiprogramacion.
- E/S y tiempos ociosos de CPU.
- Preparacion y lanzamiento de E/S.
- Liberacion de recursos al finalizar procesos.
- Decision del planificador cuando hay mas de un proceso.
- Planificador de procesos.
- Rutinas del sistema operativo para administrar procesos.
- Identificacion de procesos.
- Bloque de Control de Proceso:
  - BCP;
  - informacion del proceso;
  - recursos;
  - estado.
- Diagrama de transicion de estados.
- Eventos y rutinas que intervienen en las transiciones:
  - comenzar a listos;
  - listos a ejecutando;
  - ejecutando a listos;
  - ejecutando a bloqueado por E/S;
  - bloqueado por E/S a listos;
  - ejecutando a terminado;
  - cambios de estado.
- Control del sistema operativo en todo cambio de estado.
- Algoritmos de administracion del procesador:
  - FIFO / FCFS;
  - mas corto primero sin desalojo;
  - mas corto primero con desalojo;
  - mas corto primero con desalojo por tiempo remanente;
  - prioridades;
  - Round Robin;
  - multicolas.
- Estimacion de rafaga de proceso.
- Turnaround en los algoritmos de planificacion.
- Calesita de Round Robin.
- Colas de listos de distinta prioridad.

### 4. Threads

Fuente principal: `threads.pdf`.

Temas:

- Hilos / threads.
- Lightweight process / procesos ligeros.
- Concepto y beneficios.
- Threads compartiendo espacio de direcciones del proceso.
- Ganancia por bloqueo de un hilo y ejecucion de otro hilo del mismo proceso.
- Cambio de contexto entre hilos.
- Transicion de dominio.
- Menor vaciado de cache entre hilos.
- Elementos por hilo y por proceso.
- Estructuras de implementacion:
  - servidor-trabajador;
  - equipo;
  - pipeline.
- Reconocimiento de threads:
  - en espacio de usuario;
  - en el nucleo.
- Sistemas que implementan threads en kernel:
  - Windows XP/2000;
  - OS/2;
  - Solaris;
  - MACH;
  - CHORUS;
  - Linux;
  - Tru64 UNIX;
  - Mac OS X.
- Implementacion en espacio de usuario:
  - sistema de tiempo de ejecucion;
  - interceptar llamadas bloqueantes;
  - intercambio del procesador entre hilos;
  - ventajas;
  - desventajas;
  - jackets;
  - planificacion propia de cada proceso;
  - bloqueo por falla de pagina;
  - intercambio de contexto de menor costo.
- Implementacion en el nucleo:
  - reconocimiento por el sistema operativo;
  - mayor costo de cambio de contexto;
  - mayor espacio en tablas y pilas del nucleo;
  - escalabilidad.
- Problemas generales:
  - variables globales;
  - corrupcion por uso concurrente;
  - seniales;
  - captura de seniales por distintos hilos.
- Crear procesos con `fork`.
- Crear threads / LWP.
- Estandar POSIX.
- `pthread`.
- Ejemplos con `pthread_create`.

### 5. Semaforos y Sincronizacion

Fuente principal: `semaforos.pdf`.

Temas:

- Semaforos.
- Necesidad de semaforos para:
  - sincronizar procesos;
  - exclusion mutua;
  - zonas criticas;
  - abstraccion de recursos.
- Semaforo como variable que permite o no el paso.
- Estado disponible / ocupado.
- Aproximacion inicial con cierre y apertura.
- Espera activa / loop de uso de procesador.
- Inseguridad de aproximaciones simples.
- `Test&Set`.
- `Wait`.
- `Signal`.
- Cola asociada al semaforo.
- Politica FIFO en espera.
- Semaforos contadores de Dijkstra.
- Operaciones:
  - `P(x)`;
  - `V(x)`.
- Modelo de exclusion:
  - inicializacion en 1;
  - entrada y salida de zona critica.
- Modelo productor-consumidor:
  - un mensaje;
  - varios espacios;
  - emisor;
  - receptor;
  - vector circular;
  - indices modulo N.
- Problemas por cambio de informacion:
  - datos;
  - estructuras;
  - necesidad de serializar.
- Exclusiones mal ubicadas.
- Solucion con orden correcto de semaforos:
  - primero recurso/espacio o mensaje;
  - luego exclusion.
- Implementacion con stack.
- Semaforos para:
  - maximo de mensajes producibles;
  - mensajes disponibles para consumo;
  - exclusion.
- Estudios de casos de secuencias:
  - `ABCABC...`;
  - `ABBABB...`;
  - `A(BC)` o `A(CB)`;
  - `ABCACBABCACB...`.
- Implementacion en Linux/System V IPC:
  - `semid_ds`;
  - `ipc_perm`;
  - permisos;
  - creador;
  - `semget`;
  - operacion P;
  - operacion V.
- Implementacion POSIX:
  - `sem_close`;
  - `sem_destroy`;
  - `sem_getvalue`;
  - `sem_init`;
  - semaforos con nombre;
  - `sem_wait`;
  - `sem_post`.

### 6. Administracion de Memoria

Fuente principal: `admin de memoria.pdf`.

Temas:

- Funciones de la administracion de memoria:
  - asignar memoria a procesos;
  - proteger espacios de memoria;
  - evitar interferencia entre procesos;
  - administrar memoria compartida por SO y procesos.
- Tipos de administracion:
  - simple contigua;
  - particionado fijo;
  - particionado variable con/sin compactacion;
  - paginacion;
  - paginacion por demanda / memoria virtual;
  - segmentacion.
- Simple contigua:
  - ubicacion del SO y proceso;
  - fragmentacion externa;
  - administracion trivial;
  - ausencia de multiprogramacion.
- Variantes:
  - overlay;
  - swapping.
- Particionado fijo:
  - particiones;
  - tabla de particiones;
  - direccion de comienzo;
  - tamano de particion;
  - fragmentacion interna.
- Particionado variable:
  - huecos libres;
  - fragmentacion externa;
  - compactacion;
  - compactacion memoria-a-memoria;
  - compactacion memoria-disco-memoria;
  - costo de compactacion;
  - estrategias de asignacion:
    - mejor ajuste;
    - peor ajuste;
    - primer ajuste.
- Paginacion:
  - dividir memoria en bloques/frames;
  - dividir proceso en paginas;
  - paginas y bloques de igual tamano;
  - carga de paginas;
  - fragmentacion interna del ultimo bloque;
  - direcciones logicas/virtuales;
  - pagina y desplazamiento;
  - DAT / Direct Address Translator;
  - bus de direcciones;
  - traduccion de direccion;
  - doble acceso a memoria;
  - tabla de paginas;
  - TDP por proceso;
  - TDB del sistema.
- Paginacion por demanda / memoria virtual:
  - no cargar todas las paginas simultaneamente;
  - disco de memoria virtual;
  - tabla de paginas extendida;
  - paginas en memoria y en disco;
  - cache / TLB;
  - algoritmos de remocion:
    - FIFO;
    - LRU;
    - LFU.
- Problemas de memoria virtual:
  - buffer a caballo;
  - canales de E/S con direcciones fisicas;
  - thrashing;
  - paginas atadas a E/S;
  - paginas en transito;
  - bit de proteccion de bloque.
- Algoritmo completo de paginacion.
- Ejercicios:
  - direccionamiento de 14 bits;
  - memoria real de 4K;
  - paginas de 256 bytes;
  - tamano maximo de programa;
  - traduccion de direccion virtual.
- Traza:
  - sucesion de paginas referenciadas;
  - seguimiento con algoritmos de remocion;
  - indices de fallo/hallazgo.
- Anomalia de Belady.
- Prediccion de tasas de page fault.
- Tamano de pagina.
- Segmentacion:
  - segmentos;
  - direccionamiento segmentado;
  - tablas de segmentos;
  - ventajas y desventajas;
  - ejemplos de sistemas segmentados.
- Direccionamiento indirecto.
- Combinacion de segmentacion y paginacion.
- Paginacion de dos niveles.
- Paginacion de tres niveles en Linux.

### 7. Administracion de la Informacion / File System

Fuente principal: `admin de la info.pdf`.

Temas:

- Administracion de la informacion.
- File system.
- Objetivos:
  - administracion de archivos;
  - administracion de espacios en dispositivos compartidos;
  - administracion de accesos a archivos.
- Funcion del FS:
  - implementar archivos y directorios desde unidades de acceso de disco;
  - recibir peticiones de procesos de usuario;
  - enviar peticiones a gestores de dispositivos;
  - brindar servicios visibles al usuario.
- Directorio.
- Directorio de primer nivel.
- VTOC / Volume Table of Contents.
- Entrada de directorio:
  - nombre;
  - ubicacion;
  - longitud;
  - longitud de registro logico;
  - informacion de archivo.
- Ejemplo de directorio.
- Ocupacion de espacio:
  - asignacion contigua;
  - extension limitada;
  - primer lugar libre;
  - mejor lugar;
  - asignacion dinamica por mapeo de bloques;
  - ausencia de compactacion.
- Estructura de directorios.
- Catalogo de usuarios por volumen.
- Directorio de dos niveles.
- Directorios de dos o mas niveles.
- Evitar multiples accesos.
- TNA.
- TAA.
- Modelo general de acceso:
  - busqueda en catalogo;
  - SAS;
  - SAB;
  - TNA;
  - TAA;
  - control de accesos;
  - VCA;
  - permisos;
  - calculo de direccion logica;
  - SAL;
  - calculo de direccion fisica;
  - SAF;
  - MEA;
  - MEP.
- Calculos:
  - registro logico;
  - registro fisico;
  - direccion logica;
  - direccion fisica;
  - resto/desplazamiento.
- Metodo general de acceso.
- Llamadas simbolicas y basicas:
  - `CALL SAS`;
  - `CALL SAB`;
  - lectura;
  - identificador de archivo;
  - direccion de memoria.
- Verificacion de control de acceso.
- Sistema de archivos logicos.
- Sistema de archivos fisicos.
- Modulo de estrategia de asignacion.
- Modulo de estrategia de periferico.
- Listas de control:
  - LCA;
  - LCU.
- Ejemplos con JCL.
- Asociacion de dispositivos, archivos, TNA/TAA, permisos, buffers y BCP.
- `Open`.
- `READ`.
- CDL.
- CDF.
- Ejemplo en cluster con PBS.
- Sistemas de archivos:
  - FAT;
  - UNIX;
  - Linux;
  - NTFS;
  - HPFS;
  - XFS.
- FAT:
  - area reservada;
  - FAT principal;
  - copias adicionales;
  - directorio raiz;
  - area de datos.
- UNIX:
  - FS y swap;
  - archivos sin formato;
  - directorios con formato;
  - inodo;
  - usuario;
  - grupo;
  - permisos;
  - tiempos;
  - hard links;
  - tipo de archivo;
  - apuntadores directos;
  - indirecto;
  - doble indirección;
  - triple indirección;
  - directorio con `.` y `..`;
  - busqueda por FS/inodo;
  - inodo en memoria;
  - `sync`;
  - superblock;
  - ext3 y journaling;
  - file descriptor.
- Linux:
  - soporte de multiples FS;
  - VFS;
  - VFS superblock;
  - VFS inode;
  - operaciones de superblock;
  - blocksize;
  - device.
- NTFS:
  - sector;
  - cluster;
  - volumen;
  - particion logica;
  - sector de arranque;
  - MFT;
  - MFT espejo;
  - registros/transacciones;
  - mapa de bits de agrupamientos;
  - area de datos;
  - filas de longitud variable;
  - archivos pequenos dentro de MFT.
- HPFS.
- XFS:
  - 64 bits;
  - journaling;
  - allocation groups;
  - inodos;
  - extents;
  - block size;
  - arbol B+.

## Orden sugerido de estudio segun estas presentaciones

1. `intro SO.pdf`: objetivos, evolucion, servicios y estructura del SO.
2. `arquitecturas01.pdf`, `arquitecturas02.pdf`, `arquitecturas03.pdf`: base de arquitectura, paralelismo, clusters, pipelines y clasificacion de arquitecturas.
3. `admin del procesador.pdf`: procesos, estados, BCP, rutinas, planificacion y algoritmos.
4. `threads.pdf`: hilos, implementaciones y POSIX.
5. `semaforos.pdf`: sincronizacion, exclusion, productor-consumidor e implementaciones.
6. `admin de memoria.pdf`: modelos de administracion de memoria, paginacion, memoria virtual y segmentacion.
7. `admin de la info.pdf`: sistema de archivos, directorios, acceso, permisos, LCA/LCU y FS concretos.

## Indice rapido por presentacion

### `intro SO.pdf`

- Objetivos y evolucion de SO.
- Monitor simple, batch, time sharing, tiempo real y multiprocesamiento.
- Servicios del SO.
- Estructura en capas.
- Linux, Android, Chrome OS y otros ejemplos.
- Kernel Linux y subsistemas.

### `admin del procesador.pdf`

- Throughput y turnaround.
- Monoprogramacion y multiprogramacion.
- Rutinas de SO para procesos.
- BCP.
- Estados y transiciones.
- FIFO, SJF, prioridades, Round Robin y multicolas.

### `threads.pdf`

- Concepto de threads.
- Beneficios.
- Estructuras servidor-trabajador, equipo y pipeline.
- Threads de usuario vs kernel.
- Problemas de variables globales y seniales.
- POSIX pthreads.

### `semaforos.pdf`

- Sincronizacion y exclusion mutua.
- Test&Set, Wait, Signal.
- P/V de Dijkstra.
- Productor-consumidor.
- Casos de secuencias.
- Implementacion IPC y POSIX.

### `admin de memoria.pdf`

- Simple contigua, overlay, swapping.
- Particionado fijo y variable.
- Compactacion.
- Paginacion.
- Memoria virtual.
- TLB.
- FIFO, LRU, LFU.
- Thrashing.
- Segmentacion.
- Paginacion multinivel.

### `admin de la info.pdf`

- FS, directorios, VTOC.
- TNA, TAA, SAS, SAB, VCA, SAL, SAF, MEA, MEP.
- LCA y LCU.
- FAT, UNIX, Linux VFS, NTFS, HPFS, XFS.

### `arquitecturas01.pdf`

- Vocabulario de SO y arquitectura.
- Monoprocesador, multiprocesador, cores, hyperthreading.
- UMA, NUMA, NORMA, COMA, ccNUMA, SMP.
- Cache y TLB.
- Sistemas distribuidos, PCI/PCIe, GPUs, Xeon Phi.

### `arquitecturas02.pdf`

- Cluster, grid y cloud.
- Microkernel y paradigmas de SO.
- Arquitectura de computadores.
- Buses, unidad de control, Von Neumann, Harvard.
- Flynn: SISD, SIMD, MISD, MIMD.
- Paralelismo y condiciones de Bernstein.

### `arquitecturas03.pdf`

- Pipelines.
- Latencia, aceleracion y tablas de reserva.
- Vector de colisiones.
- Pipeline vectorial y de punto flotante.
- RAW, WAR, WAW.
- Prediccion de saltos.

## Temas que aparecen como eje fuerte

- Sistema operativo como administrador de recursos.
- Estructura del SO y kernel.
- Arquitectura de hardware y paralelismo.
- Administracion del procesador.
- Procesos, estados y planificacion.
- Threads.
- Semaforos y sincronizacion.
- Administracion de memoria.
- Paginacion, memoria virtual y segmentacion.
- Administracion de archivos e informacion.
- Sistemas de archivos reales.

## Temas de ejercicios sugeridos por las presentaciones

- Calculo de turnaround.
- Simulacion de algoritmos de planificacion.
- Seguimiento de transiciones de estados.
- Resolucion de productor-consumidor con semaforos.
- Ubicacion correcta de exclusiones.
- Traduccion de direcciones en paginacion.
- Seguimiento de trazas con FIFO, LRU y LFU.
- Analisis de anomalia de Belady.
- Calculo de direccion logica/fisica en archivos.
- Manejo de LCA/LCU y permisos.
- Apuntadores de inodos.
- Analisis de pipelines, latencias y colisiones.

