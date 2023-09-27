class ListaDrones():    
    nombre = None    
    siguiente = None    


    def __init__(self, nombre):        
        self.nombre = nombre        
        self.siguiente = None

    def agregar(self, nombre):        
        if self.nombre == None:            
            self.nombre = nombre        
        else:            
            tmp = self            
            while tmp.siguiente != None:                
                tmp = tmp.siguiente            
            tmp.siguiente = ListaDrones(nombre)

    def ordenar(self):
        tmp = self            
        while tmp.siguiente != None:            
            tmp2 = tmp.siguiente            
            while tmp2 != None:                
                if tmp.nombre > tmp2.nombre:                    
                    aux = tmp.nombre                    
                    tmp.nombre = tmp2.nombre                    
                    tmp2.nombre = aux                
                tmp2 = tmp2.siguiente            
            tmp = tmp.siguiente