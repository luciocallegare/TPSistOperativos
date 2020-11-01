import Proceso
import time
import threading
from operator import itemgetter, attrgetter
from scheduling import aux

def ejecutar(lista_procesos,threads):
    lista_espera =[] #declaro lista de espera
    lista_hilos=[] #declaro lista de hilos
    lista_finalizados = [] #declaro lista finalizados
    for i in range(0,threads): #genero lista de threads de acuerdo al parametro recibido en el parser
        lista_hilos.append(threading.Thread(name='Hilo %s' %i,target=ciclo,args=(lista_procesos,lista_espera,lista_finalizados, )))
    for i in range(0,threads): #ejecuto cada hilo de la lista de hilos
            lista_hilos[i].start()

def ciclo(lista_procesos,lista_espera,lista_finalizados):
    tiempo_inicio = time.time() #guardo el tiempo en que arranca el algoritmo
    cpu_ocupado = False #declaro variable booleana para el estado de cpu
    tiempo_en_cpu = 0 #tiempo de un proceso en cpu
    ejecucion=[]#elemento en ejecucion
    tiempo_de_procesador = 0 #timepo que lleva ejecutado un proceso en el cpu
    tiempo_ingreso_cpu = 0 #tiempo en que ingresa en el cpu
        
    #ejecuto el algoritmo mientras haya un elemento en lista de espera
    #o por arribar o mientras el cpu este ocupado (ultimo elemento en ejecucion)
    while len(lista_procesos)>0 or len(lista_espera)>0 or cpu_ocupado == True:
        cronometro = int(time.time() - tiempo_inicio)
        print("*************\n")
        print("TIEMPO " , cronometro)#voy imprimiendo el tiempo en ejecucion
        
        if len(lista_procesos)>0:#si hay algun elemento reviso si arriba un proceso en el tiempo acutal
            lista_espera.extend(aux.BuscaArribo(lista_procesos,cronometro))
            lista_espera.sort() #metodo __cmp__ sobrecargado
            #lista2=sorted(lista_procesos,key=attrgetter('get_prioridad'))#ordenar por prioridad

        print("Lista de Espera: ")#voy imprimiendo la lista de procesos en espera
        for proc in lista_espera:
            print(proc)        
        
        if len(lista_espera)>0 and not cpu_ocupado:#cargo un proceso al cpu si hay un elemento en espera y el cpu vacio 
            ejecucion = lista_espera.pop(0)#saco el primer elemento de la lista de espera
            print("Entro al CPU el proceso " , ejecucion.get_procID()) #indico quien entro
            tiempo_ingreso_cpu = time.time() #guardo el tiempo que ingresa al cpu
            cpu_ocupado = True
            tiempo_de_procesador = ejecucion.get_tiempo_cpu() #traigo el tiempo del proceso que entra en el cpu
        elif len(lista_espera)==0:
            print("lista espera vacia")
        
        if int(tiempo_de_procesador) ==  int(time.time() - tiempo_ingreso_cpu) :#si el tiempo en procesador termino
            print("tiempo en procesador finalizado")
            if cpu_ocupado == True:
                if ejecucion.get_tiempo_restante() <= 0 :#si finalizo el proceso, lo envio a lista de finalizados
                    print("Finalizo el proceso PID",ejecucion.get_procID())
                    lista_finalizados.append(ejecucion)
                cpu_ocupado = False #libero cpu
            
            elif len(lista_espera) > 0: #si hay elementos en la lista de espera, lo cargo en cpu
                lista_espera.append(ejecucion)
                tiempo_en_cpu = time.time()
                cpu_ocupado = True #cpu ocupado
            else:
                tiempo_en_cpu = time.time()        
        
        Mostrar_estado_CPU(cpu_ocupado,ejecucion)
        time.sleep(1)#duermo un segundo para simular

def Chequear_tiempo_en_cpu(tiempo_de_procesador,tiempo_ingreso_cpu,cpu_ocupado,ejecucion,lista_finalizados,lista_espera)

def Mostrar_estado_CPU(cpu_ocupado,ejecucion):
    if cpu_ocupado == True:
        print("En CPU PID ",end='')#proceso que esta en el cpu en este momento
        print(ejecucion)
        nombre_hilo=threading.currentThread().getName()
        print(' ejecutando en %s' %nombre_hilo)
    else:
        print("CPU vacio")
