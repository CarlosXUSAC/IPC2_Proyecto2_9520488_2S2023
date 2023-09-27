import graphviz
import os
from dataclasses import dataclass



@dataclass
class Drone():
    estado: bool    
    alto: int    
    next: None
    back: None


class Columna():
    largo = int
    primerDrone = Drone
        

    def __init__(self):
        self.largo = 0
        self.primerDrone = None

    
    def insertar(self, alto):
        nuevo = Drone()
        nuevo.alto = alto
        if self.primerDrone == None:
            self.primerDrone = nuevo
        else:
            actual = self.primerDrone
            while actual.next != None:
                actual = actual.next
            actual.next = nuevo
            nuevo.back = actual
        self.largo += 1

class Tablero():
    ancho = int
    first = Columna

    def __init__(self):
        self.ancho = 0
        self.first = None





