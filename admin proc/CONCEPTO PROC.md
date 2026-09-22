
Primero hay que diferenciar entre lo que esta activo y lo que esta pasivo

El programa es un bloque grande de codigo guardado en memoria

El proceso es el programa  ejecutandose

Un programa puede estar guardado en disco y no estar haciendo nada. Por ejemplo, un archivo ejecutable, un script o una aplicación instalada. Mientras no se ejecuta, es solo instrucciones almacenadas.

Proceso = Programa + Contexto + Recursos + Estado de ejecución

---
La administracion del procesador viene cuando tenemos mas de un proceso que requiere de la cpu para ejecutarse. Son las ditintas maneras de asignar el control de la cpu.

En este caso necesitamos de un mencanismo mediante el cual el SO decide que proceso recibe el control de la CPU. A esto se lo llama SCHEDULING(programar/planificar)

>recordando a fabio y spd, es el entralzamiento pero de procesos, el "pipeline", cada proceso ocupa el procesador por un corto lapaso, en caso de tener dos apps abiertas al mismo tiempo, el procesador hace un poquito de cada una pero para nosotros párece en paralelo.
## THROUGHPUT 
es la cantidad de procesos en el sistema por unidad de tiempo

¿Cuántos procesos consigue procesar/terminar el sistema en determinado tiempo?


## TURNAROUND
es el promedio que puede demorar la ejecucion de un programa pero depende en que tipo de programacion trabajemos

- turnaround en monoprogramacion
	- primero se ejecuta un programa y luego el otro, independientemente si en el medio de cada proceso hallan tiempos de espera desperdiciados.


- en multiprogramacion
	- intercala las ejecuciones aprobechando cada momento en que un proceso esta bloqueado para ejecutar otro en su lugar.