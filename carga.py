import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import graphviz as gv
from nodoDrones import ListaDrones

tree = ET.parse('entradaV3.xml')
root = tree.getroot()

cont = 0
cont2 = 0
orden = ListaDrones(None)


print("Drones:")
print("..................................................")
for dron in root[0].findall('dron'):    
    print(f'(',cont+1,')  ',root[0][cont].text)
    orden.agregar(root[0][cont].text)
        
    cont += 1
print("..................................................")
num = int(input("Ingrese el numero del Dron que desea procesar: "))
num -= 1    
print("")

# tmp = orden
# while tmp != None:
#     print("Dron: ",tmp.nombre)
#     tmp = tmp.siguiente
    

ListaDrones.ordenar(orden)

print("Drones:")
print("..................................................")
tmp = orden
while tmp != None:
    print(f'(',cont2+1,')  ',tmp.nombre)
    tmp = tmp.siguiente              
    cont2 += 1
print("..................................................")


tree = ET.ElementTree(root)
xml_str = ET.tostring(root, encoding="utf-8")
dom = minidom.parseString(xml_str)
formatted_xml = dom.toprettyxml(indent="  ")

with open("libreria.xml", "w") as xml_file:
    xml_file.write(formatted_xml)
