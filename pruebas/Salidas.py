class Salidas():
    def __init__(self,turnaround,espera_tot,rta,cadaMil,espera):
        self.tiempo_espera={}
        self.tiempo_turnaround=round(turnaround,2)
        self.tiempo_espera=espera
        self.espera_tot=espera_tot
        self.tiempo_rta=round(rta,2)
        self.finalizados_1000=round(cadaMil,2)
    
    def imprimirEnPantalla(self):
        print("*******************************")
        print("Informacion sobre la ejecucion:")
        print("*******************************")
        print("Tiempo de turnaround promedio: ",self.tiempo_turnaround)
        print("Tiempo de Espera total para cada proceso: ")
        for proc in self.tiempo_espera.keys():
            print("\tProceso "+proc+": "+str(self.tiempo_espera[proc]))
        print("Tiempo de espera total",self.espera_tot)
        print("Tiempo de Respuesta promedio: ",self.tiempo_rta)
        print("Cantidad de procesos finalizados cada 1000 segundos: ",self.finalizados_1000)
    
    def imprimirEnArchivo(self,f):
        f.write("Tiempo de turnaround promedio: "+str(self.tiempo_turnaround)+'\n')
        f.write("Tiempo de Espera total para cada proceso:\n")
        for proc in self.tiempo_espera.keys():
            f.write("\tProceso "+proc+": "+str(self.tiempo_espera[proc])+'\n')
        f.write("Tiempo de espera total: "+str(self.espera_tot)+'\n')
        f.write("Tiempo de Respuesta promedio: "+str(self.tiempo_rta)+'\n')
        f.write("Cantidad de procesos finalizados cada 1000 segundos: "+str(self.finalizados_1000))

class Salidas_Threads(Salidas):
    def __init__(self,turnaround,espera_tot,rta,cadaMil,threads,espera):
        super().__init__(turnaround,espera_tot,rta,cadaMil,espera)
        self.threads=threads
    
    def setThreads(self,t):
        self.threads=t
    
    
    def imprimirEnPantalla(self):
        super().imprimirEnPantalla()
        print("Cantidad de threads utilizados: ",self.threads)

    def imprimirEnArchivo(self,f):
        super().imprimirEnArchivo(f)
        f.write("Cantidad de threads utilizados: "+str(self.threads))
        
