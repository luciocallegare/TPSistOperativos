import Proceso
import time
import threading #libreria de hilos
import math

inicio=time.perf_counter() #inicializo el tiempo

def ejecucionProceso(proceso):   #funcion que simula la ejecucion de un proceso en un hilo
    print(f"Ejecutando proceso {proceso.get_procID()} en un hilo...")
    time.sleep(int(proceso.get_tiempo_cpu()))
    fin=time.perf_counter()
    print(f'Proceso {proceso.get_procID()} terminado a los {round(fin-inicio,2)} segundo(s)')

def ejecutar(lista_procesos,cantThreads): #ejecutar los procesos por orden de prioridad
    lista_procesos.sort(key= lambda x:x.get_prioridad()) #ordena la lista de procesos por prioridad
    threads=[] #inicializo una lista de procesos
    i=0
    l=len(lista_procesos)
    n=math.ceil(l/cantThreads) #calcula la cantidad de veces que se itera la lista de procesos
    for _ in range(n):  #la lista se  itera con n que es igual a la cantidad de procesos dividido la cantidad de hilos
        for _ in range(cantThreads):
            if i<l:
                t=threading.Thread(target=ejecucionProceso,args=(lista_procesos[i],))
                t.start()
                threads.append(t)
                i=i+1
            else: #si sobran threads para la iteracion
                break
        for thread in threads:
            thread.join()  #junta los distintos hilos para que terminen juntos

    
