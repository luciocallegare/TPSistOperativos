import Proceso
import time
import Salidas
import threading
import queue
from operator import itemgetter, attrgetter
from scheduling import utils

proc_lock = threading.Lock()
cola_listos = queue.PriorityQueue() 
lista_finalizados = []

def ciclo(worker,lista_finalizados) :
    #ciclo en cpu
    tiempo_arribo = worker.get_tiempo_arribo()
    tiempo_ingreso = time.time()
    worker.set_tiempo_entrada(tiempo_ingreso)
    worker.set_tiempo_espera(tiempo_ingreso-tiempo_arribo)
    tiempo_ejecucion = worker.get_tiempo_cpu()
    print("Comienza proceso: ", worker.get_procID())
    while tiempo_ejecucion > 0 :
        tiempo_ejecucion -= 1
        time.sleep(1)            
    with proc_lock :
        print("termino el proceso ",worker.get_procID())
        tiempo_salida = time.time()
        worker.set_tiempo_salida(tiempo_salida)    
        #turnaround
        print("Turnaround = ",int(tiempo_salida-tiempo_arribo))
        #tiempo espera
        print("Tiempo de Espera = ", int(worker.get_tiempo_espera()))
        #tiempo espera total (para los casos sin desalojo = tiempo espera)
        print("Tiempo de Espera Total = ", int(worker.get_tiempo_espera()))
        #tiempo de respuesta
        print("Tiempo de Respuesta = ",int(tiempo_ingreso)-int(worker.get_tiempo_entrada()))
        #tiempo en procesador
        print("Tiempo uso procesador = ",worker.get_tiempo_cpu())

    lista_finalizados.append(worker)


def threader(lista_finalizados):
    while True:
        worker = cola_listos.get()
        ciclo(worker,lista_finalizados)
        cola_listos.task_done()

def Simulacion(lista_procesos):
    tiempo_inicio = time.time() #guardo el tiempo en que arranca el algoritmo
    total_procesos = len(lista_procesos)    
    while len(lista_finalizados) < total_procesos :
        cronometro = int(time.time() - tiempo_inicio)
        print("*************\n")
        print("TIEMPO " , cronometro)#voy imprimiendo el tiempo en ejecucion           
        if len(lista_procesos) > 0 :    
            lista_arribos = utils.BuscaArribo(lista_procesos,cronometro)
            for arribo in lista_arribos:
                print("arribo: ",arribo)
                arribo.set_tiempo_arribo(time.time())
                cola_listos.put((arribo))                  
        
        time.sleep(1)#duermo un segundo para simular


def thread_ejecutar(threads,lista_procesos,lista_finalizados):
    for i in range(threads):
        t=threading.Thread(name='Hilo %s' %i,target=threader,args=(lista_finalizados, ))
        t.daemon = True
        t.start()    
    #ciclo que alimenta la lista a medida que arriban los procesos
    Simulacion(lista_procesos)
    #espera que el thread termine
    cola_listos.join()


def ejecutar(lista_procesos,threads):
    #tiempo de inicio de la simulacion
    inicio_simulacion = time.time()    
    thread_ejecutar(threads,lista_procesos,lista_finalizados)
    #inicializar variables
    sum_turnaround = espera = sum_rta = 0
    espera_individual={}
    tot = len(lista_finalizados)
    #tiempo en que finaliza la ejecucion
    fin_simulacion = time.time()
    #calculo de los valores totales de la ejecucion
    for p in lista_finalizados :
        sum_turnaround += p.get_tiempo_salida() - p.get_tiempo_arribo()
        espera += p.get_tiempo_espera()
        sum_rta += p.get_tiempo_entrada() - p.get_tiempo_arribo()
        espera_individual[p.get_procID()]=p.get_tiempo_espera()

    finalizados_cada_mil = tot * 1000 / int(fin_simulacion-inicio_simulacion)
    
    #se devuelve un objeto salida con la informacion de la simulacion
    return Salidas.Salidas_Threads(sum_turnaround/tot,espera,sum_rta/tot,finalizados_cada_mil,threads,espera_individual)