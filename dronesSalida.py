class Salida():    
    nombre = None
    valor = None    
    siguiente = None    


    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
        self.siguiente = None

    def agregar(self, nombre, valor):
        tmp = self
        while tmp.siguiente != None:
            tmp = tmp.siguiente
        tmp.siguiente = Salida(nombre, valor)