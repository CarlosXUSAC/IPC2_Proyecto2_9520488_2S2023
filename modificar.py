import tkinter as tk
from tkinter import ttk, messagebox
import xml.etree.ElementTree as ET

class XMLModifier:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Agregar Instrucción a Mensaje")        
        self.root.iconbitmap("Usac_logo.ico")
        self.root.resizable(False, False)
        self.root.config(background="#EDB27A")
        self.root.geometry("400x140")

        # Establecer el estilo para el marco
        self.style = ttk.Style()
        self.style.configure("My.TFrame", background="#EDB27A")

        self.create_interface()

    def create_interface(self):
        # Crear un marco para organizar los elementos con el estilo personalizado
        frame = ttk.Frame(self.root, style="My.TFrame")
        frame.grid(row=0, column=0, padx=10, pady=10)

        label_text = ""
        ttk.Label(frame, text=label_text, background="#EDB27A").grid(row=0, column=0, padx=25)

        # Etiqueta para mostrar instrucciones con fondo de color
        label_text = "Agregar Instrucción a Mensaje"
        ttk.Label(frame, text=label_text, background="#EDB27A").grid(row=0, column=1, columnspan=2)

        # Campo de entrada para el nombre del mensaje
        ttk.Label(frame, text="Nombre del Mensaje:", background="#EDB27A").grid(row=1, column=1)
        self.nombre_mensaje_entry = ttk.Entry(frame)
        self.nombre_mensaje_entry.grid(row=1, column=2)

        # Campo de entrada para el nombre del dron
        ttk.Label(frame, text="Nombre del Dron:", background="#EDB27A").grid(row=2, column=1)
        self.nombre_dron_entry = ttk.Entry(frame)
        self.nombre_dron_entry.grid(row=2, column=2)

        # Campo de entrada para el valor de la instrucción
        ttk.Label(frame, text="Valor de la Instrucción:", background="#EDB27A").grid(row=3, column=1)
        self.valor_instruccion_entry = ttk.Entry(frame)
        self.valor_instruccion_entry.grid(row=3, column=2)

        # Botón para agregar la instrucción
        ttk.Button(frame, text="Agregar Instrucción", command=self.agregar_instruccion).grid(row=4, column=1, columnspan=2)

    def agregar_instruccion(self):
        nombre_mensaje = self.nombre_mensaje_entry.get()
        nombre_dron = self.nombre_dron_entry.get()
        valor_instruccion = self.valor_instruccion_entry.get()

        # Obtener el elemento Mensaje con el nombre especificado
        self.tree = ET.parse("config.xml")  # Lee el archivo XML existente
        mensaje = self.tree.find(".//Mensaje[@nombre='" + nombre_mensaje + "']")
        if mensaje is None:
            messagebox.showerror("Error", "No se encontró el Mensaje con el nombre especificado")
            return

        # Crear el elemento Instrucción
        instruccion = ET.Element("instruccion")
        instruccion.set("dron", nombre_dron)
        instruccion.text = valor_instruccion

        # Obtener el elemento Instrucciones o crearlo si no existe
        instrucciones = mensaje.find("instrucciones")
        if instrucciones is None:
            instrucciones = ET.Element("instrucciones")
            mensaje.append(instrucciones)

        # Agregar la instrucción a las instrucciones
        instrucciones.append(instruccion)

        # Guardar el archivo XML actualizado
        self.tree.write("config.xml")

        messagebox.showinfo("Éxito", "Instrucción agregada correctamente")

if __name__ == "__main__":
    app = XMLModifier()
    app.root.mainloop()
