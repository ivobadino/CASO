
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
- [[Concepto de proceso]].
- [[Programa vs proceso]].
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