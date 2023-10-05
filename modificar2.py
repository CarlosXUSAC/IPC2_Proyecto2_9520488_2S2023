import tkinter as tk
from tkinter import scrolledtext
import xml.etree.ElementTree as ET

class VisorXML:
    def __init__(self, nombre_archivo):
        self.ventana = tk.Tk()
        self.ventana.title("Visor de XML")
        
        # Etiqueta y entrada para el nombre del archivo XML
        self.etiqueta_archivo = tk.Label(self.ventana, text="Nombre del archivo XML:")
        self.etiqueta_archivo.pack()
        
        self.entrada_archivo = tk.Entry(self.ventana)
        self.entrada_archivo.pack()
        self.entrada_archivo.insert(tk.END, nombre_archivo)
        
        # Botón para cargar el archivo XML
        self.boton_cargar = tk.Button(self.ventana, text="Cargar XML", command=self.mostrar_xml)
        self.boton_cargar.pack()
        
        # Área de texto para mostrar el contenido XML
        self.texto = scrolledtext.ScrolledText(self.ventana, wrap=tk.WORD, width=40, height=20)
        self.texto.pack()
    
    def mostrar_xml(self):
        archivo = self.entrada_archivo.get()
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
nombre_archivo = "ejemplo.xml"  # Reemplaza con el nombre de tu archivo XML
visor = VisorXML(nombre_archivo)
visor.iniciar()
