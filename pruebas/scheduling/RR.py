import Proceso
import time

def ejecutar(lista_procesos,q):
    tiempo_inicio = time.time() #guardo el tiempo en que arranca el algoritmo
    lista_espera =[] #declaro lista de espera
    lista_finalizados = [] #declaro lista finalizados
    cpu_ocupado = False #declaro variable booleana para el estado de cpu
    tiempo_en_cpu = 0 #tiempo de un proceso en cpu
    tiempo_ant=0
    ejecucion=lista_procesos[0] #arreglar
    print("ROUND ROBIN")
    print("quantum = ",q)
    
    """"ejecuto el algoritmo mientras haya un elemento en lista de espera
     o por arribar o mientras el cpu este ocupado (ultimo elemento en ejecucion)"""
    while len(lista_procesos)>0 or len(lista_espera)>0 or cpu_ocupado == True:
        cronometro = int(time.time() - tiempo_inicio)
        print("*************\n")
        print("TIEMPO " , cronometro)#voy imprimiendo el tiempo en ejecucion

        if cpu_ocupado:
            ejecucion.set_tiempo_restante(cronometro-tiempo_ant)
            print("En CPU PID ",end='')#proceso que esta en el cpu en este momento
            print(ejecucion)
            print("Tiempo restante: ",end='')
            print(ejecucion.get_tiempo_restante())
        
        print("Lista de Espera: ")#voy imprimiendo la lista de procesos en espera
        if len(lista_espera)>0:
            for proc in lista_espera:
                print(proc)
        else:
            print("Lista de Espera vacia")

        if len(lista_procesos)>0:#si hay algun elemento reviso si arriba un proceso en el tiempo acutal
            #lista_espera.extend(BuscaArribo(lista_procesos,tiempo_inicio))
            if int(lista_procesos[0].get_arribo())<=cronometro:
                lista_espera.append(lista_procesos.pop(0))
        
        if len(lista_espera)>0 and not cpu_ocupado:#cargo un proceso al si hay un elemento en espera y el cpu vacio 
            ejecucion = lista_espera.pop(0)#saco el primer elemento de la lista de espera
            print("Entro al CPU el proceso " , ejecucion.get_procID())
            tiempo_en_cpu = cronometro#guardo el tiempo en que entro
            cpu_ocupado = True
        elif len(lista_espera)==0 and not cpu_ocupado:
            print("lista espera vacia")
        elif cpu_ocupado:
            if ejecucion.get_tiempo_restante()<=0:
                print("Finalizo el proceso PID",ejecucion.get_procID())
                lista_finalizados.append(ejecucion)       
                cpu_ocupado=False         
            elif cronometro-tiempo_en_cpu == q :#si se termino el quantum del cpu
                print("quantum finalizado del proceso")
                print("Se desaloja proceso ",ejecucion.get_procID(), "le quedan ", ejecucion.get_tiempo_restante())
                lista_espera.append(ejecucion) #sino a lista de espera
                cpu_ocupado = False #libero cpu  
        tiempo_ant=time.time()-tiempo_inicio      
        time.sleep(1)#duermo un segundo para simular
    print("******FIN DE SIMULACION******")
    return lista_finalizados

# def BuscaArribo(lista_procesos,tiempo_inicio):#funcion que busca uno o mas procesos que arribaron en el tiempo actual
#     tiempo_actual = int(time.time()-tiempo_inicio)
#     lista_arribados=[]
#     while len(lista_procesos) > 0 and int(lista_procesos[0].get_arribo())==int(tiempo_actual): 
#         lista_arribados.append(lista_procesos.pop(0)) #armo la lista con todos los elementos que arribaron en el tiempo_actual
#     return lista_arribados #devuelvo todos los elementos que arribaron en este tiempo


