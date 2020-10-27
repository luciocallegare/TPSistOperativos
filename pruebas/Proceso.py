class Proceso(): #clase proceso
    
    def __init__(self,proceso):
        """
        Constructor de Proceso
        """
        self.__procID = proceso[0]
        self.__arribo = proceso[1]
        self.__prioridad = proceso[2]
        self.__tiempo_cpu = proceso[3]
        self.__tiempo_restante = int(proceso[3])
        self.__tiempo_espera = 0
        #variables privadas __


    def imprimir(self):
        """
        Imprime proceso
        """
        print(self.__procID,self.__arribo,self.__prioridad,self.__tiempo_cpu)
    
    def get_procID(self):
        """
        Devuelve tiempo en cpu
        """
        return self.__procID

    def get_arribo(self):
        """
        Devuelve tiempo de arribo
        """
        return self.__arribo

    def get_tiempo_cpu(self):
        """
        Devuelve tiempo en cpu
        """
        return self.__tiempo_cpu

    def get_prioridad(self):
        """
        Devuelve prioridad
        """
        return self.__prioridad
    
    def set_tiempo_restante(self,q):
        """
        Devuelve tiempo restante de ejecucion
        """
        self.__tiempo_restante = int(self.__tiempo_restante - q)

    def get_tiempo_restante(self):
        """
        Devuelve tiempo en cpu
        """
        return self.__tiempo_restante
    
    def __str__(self):
        """
        imprime id objeto
        """
        return str(self.__procID)