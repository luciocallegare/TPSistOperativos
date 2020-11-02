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
        self.__tiempo_salida = 0
        self.__tiempo_arribo =0 
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
        return int(self.__tiempo_cpu)

    @property #property para que attrgetter funcione y tome el atributo de una getter y pueda ordenar
    def get_prioridad(self):
        """
        Devuelve prioridad
        """
        return int(self.__prioridad)
    
    def get_tiempo_salida(self):
        """
        Devuelve tiempo salida
        """
        return int(self.__tiempo_salida)
    
    def get_tiempo_arribo(self):
        """
        Devuelve tiempo arribo
        """
        return int(self.__tiempo_arribo)
    
    def set_tiempo_restante(self,q):
        """
        Setea tiempo restante de ejecucion
        """
        self.__tiempo_restante = int(self.__tiempo_restante - q)

    def set_tiempo_salida(self,tiempo):
        """
        Setea tiempo de salida
        """
        self.__tiempo_salida = int(tiempo)
    
    def set_tiempo_arribo(self,tiempo):
        """
        Setea tiempo de arribo
        """
        self.__tiempo_arribo = int(tiempo)

    def get_tiempo_restante(self):
        """
        Devuelve tiempo en cpu
        """
        return self.__tiempo_restante
    
    def __str__(self): #metodo sobrecargado para funcion print de objetos
        """
        imprime id objeto
        """
        return str(self.__procID)
    
    def __gt__(self,proceso): #greater
        return int(self.__prioridad)<int(proceso.__prioridad)

    def __cmp__(self, other): #comparador para funcion sort por prioridad
        if self.__prioridad == other.__prioridad:
            return 1 if self.__arribo > other.__arribo else -1
        elif self.__prioridad < other__prioridad:
            return -1
        else:
            return 1

    def __lt__(self,other): #smaller, metodos magicos python para ordenamiento
        return self.__prioridad<other.__prioridad
    
    