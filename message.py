import tkinter as tk
from tkinter import scrolledtext
import xml.etree.ElementTree as ET
from vuelo2 import SistemaDrones
from ordenarXml import sort_contents_in_sistema_drones


class Mesage:
    def __init__(self, nombre_archivo):
        self.ventana = tk.Tk()
        self.ventana.title("Mensaje")
        self.ventana.iconbitmap('Usac_logo.ico')
        self.ventana.geometry("600x600")
        self.ventana['bg'] = '#CF91DA'
        self.sistema_drones = SistemaDrones()
       
        self.etiqueta = tk.Label(self.ventana, bg= '#CF91DA')
        self.etiqueta.grid(column=0, row=0)        
        self.etiqueta = tk.Label(self.ventana, bg= '#CF91DA', padx = 13)
        self.etiqueta.grid(column=0, row=1)

        # self.etiqueta_archivo = tk.Label(self.ventana, text="Archivo XML:", bg= '#CF91DA')
        # self.etiqueta_archivo.grid(column=1, row=1)
        
        self.entrada_archivo = tk.Entry(self.ventana)
        self.entrada_archivo.grid(column=1, row=1)
        self.entrada_archivo.insert(tk.END, nombre_archivo)
        
        # Botón para cargar el archivo XML
        self.boton_cargar = tk.Button(self.ventana, text="Cargar XML", command = self.mostrar_xml)
        self.boton_cargar.grid(column=2, row=1)
        
        # Botón para Simular Mensaje
        self.boton_simular = tk.Button(self.ventana, text="Enviar Mensaje", command = self.enviar_mensaje)
        self.boton_simular.grid(column=3, row=1)

        # Área de texto para mostrar el contenido XML
        self.texto = scrolledtext.ScrolledText(self.ventana, wrap=tk.WORD, width=65, height=30)
        self.texto.grid(column=1, row=2, columnspan=3)

        # self.mostrar_xml()


    def enviar_mensaje(self):
        sistema_drones = SistemaDrones()
        sistema_drones.procesar_mensajes()        


    def mostrar_xml(self):
        archivo = "Salida.xml"
        try:
            # Intenta analizar el archivo XML
            tree = ET.parse(archivo)
            root = tree.getroot()
            
            # Limpia el área de texto
            self.texto.delete(1.0, tk.END)
            
            # Agrega el contenido del archivo XML al área de texto
            self.texto.insert(tk.INSERT, ET.tostring(root, encoding="utf-8").decode())
        except Exception as e:
            # Maneja las excepciones en caso de errores
            self.texto.delete(1.0, tk.END)
            self.texto.insert(tk.INSERT, f"Error al cargar el archivo XML: {str(e)}")        
    
    def iniciar(self):
        self.ventana.mainloop()

# Uso de la clase
# nombre_archivo = "ejemplo.xml"  # Reemplaza con el nombre de tu archivo XML
# visor = VisorXML("entradaV3a.xml")
# visor.iniciar()
