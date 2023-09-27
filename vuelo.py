import xml.etree.ElementTree as ET
from time import sleep
import sys
import os
from mensaje import Mensaje
from nodoDrones import ListaDrones

# text = "aun me parece gracioso el chavo"
# for c in text:
#     print(c, end='')
#     sys.stdout.flush()
#     sleep(0.5)
tree = ET.parse('entradaV3a.xml')
root = tree.getroot()

cont = 1
cont2 = 0
cont3 = 0   
time = 0.9
reloj = 1
sistema = ListaDrones(None)


mensaje = Mensaje(None)
mensaje.agregar(16)
mensaje.agregar(14)
mensaje.agregar(18)
mensaje.agregar(20)
mensaje.agregar(0)

# tmp = mensaje
# while tmp != None:
#     print(f'(',cont2+1,')  ',tmp.pulso)
#     tmp = tmp.siguiente              
#     cont2 += 1

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
                #print('[ X ]', end='')
            else:
                print('[   ]', end='')
            cont += 1        
        print()
    print("\033[1;34m"+"Relog: [ ", reloj," ]"+'\033[0;m')
    reloj += 1   
    
    sys.stdout.flush()
    sleep(time)
    os.system('cls')

# imprimir(2)
# imprimir2(16)
# imprimir2(15)
# imprimir2(18)
# imprimir(1)
# imprimir2(20)
# imprimir(1)

# print(root[1][0][0].text)
# print(root[1][0][1].text)
# print(root[2][0].get('nombre'))
# print(root[2][0][1].tag)

# V3a
# print(root[1][2][0].tag) 
# print(root[1][2][0].text)
# print(root[1][2][1].tag)
# print(root[1][2][1].text) # Sistema de Drones SDG

# print(root[2][2].get('nombre')) # Mensaje "msg" root[2][0]  "msg2" root[2][1]  "msg3" root[2][2]    "msg4" root[2][3]

n = int(root[1][2][0].text) * int(root[1][2][1].text)
# print(n)


# r = int (root[2][0][1][0].text)
# s = int(root[2][0][1][1].text)
# t = int(root[2][0][1][2].text)
# u = int(root[2][0][1][3].text)

# imprimir(r)
# imprimir2(n-1-r*2)
# imprimir2(n-1-s*2)
# imprimir2(n-1-t)
# x = abs(s-u)
# imprimir(x)
# imprimir2(n-1-u*2)

# imprimir(6)
# imprimir2(105)
# imprimir(2)
# imprimir2(82)
# imprimir2(147)

# imprimir2(124)
# imprimir(3)
# imprimir2(37)
# imprimir2(158)

# imprimir2(111)

# imprimir2(16)
# imprimir2(57)
# imprimir2(130)
# imprimir2(123)

# imprimir2(36)
# imprimir2(109)

# imprimir2(22)
# imprimir2(15)
# imprimir2(88)
# imprimir(2)

# print(root[2][2].get('nombre'))
# print(root[2][2][1][0].text)
# print(root[2].tag)


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

# print(root[2][num][1].tag)
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
        # print(inf, "   ", cont)
        imprimir(cont)
        imprimir2(ref)        
        cont = inf
        cont3 += 1
        
    else:        
        # print(int(tmp.nombre))
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

tmp = sistema
# while tmp != None:
#     for i in range(int(tmp.nombre) - 1):
#         print(tmp.nombre)
#     tmp = tmp.siguiente
        

# while tmp != None:
#     if res < int(tmp.nombre):
#         inf = int(tmp.nombre)
#         res = inf - res - 1
#         print(inf, "   ", res)        
#         res = inf
        
#     else:        
#         print(int(tmp.nombre))
#         res += 1
        
#     if res3 == 8:        
#         res3 = 1
#     tmp = tmp.siguiente