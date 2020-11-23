import time
import Proceso
import Salidas
from operator import itemgetter, attrgetter
from scheduling import utils

def ejecutar(lista_procesos):
    lista_espera =[] #declaro lista de espera
    lista_hilos=[] #declaro lista de hilos
    lista_finalizados = [] #declaro lista finalizados
    tiempo_inicio = time.time() #guardo el tiempo en que arranca el algoritmo
    cpu_ocupado = False #declaro variable booleana para el estado de cpu
    tiempo_en_cpu = 0 #tiempo de un proceso en cpu
    ejecucion=[]#elemento en ejecucion
    tiempo_de_procesador = 0 #tiempo que lleva ejecutado un proceso en el cpu
    tiempo_ingreso_cpu = 0 #tiempo en que ingresa en el cpu
    sum_turnaround=espera_tot=sum_rta=0
    espera={}
    print("FCFS")
    while len(lista_procesos)>0 or len(lista_espera)>0 or cpu_ocupado == True:
        cronometro = int(time.time() - tiempo_inicio)
        print("*************\n")
        print("TIEMPO " , cronometro)#voy imprimiendo el tiempo en ejecucion

        if len(lista_procesos)>0:#si hay algun elemento reviso si arriba un proceso en el tiempo acutal
            lista_espera.extend(utils.BuscaArribo(lista_procesos,cronometro))

        if int(tiempo_de_procesador) ==  int(time.time() - tiempo_ingreso_cpu) :#si el tiempo en procesador termino
            print("Finalizo el proceso PID",ejecucion.get_procID())
            ejecucion.set_tiempo_salida(time.time())
            utils.InformeProceso(ejecucion)
            lista_finalizados.append(ejecucion)
            cpu_ocupado = False #libero cpu
        
        print("Lista de Espera: ")#voy imprimiendo la lista de procesos en espera
        for proc in lista_espera:
            print(proc)        
        
        if len(lista_espera)>0 and not cpu_ocupado:#cargo un proceso al cpu si hay un elemento en espera y el cpu vacio 
            ejecucion = lista_espera.pop(0)#saco el primer elemento de la lista de espera
            print("Entro al CPU el proceso " , ejecucion.get_procID()) #indico quien entro
            tiempo_ingreso_cpu = time.time() #guardo el tiempo que ingresa al cpu
            ejecucion.set_tiempo_entrada(tiempo_ingreso_cpu)
            ejecucion.set_tiempo_espera(tiempo_ingreso_cpu-ejecucion.get_tiempo_arribo())
            cpu_ocupado = True
            tiempo_de_procesador = ejecucion.get_tiempo_cpu() #traigo el tiempo del proceso que entra en el cpu
        elif len(lista_espera)==0:
            print("lista espera vacia")       
        
        Mostrar_estado_CPU(cpu_ocupado,ejecucion)
        time.sleep(1)#duermo un segundo para simular
    tot=len(lista_finalizados)
    for p in lista_finalizados:
        sum_turnaround += p.get_tiempo_salida() - p.get_tiempo_arribo()
        espera_tot += p.get_tiempo_espera()
        sum_rta += p.get_tiempo_entrada() - p.get_tiempo_arribo()
        espera[p.get_procID()]=p.get_tiempo_espera()

    return Salidas.Salidas(sum_turnaround/tot,espera_tot,sum_rta/tot,tot*1000/cronometro,espera)




def Mostrar_estado_CPU(cpu_ocupado,ejecucion):
    if cpu_ocupado == True:
        print("En CPU PID ",end='')#proceso que esta en el cpu en este momento
        print(ejecucion)
    else:
        print("CPU vacio")
         