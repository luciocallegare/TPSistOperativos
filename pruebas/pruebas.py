import time #libreria tiempo
import argparse #libreria parser
import threading #libreria de hilos
from subprocess import call #libreria para funcion limpiar pantalla
import scheduling #modulo de algoritmos
import Proceso #clase Proceso
import Salidas #clase Salidas
from scheduling import FCFS,RR,SJF,Prioridad,PrioridadNew
from operator import itemgetter, attrgetter
call('clear')

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


def Generar_lista():
    lista_procesos = []#declaro lista de procesos
    listos=[] #declaro lisa de procesos
    archivo_procesos = input("Ingrese nombre de archivo: ")#leo el nombre del archivo
    if archivo_procesos == '': #si no ingreso un nombre por defecto es 'procesos.txt'
        archivo_procesos='procesos.txt'
    print('Abriendo archivo:', archivo_procesos)
    f = open(archivo_procesos,"r") #abro archivo
    for linea in f: #leo el archivo
        proceso = linea.split(' ')#creo una lista proceso, donde cada elemento es un atributo
        proceso[3]=proceso[3].rstrip()#del ultimo elemento borro el salto de linea \n
        listos.append(proceso)
    listos = sorted(listos,key=lambda arribo: int(arribo[1])) #ordeno por el segundo elemento de la lista
    for proceso in listos:  
        lista_procesos.append(Proceso.Proceso(proceso))#armo la lista de objetos proceso
    ImprimeProcesos(listos)#imprimo la lista ordenada y con formato
    return lista_procesos

parser = argparse.ArgumentParser(description="SIMULADOR DE EJECUCION DE PROCESOS!") #se crea el parser
parser.add_argument('-a',metavar='algoritmo',dest='algoritmo',type=str,required=True,choices=['RR','FCFS','SJF','Prioridad'],help="Seleccion tipo de Algoritmo puede ser RR o FCFS")
parser.add_argument('-q',metavar='quantum',dest='q',type=int,help="Indica quantum",default=2)
parser.add_argument('-t',metavar='threads',dest='threads',type=int,help="Indica threads",default=1)

args = parser.parse_args()
print("Algoritmo: ",args.algoritmo) #se imprime el algoritmo ingresado en la linea de comando
print("quantum: ",args.q) #se imprime el algoritmo ingresado en la linea de comando
print("Hilos: ",args.threads) #se imprime el algoritmo ingresado en la linea de comando

lista_procesos=Generar_lista() #declaro lista de objetos proceso



if args.algoritmo == 'RR': #ejecuto el algoritmo indicado en el parser
    salidas=scheduling.RR.ejecutar(lista_procesos,args.q)
elif args.algoritmo == 'FCFS':
    scheduling.FCFS.ejecutar(lista_procesos)
elif args.algoritmo == 'SJF':
    scheduling.SJF.ejecutar()
elif args.algoritmo == 'Prioridad': 
    salidas=scheduling.PrioridadNew.ejecutar(lista_procesos,args.threads)

salidas.imprimirEnPantalla()
f=open("salidas.txt","w")
salidas.imprimirEnArchivo(f)
f.close()
