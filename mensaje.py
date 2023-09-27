class Mensaje():    
    pulso = None    
    siguiente = None    


    def __init__(self, pulso):        
        self.pulso = pulso        
        self.siguiente = None

    def agregar(self, pulso):        
        if self.pulso == None:            
            self.pulso = pulso        
        else:            
            tmp = self            
            while tmp.siguiente != None:                
                tmp = tmp.siguiente            
            tmp.siguiente = Mensaje(pulso)

    # def agregar(self, nombre):        
    #     if self.nombre == None:            
    #         self.nombre = nombre        
    #     else:            
    #         tmp = self            
    #         while tmp.siguiente != None:                
    #             tmp = tmp.siguiente            
    #         tmp.siguiente = ListaDrones(nombre)