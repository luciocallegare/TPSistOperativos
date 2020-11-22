class Salidas():
    def __init__(self,turnaround,espera,rta,cadaMil):
        self.tiempo_turnaround=turnaround
        self.tiempo_espera=espera
        self.tiempo_rta=rta
        self.finalizados_1000=cadaMil
    
    def imprimirEnPantalla(self):
        print("Informacion sobre la ejecucion:")
        print("Tiempo de turnaround promedio: ",self.tiempo_turnaround)
        print("Tiempo de Espera total: ",self.tiempo_espera)
        print("Tiempo de Respuesta promedio: ",self.tiempo_rta)
        print("Cantidad de procesos finalizados cada 1000 segundos: ",self.finalizados_1000)
    
    def imprimirEnArchivo(self,f):
        f.write("Tiempo de turnaround promedio: "+str(self.tiempo_turnaround)+'\n')
        f.write("Tiempo de Espera total: "+str(self.tiempo_espera)+'\n')
        f.write("Tiempo de Respuesta promedio: "+str(self.tiempo_rta)+'\n')
        f.write("Cantidad de procesos finalizados cada 1000 segundos: "+str(self.finalizados_1000))

class Salidas_Threads(Salidas):
    def __init__(self,turnaround,espera,rta,cadaMil,threads):
        super().__init__(turnaround,espera,rta,cadaMil)
        self.threads=threads
    
    def setThreads(self,t):
        self.threads=t
    
    
    def imprimirEnPantalla(self):
        super().imprimirEnPantalla()
        print("Cantidad de threads utilizados: ",self.threads)

    def imprimirEnArchivo(self,f):
        super().imprimirEnArchivo(f)
        f.write("Cantidad de threads utilizados: "+str(self.threads))
        
