import Proceso
import time

def ejecutar(lista_procesos,q):
    tiempo_inicio = time.time() #guardo el tiempo en que arranca el algoritmo
    lista_espera =[] #declaro lista de espera
    lista_finalizados = [] #declaro lista finalizados
    cpu_ocupado = False #declaro variable booleana para el estado de cpu
    tiempo_en_cpu = 0 #tiempo de un proceso en cpu
    ejecucion=lista_procesos[0]#le cargo el primer elemento porque no podia poner uno vacio (arreglar)
    print("ROUND ROBIN")
    print("q = ",q)
    
    """"ejecuto el algoritmo mientras haya un elemento en lista de espera
     o por arribar o mientras el cpu este ocupado (ultimo elemento en ejecucion)"""
    while len(lista_procesos)>0 or len(lista_espera)>0 or cpu_ocupado == True:
        cronometro = int(time.time() - tiempo_inicio)
        print("*************\n")
        print("TIEMPO " , cronometro)#voy imprimiendo el tiempo en ejecucion
        
        print("Lista de Espera: ")#voy imprimiendo la lista de procesos en espera
        for proc in lista_espera:
            print(proc)

        if len(lista_procesos)>0:#si hay algun elemento reviso si arriba un proceso en el tiempo acutal
            lista_espera.extend(BuscaArribo(lista_procesos,tiempo_inicio))
        
        if len(lista_espera)>0 and not cpu_ocupado:#cargo un proceso al si hay un elemento en espera y el cpu vacio 
            ejecucion = lista_espera.pop(0)#saco el primer elemento de la lista de espera
            print("Entro al CPU el proceso " , ejecucion.get_procID())
            tiempo_en_cpu = time.time()#guardo el tiempo en que entro
            cpu_ocupado = True
        elif len(lista_espera)==0:
            print("lista espera vacia")
        
        if int(time.time() - tiempo_en_cpu) == q:#si se termino el quantum del cpu
            print("quantum finalizado del procesor")
            if cpu_ocupado == True:
                ejecucion.set_tiempo_restante(q)#resto el quantum tiempo de ejecucion del proceso
                print("Se desaloja proceso ",ejecucion.get_procID(), "le quedan ", ejecucion.get_tiempo_restante())
                if ejecucion.get_tiempo_restante() <= 0 :#si finalizo el proceso, lo envio a lista de finalizados
                    print("Finalizo el proceso PID",ejecucion.get_procID())
                    lista_finalizados.append(ejecucion)
                else:
                    lista_espera.append(ejecucion) #sino a lista de espera
                cpu_ocupado = False #libero cpu
            elif len(lista_espera) > 0: #si hay elementos en la lista de espera, lo cargo en cpu
                lista_espera.append(ejecucion)
                tiempo_en_cpu = time.time()
                cpu_ocupado = True #cpu ocupado
            else:
                cpu_ocupado = False
                tiempo_en_cpu = time.time()
        print("En CPU PID ",end='')#proceso que esta en el cpu en este momento
        print(ejecucion)
        time.sleep(1)#duermo un segundo para simular

def BuscaArribo(lista_procesos,tiempo_inicio):#funcion que busca uno o mas procesos que arribaron en el tiempo actual
    tiempo_actual = int(time.time()-tiempo_inicio)
    lista_arribados=[]
    while len(lista_procesos) > 0 and int(lista_procesos[0].get_arribo())==int(tiempo_actual): 
        lista_arribados.append(lista_procesos.pop(0)) #armo la lista con todos los elementos que arribaron en el tiempo_actual
    return lista_arribados #devuelvo todos los elementos que arribaron en este tiempo