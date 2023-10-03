import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

# Crear el elemento raíz del XML
root2 = ET.Element("Salida")

# Crear el elemento listaMensajes
lista_mensajes = ET.SubElement(root2, "listaMensajes")

# Crear un ejemplo de mensaje
mensaje = ET.SubElement(lista_mensajes, "mensaje", nombre="nombreMensaje")

sistema_drones = ET.SubElement(mensaje, "sistemaDrones")
sistema_drones.text = "[valorAlfanumerico]"

tiempo_optimo = ET.SubElement(mensaje, "tiempoOptimo")
tiempo_optimo.text = "[valorNumerico]"

mensaje_recibido = ET.SubElement(mensaje, "mensajeRecibido")
mensaje_recibido.text = "[valorAlfanumerico]"

instrucciones = ET.SubElement(mensaje, "instrucciones")

# Crear un ejemplo de tiempo y acciones dentro de instrucciones
tiempo = ET.SubElement(instrucciones, "tiempo", valor="valorNumerico")

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
