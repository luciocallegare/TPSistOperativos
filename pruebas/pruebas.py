import time #libreria tiempo
import argparse #libreria parser
import threading #libreria de hilos
from subprocess import call #libreria para funcion limpiar pantalla
import scheduling #modulo de algoritmos
import Proceso #clase Proceso
#from scheduling import FCFS,RR,SJF,Prioridad
from scheduling import FCFS,RR,SJF,Prioridad
call('clear')


parser = argparse.ArgumentParser(description="SIMULADOR DE EJECUCION DE PROCESOS") #se crea el parser
parser.add_argument('-a',metavar='algoritmo',dest='algoritmo',type=str,required=True,choices=['RR','FCFS','SJF','Prioridad'],help="Seleccion tipo de Algoritmo puede ser RR o FCFS")
parser.add_argument('-q',metavar='quantum',dest='q',type=int,help="Indica quantum",default=2)
parser.add_argument('-t',metavar='threads',dest='threads',type=int,help="Indica threads",default=1)

args = parser.parse_args()
print("Algoritmo: ",args.algoritmo) #se imprime el algoritmo ingresado en la linea de comando
print("quantum: ",args.q) #se imprime el algoritmo ingresado en la linea de comando
print("Hilos: ",args.threads) #se imprime el algoritmo ingresado en la linea de comando




for i in range(4):#imprimo unos espacios en blanco
    print()

inicio = time.time() #guardo el tiempo actual

for i in range(1,4):#duermo x segundos
    time.sleep(1)
    print("Segundos ",i)

fin=time.time() #guardo el tiempo actual

print('tiempo transcurrido',int(fin-inicio)) #imprimo el tiempo que estuvo dormido






f = open("procesos.txt","r") #abro archivo

listos=[] #declaro lisa de procesos

def ImprimeProcesos(listos):#funcion que imprime la tabla de procesos
    Tabla = """\
+------------------------------------------+
| PID    Arribo    Prioridad    Tiempo Proc|
|------------------------------------------|
{}
+------------------------------------------+\
"""
    Tabla = (Tabla.format('\n'.join("| {:<8} {:<8} {:>4} {:>14}    |".format(*proceso) for proceso in listos)))
    print (Tabla)
    

def InsertaOrdenado(listos,proceso): #funcion que inserta los procesos ordenados por arribo en la lista de listos
    totalProcesos=int(len(listos))
    for i in range(0,totalProcesos):#voy leyendo toda la lista e inserto ordenado
        if int(listos[i][1])>int(proceso[1]):
            listos.insert(i,proceso)
            break
    else:
        listos.append(proceso)#si es mayor que cualquier elemento en la lista inserto al final

for linea in f: #leo el archivo
    proceso = linea.split(' ')#creo una lista proceso, donde cada elemento es un atributo
    proceso[3]=proceso[3].rstrip()#del ultimo elemento borro el salto de linea \n
    InsertaOrdenado(listos,proceso)#inserto el proceso leido en la lista


ImprimeProcesos(listos)#imprimo la lista ordenada y con formato

def PruebaHilo(tiempo):#funcion para probar hilos
    for i in range(tiempo):
        time.sleep(1)
        print("segundos ",i)

print("PRUEBA DE HILOS")
t1 = threading.Thread(name='hilo1',target=PruebaHilo,args=(2, ))
t2 = threading.Thread(name='hilo2',target=PruebaHilo,args=(5, ))    

t1.start()
t2.start()

lista_procesos=[]#declaro lista de objetos proceso

for proceso in listos:  
    lista_procesos.append(Proceso.Proceso(proceso))#armo la lista de objetos proceso


if args.algoritmo == 'RR': #ejecuto el algoritmo indicado en el parser
    scheduling.RR.ejecutar(lista_procesos,args.q)
elif args.algoritmo == 'FCFS':
    scheduling.FCFS.ejecutar()
elif args.algoritmo == 'SJF':
    scheduling.SJF.ejecutar()
elif args.algoritmo == 'Prioridad': 
    scheduling.Prioridad.ejecutar()

