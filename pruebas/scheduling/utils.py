import Proceso
import time

def BuscaArribo(lista_procesos,cronometro):#funcion que busca uno o mas procesos que arribaron en el tiempo actual
    lista_arribados=[]
    while len(lista_procesos) > 0 and int(lista_procesos[0].get_arribo())==int(cronometro): 
        nuevo_arribo = lista_procesos.pop(0)
        nuevo_arribo.set_tiempo_arribo(time.time())
        lista_arribados.append(nuevo_arribo) #armo la lista con todos los elementos que arribaron en el tiempo_actual
    return lista_arribados #devuelvo todos los elementos que arribaron en este tiempo

def InformeProceso(proceso):
    pid = proceso.get_procID()
    turnaround = int(proceso.get_tiempo_salida()) - int(proceso.get_tiempo_arribo())
    tiempo_espera = int(turnaround) - int(proceso.get_tiempo_cpu())
    #turnaround
    print("Turnaround = ",turnaround)
    #tiempo espera
    print("Tiempo de Espera = ", tiempo_espera)
    #tiempo espera total (para los casos sin desalojo = tiempo espera)
    print("Tiempo de Espera Total = ", tiempo_espera)
    #tiempo de respuesta
    print("Tiempo de Respuesta = ",int(proceso.get_tiempo_entrada())-int(proceso.get_tiempo_arribo()))
    #tiempo en procesador
    print("Tiempo uso procesador = ",proceso.get_tiempo_cpu())    