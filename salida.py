import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

# Crear el elemento raíz del XML
root = ET.Element("Libreria")

# Crear subelementos
libro1 = ET.SubElement(root, "Libro")
titulo1 = ET.SubElement(libro1, "Titulo")
titulo1.text = "El Gran Gatsby"
autor1 = ET.SubElement(libro1, "Autor")
autor1.text = "F. Scott Fitzgerald"

libro2 = ET.SubElement(root, "Libro")
titulo2 = ET.SubElement(libro2, "Titulo")
titulo2.text = "1984"
autor2 = ET.SubElement(libro2, "Autor")
autor2.text = "George Orwell"

# Crear un objeto ElementTree para representar el árbol XML
tree = ET.ElementTree(root)

# Obtener el XML como una cadena con formato
xml_str = ET.tostring(root, encoding="utf-8")
dom = minidom.parseString(xml_str)
formatted_xml = dom.toprettyxml(indent="  ")

# Guardar el archivo XML formateado en el disco
with open("libreria.xml", "w") as xml_file:
    xml_file.write(formatted_xml)

print("Archivo XML generado con formato y saltos de línea.")
