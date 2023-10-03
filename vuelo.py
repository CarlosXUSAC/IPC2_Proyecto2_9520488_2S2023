import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from time import sleep
import sys
import os
from mensaje import Mensaje
from nodoDrones import ListaDrones


tree = ET.parse('entradaV3a.xml')
root = tree.getroot()

cont = 1
cont2 = 0
cont3 = 0   
time = 0.2
reloj = 1
sistema = ListaDrones(None)


mensaje = Mensaje(None)
# mensaje.agregar(16)
# mensaje.agregar(14)
# mensaje.agregar(18)
# mensaje.agregar(20)
# mensaje.agregar(0)


os.system('cls')

def imprimir(self):
    times = self
    global time
    global reloj  
    for k in range(times):
        for j in range(20):
            for i in range(8):
                print('[   ]', end='')        
            print()
        print("\033[1;34m"+"Relog: [ ", reloj," ]"+'\033[0;m')
        reloj += 1    
    
        sys.stdout.flush()
        sleep(time)
        os.system('cls')

def imprimir2(self):
    r = self
    cont = 1
    global reloj
    global time 
    for j in range(20):
        for i in range(8):
            if r == cont:
                print("\033[0;33m"+"[ █ ]"+'\033[0;m', end='')  # 1;32m Azul 1;31m Rojo 1;34m light blue                
            else:
                print('[   ]', end='')
            cont += 1        
        print()
    print("\033[1;34m"+"Relog: [ ", reloj," ]"+'\033[0;m')
    reloj += 1   
    
    sys.stdout.flush()
    sleep(time)
    os.system('cls')


# n = int(root[1][2][0].text) * int(root[1][2][1].text)


print("Sistema de Drones:")
print("..................................................")
for sistemaDrones in root[1]:
    print(f'(',cont3+1,')  ',root[1][cont3].get('nombre'))
    cont3 += 1
print("..................................................")
num2 = int(input("Ingrese el numero del Sistema que desea utilizar: "))
num2 -= 1    
print("")
cont3 = 0


print("Mensajes:")
print("..................................................")
for Mensaje in root[2]:
    print(f'(',cont3+1,')  ',root[2][cont3].get('nombre'))
    cont3 += 1
print("..................................................")
num = int(input("Ingrese el numero de Mensaje que desea procesar: "))
num -= 1    
print("")
cont3 = 0

print("Mensaje: ",root[2][num].get('nombre'))
print("..................................................")
for instruccion in root[2][num][1]:
    print(f'(',cont3+1,')...', root[2][num][1][cont3].get('dron') ,root[2][num][1][cont3].text)
    sistema.agregar(root[2][num][1][cont3].text) 
    cont3 += 1
print("..................................................\n")


os.system('cls')

cont = 0
cont2 = 0
cont3 = 1
cont4 = 1
print("Mensaje:")
print("..................................................")

os.system('cls')

tmp = sistema
while tmp != None:
    if cont < int(tmp.nombre):
        inf = int(tmp.nombre)
        cont = inf - cont - 1
        ref = 8 * (20 - inf) + cont3        
        imprimir(cont)
        imprimir2(ref)        
        cont = inf
        cont3 += 1
        
    else:                
        inf = int(tmp.nombre)
        ref = 8 * (20 - inf) + cont3
        imprimir2(ref)        
        cont += 1
        cont3 += 1
        
    if cont3 > 8:        
        cont3 = 1
    tmp = tmp.siguiente

imprimir(2)   

print("..................................................")


tiempoO = str(reloj - 3)
nombre = (root[2][num].get('nombre'))


# Crear el elemento raíz del XML
root2 = ET.Element("Salida")

# Crear el elemento listaMensajes
lista_mensajes = ET.SubElement(root2, "listaMensajes")

# Crear un ejemplo de mensaje
mensaje = ET.SubElement(lista_mensajes, "mensaje", nombre = nombre)

sistema_drones = ET.SubElement(mensaje, "sistemaDrones")
sistema_drones.text = "[valorAlfanumerico]"

tiempo_optimo = ET.SubElement(mensaje, "tiempoOptimo")
tiempo_optimo.text = "[valorNumerico]"

mensaje_recibido = ET.SubElement(mensaje, "mensajeRecibido")
mensaje_recibido.text = "[valorAlfanumerico]"

instrucciones = ET.SubElement(mensaje, "instrucciones")

# Crear un ejemplo de tiempo y acciones dentro de instrucciones
tiempo = ET.SubElement(instrucciones, "tiempo", valor = tiempoO)

acciones = ET.SubElement(tiempo, "acciones")

dron = ET.SubElement(acciones, "dron", nombre="valorAlfanumerico")
dron.text = "[valorAccionDron]"

# Puedes agregar más mensajes, tiempos y acciones según sea necesario

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