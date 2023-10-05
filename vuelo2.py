import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from time import sleep
import sys
import os
from mensaje import Mensaje
from dronesSalida import Salida
from nodoDrones import ListaDrones

class SistemaDrones:
    def __init__(self):
        self.tree = ET.parse('entradaV3a.xml')
        self.root = self.tree.getroot()
        self.cont = 1
        self.cont2 = 0
        self.cont3 = 0
        self.time = 0.2
        self.reloj = 1
        self.sistema = ListaDrones(None)
        self.salidaD = Salida(None, None)
        self.mensaje = Mensaje(None)
        os.system('cls')

    def imprimir(self, t):
        times = t
        for k in range(times):
            for j in range(20):
                for i in range(8):
                    print('[   ]', end='')
                print()
            print("\033[1;34m" + "Reloj: [ ", self.reloj, " ]" + '\033[0;m')
            self.reloj += 1
            sys.stdout.flush()
            sleep(self.time)
            os.system('cls')

    def imprimir2(self, r):
        cont = 1
        for j in range(20):
            for i in range(8):
                if r == cont:
                    print("\033[0;33m" + "[ █ ]" + '\033[0;m', end='')  # 1;32m Azul 1;31m Rojo 1;34m light blue
                else:
                    print('[   ]', end='')
                cont += 1
            print()
        print("\033[1;34m" + "Reloj: [ ", self.reloj, " ]" + '\033[0;m')
        self.reloj += 1
        sys.stdout.flush()
        sleep(self.time)
        os.system('cls')

    def procesar_mensajes(self):
        print("Sistema de Drones:")
        print("..................................................")
        for sistemaDrones in self.root[1]:
            print(f'(', self.cont3 + 1, ')  ', self.root[1][self.cont3].get('nombre'))
            self.cont3 += 1
        print("..................................................")
        num2 = int(input("Ingrese el numero del Sistema que desea utilizar: "))
        num2 -= 1
        print("")
        self.cont3 = 0
        sistemaD = self.root[1][self.cont3].get('nombre')

        print("Mensajes:")
        print("..................................................")
        for mensaje in self.root[2]:
            print(f'(', self.cont3 + 1, ')  ', self.root[2][self.cont3].get('nombre'))
            self.cont3 += 1
        print("..................................................")
        num = int(input("Ingrese el numero de Mensaje que desea procesar: "))
        num -= 1
        print("")
        self.cont3 = 0

        print("Mensaje: ", self.root[2][num].get('nombre'))
        print("..................................................")
        for instruccion in self.root[2][num][1]:
            print(f'(', self.cont3 + 1, ')...', self.root[2][num][1][self.cont3].get('dron'), self.root[2][num][1][self.cont3].text)
            self.sistema.agregar(self.root[2][num][1][self.cont3].text)
            self.cont3 += 1
        print("..................................................\n")

        os.system('cls')

        self.cont = 0
        self.cont2 = 0
        self.cont3 = 1
        self.cont4 = 1
        print("Mensaje:")
        print("..................................................")

        os.system('cls')
        print("XML")

        text = ''
        self.cont5 = 2
        tmp = self.sistema
        while tmp != None:
            if self.cont < int(tmp.nombre):
                inf = int(tmp.nombre)
                self.cont = inf - self.cont - 1
                ref = 8 * (20 - inf) + self.cont3
                text = text + self.root[1][2][self.cont5][1][inf - 1].text
                self.salidaD.agregar(self.root[1][2][self.cont5][0].text, inf)
                self.imprimir(self.cont)
                self.imprimir2(ref)
                self.cont = inf
                self.cont3 += 1
                self.cont5 += 1
            else:
                inf = int(tmp.nombre)
                ref = 8 * (20 - inf) + self.cont3
                text = text + self.root[1][2][self.cont5][1][inf - 1].text
                self.salidaD.agregar(self.root[1][2][self.cont5][0].text, inf)
                self.imprimir2(ref)
                self.cont += 1
                self.cont3 += 1
                self.cont5 += 1
            if self.cont3 > 8:
                self.cont3 = 1
            if self.cont5 > 9:
                self.cont5 = 2
            tmp = tmp.siguiente

        self.imprimir(2)

        print("..................................................")

        tiempoO = str(self.reloj - 3)
        nombre = self.root[2][num].get('nombre')

        root2 = ET.Element("Salida")

        lista_mensajes = ET.SubElement(root2, "listaMensajes")

        # Crear un ejemplo de mensaje
        mensaje = ET.SubElement(lista_mensajes, "mensaje", nombre = nombre)

        sistema_drones = ET.SubElement(mensaje, "sistemaDrones")
        sistema_drones.text = sistemaD

        tiempo_optimo = ET.SubElement(mensaje, "tiempoOptimo")
        tiempo_optimo.text = tiempoO

        mensaje_recibido = ET.SubElement(mensaje, "mensajeRecibido")
        mensaje_recibido.text = text

        instrucciones = ET.SubElement(mensaje, "instrucciones")

        
        tmp = self.salidaD
        tmp = tmp.siguiente
        while tmp != None:

            tiempo = ET.SubElement(instrucciones, "tiempo", valor = "tiempo")

            acciones = ET.SubElement(tiempo, "acciones")

            time = str(tmp.valor)
            dron = ET.SubElement(acciones, "dron", nombre = time)
            dron.text = tmp.nombre
            tmp = tmp.siguiente


        # Crear un objeto ElementTree para representar el árbol XML
        tree = ET.ElementTree(root2)

        # Obtener el XML como una cadena con formato
        xml_str = ET.tostring(root2, encoding="utf-8")
        dom = minidom.parseString(xml_str)
        formatted_xml = dom.toprettyxml(indent="  ")

        # Guardar el archivo XML formateado en el disco
        with open("Salida.xml", "w") as xml_file:
            xml_file.write(formatted_xml)

        print("Archivo XML generado con la estructura deseada.")

if __name__ == "__main__":
    sistema_drones = SistemaDrones()
    sistema_drones.procesar_mensajes()
