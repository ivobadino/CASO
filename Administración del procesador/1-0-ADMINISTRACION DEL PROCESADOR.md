# 1-0-Administración del procesador

Decide qué proceso usa la CPU, cuándo y durante cuánto tiempo.

Empezar por [[Administración del procesador/2-0-Concepto de proceso|Concepto de proceso]]. Relacionar con memoria y periféricos. Volver a [[CASO]].

Base y temas para seguir: Procesador en el mapa local (mapa/mapa_definitivo_parciales#2. Administracion del Procesador).

## Apuntes previos

La administracion del procesdor es la parte del sistema operativo que decide que proceso usa la CPU, cuando la usa y por cuanto tiempo.

En este caso si en la pc se quiere ejecutar un solo programa, la misma perderia mucha funcionalidad e ineficiencia, incluso, muchos programas tienen muchos sub procesos que se tienen que ejecutar en paralelo. Para ello hay que implementar sistemas pro software o hardware para poder gestionar de forma eficiente el uso del procesador.

Como  normalmente hay varios procesos queriendo ejecutar pero al cpu es un recurso limitado, el sistema operativo necesita organizar esa competencia. Para esto usa estructura como la cola de listos, el BCP/PCB, el planificador de procesos y distintas pliticas de asignacion fomo FIFO, round robin, prioridades, multicolas, etc.

Busca principalmente:

- Aprovechar la CPU lo máximo posible.
- Reducir tiempos muertos.
- Mejorar el tiempo de respuesta.
- Hacer que varios procesos parezcan avanzar “a la vez”.
- Cambiar de un proceso a otro cuando uno termina, se bloquea, pide E/S o es desalojado.

En multiprogramación, esto es fundamental: si un proceso está esperando una entrada/salida, la CPU no debería quedarse ociosa; el SO puede darle la CPU a otro proceso listo.

Una respuesta de parcial podría ser:

> La administración del procesador es el conjunto de mecanismos y políticas del sistema operativo encargados de asignar el recurso CPU a los distintos procesos del sistema, decidiendo cuál pasa de listo a ejecutando, cuándo se produce un cambio de contexto y qué criterio de planificación se utiliza para mejorar el rendimiento y el tiempo de respuesta.

---
TEMAS:
- [[Administración del procesador/2-0-Concepto de proceso|Concepto de proceso]].
- [[Administración del procesador/2-0-Concepto de proceso|Programa vs proceso]].
- [[Administración del procesador/3-0-Carga de un programa en memoria|Carga de un programa en memoria]].
- [[Administración del procesador/4-0-Recursos asociados a un proceso|Recursos asociados a un proceso]].
- [[Administración del procesador/5-0-Bloque de Control de Proceso|Bloque de Control de Proceso]]:
  - BCP / PCB;
  - informacion del proceso;
  - registros;
  - estado;
  - recursos asociados.
- [[Administración del procesador/6-0-Estados de proceso|Estados de proceso]]:
  - comenzar / nuevo;
  - listo;
  - ejecutando;
  - bloqueado / espera;
  - terminado.
- [[Administración del procesador/6-6-Diagrama de transición de estados|Diagrama de transicion de estados]].
- [[Administración del procesador/6-7-Eventos que provocan transiciones|Eventos que provocan transiciones]].
- [[Administración del procesador/7-0-Interrupciones y rutinas de atención|Interrupciones y rutinas de atencion]].
- [[Administración del procesador/8-0-Planificador de procesos|Planificador de procesos]].
- [[Administración del procesador/8-1-Cola de listos|Cola de listos]].
- [[Administración del procesador/8-2-Colas de bloqueados por recurso|Colas de bloqueados por recurso]].
- [[Administración del procesador/9-0-Cambio de contexto|Cambio de contexto]].
- [[Administración del procesador/10-0-Idle - proceso ocioso|Idle / proceso ocioso]].
- [[Administración del procesador/11-0-Multiprogramación|Multiprogramacion]].
- [[Administración del procesador/12-0-Simultaneidad y paralelismo|Simultaneidad y paralelismo]].
- [[Administración del procesador/13-0-Políticas de planificación del procesador|Administraciones de procesador]]:
  - FIFO / FCFS;
  - Round Robin;
  - quantum;
  - mas corto primero;
  - comparacion por turnaround;
  - multicolas;
  - prioridades;
  - procesos interactivos vs batch.
- [[Administración del procesador/14-0-Ejercicios de cronograma|Ejercicios de cronograma]]:
  - CPU;
  - E/S;
  - disco/cinta;
  - interrupciones;
  - tiempos de rutinas del SO;
  - seleccion de procesos.