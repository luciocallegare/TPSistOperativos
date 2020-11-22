import Proceso
import time
import threading
import queue
from operator import itemgetter, attrgetter
from scheduling import utils

proc_lock = threading.Lock()
cola_listos = queue.PriorityQueue() 


def ciclo(worker,lista_finalizados) :
    #ciclo en cpu
    tiempo_ingreso = time.time()
    worker.set_tiempo_arribo(tiempo_ingreso)
    tiempo_ejecucion = worker.get_tiempo_cpu()
    print("Comienza proceso: ", worker.get_procID())
    while tiempo_ejecucion > 0 :
        tiempo_ejecucion -= 1
        time.sleep(1)            
    print("termino el proceso ",worker.get_procID())
    tiempo_salida = time.time()
    worker.set_tiempo_salida(tiempo_salida)    
    worker.set_tiempo_espera = tiempo_salida - tiempo_ingreso
    lista_finalizados.append(worker)
    


def threader(lista_finalizados):
    while True:
        worker = cola_listos.get()
        ciclo(worker,lista_finalizados)
        cola_listos.task_done()

def Simulacion(lista_procesos):
    tiempo_inicio = time.time() #guardo el tiempo en que arranca el algoritmo
        
    #ejecuto el algoritmo mientras haya un elemento en lista de espera
    #o por arribar o mientras el cpu este ocupado (ultimo elemento en ejecucion)
    while len(lista_procesos)>0 or cola_listos.qsize() > 0 :
        cronometro = int(time.time() - tiempo_inicio)
        print("*************\n")
        print("TIEMPO " , cronometro)#voy imprimiendo el tiempo en ejecucion
                   
        lista_arribos = utils.BuscaArribo(lista_procesos,cronometro)
        for arribo in lista_arribos:
            #prioridad = arribo.get_prioridad()
            print("arribo: ",arribo)
            cola_listos.put((arribo))
            print("largo cola listos ",cola_listos.qsize())                  
        
        time.sleep(1)#duermo un segundo para simular


def thread_ejecutar(threads,lista_procesos,lista_finalizados):
    for i in range(threads):
        t=threading.Thread(name='Hilo %s' %i,target=threader,args=(lista_finalizados, ))
        t.daemon = True
        t.start()
    
    #ciclo que alimenta la lista a medida que llegan
    Simulacion(lista_procesos)
    #espera que el thread termine
    cola_listos.join()


def ejecutar(lista_procesos,threads):
    lista_espera = []
    lista_finalizados = []
    thread_ejecutar(threads,lista_procesos,lista_finalizados)