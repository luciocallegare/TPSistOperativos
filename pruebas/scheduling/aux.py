

def BuscaArribo(lista_procesos,cronometro):#funcion que busca uno o mas procesos que arribaron en el tiempo actual
    
    lista_arribados=[]
    while len(lista_procesos) > 0 and int(lista_procesos[0].get_arribo())==int(cronometro): 
        lista_arribados.append(lista_procesos.pop(0)) #armo la lista con todos los elementos que arribaron en el tiempo_actual
    return lista_arribados #devuelvo todos los elementos que arribaron en este tiempo
