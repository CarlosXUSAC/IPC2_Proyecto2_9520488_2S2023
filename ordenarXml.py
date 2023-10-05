import xml.etree.ElementTree as ET

def sort_contents_in_sistema_drones(xml_file):
    try:
        # Leer el contenido del archivo XML
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_string = file.read()

        # Crear una instancia de XMLProcessor y ordenar los contenidos en sistemasDrones
        xml_processor = XMLProcessor(xml_string)
        xml_processor.sort_contents_in_sistemas_drones()

        # Obtener el XML procesado con los contenidos ordenados
        xml_result = xml_processor.to_string()

        # Guardar el XML ordenado en un nuevo archivo
        sorted_xml_file = xml_file.replace('.xml', '.xml')
        with open(sorted_xml_file, 'w', encoding='utf-8') as sorted_file:
            sorted_file.write(xml_result)

        print(f'El archivo XML ordenado se ha guardado en {sorted_xml_file}')
    except Exception as e:
        print(f'Ocurrió un error: {str(e)}')

class XMLProcessor:
    def __init__(self, xml_string):
        self.root = ET.fromstring(xml_string)

    def sort_contents_in_sistemas_drones(self):
        lista_sistemas_drones = self.root.find('listaSistemasDrones')
        sistemas_drones = lista_sistemas_drones.findall('sistemaDrones')

        for sistema in sistemas_drones:
            contenidos = sistema.findall('contenido')
            contenidos.sort(key=lambda contenido: contenido.find('dron').text)

            for contenido in contenidos:
                sistema.remove(contenido)

            for contenido in contenidos:
                sistema.append(contenido)

    def to_string(self):
        return ET.tostring(self.root, encoding='UTF-8').decode()

# Nombre del archivo XML desordenado
# xml_file_name = 'entradaV3d.xml'

# Llamar a la función para ordenar el XML y guardar el resultado en un nuevo archivo
# sort_contents_in_sistema_drones(xml_file_name)
