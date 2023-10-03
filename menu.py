import tkinter as tk
from tkinter import *


def info():
    ventana = tk.Toplevel()
    ventana.title("Info")
    ventana.iconbitmap('Usac_logo.ico')
    ventana.geometry("486x200")
    ventana['bg'] = '#66C6A0'
    img = tk.PhotoImage(file = "Foto.png")
    img2 = tk.PhotoImage(file = "Datos.png")
    label_X = tk.Label(ventana, text = '    ', bg= '#66C6A0')
    label_X.grid(row=0, column=0)
    label_img = tk.Label(ventana, image = img)
    label_img.grid(row=1, column=1)
    label_X2 = tk.Label(ventana, text = '    ', bg= '#66C6A0') 
    label_X2.grid(row=2, column=2)
    label_img2 = tk.Label(ventana, image = img2)
    label_img2.grid(row=1, column=3)
    ventana.mainloop()       


def menu():
    root = Tk()
    root.title('USAC')
    root.iconbitmap('Usac_logo.ico')
    root.geometry("400x320")
    root['bg'] = '#74a5d6'


    for r in range(0, 8):
        for c in range(0, 4):
            cell = Entry(root, width=13, bg= '#74a5d6')
            cell.grid(padx=8, pady=10, row=r, column=c)
            #cell.insert(0, '({}, {})'.format(r, c))

    etiqueta2 = tk.Label(root, text = "Drone", bg= '#74a5d6')
    etiqueta2.grid(row = 0, column = 1)

    etiqueta2 = tk.Label(root, text = "Console", bg= '#74a5d6')
    etiqueta2.grid(row = 0, column = 2)

    etiqueta3 = tk.Label(root, text = "          File         ", bg= '#8DB6CD')
    etiqueta3.grid(row = 1, column = 1)

    etiqueta3 = tk.Label(root, text = "  Management  ", bg= '#8DB6CD')
    etiqueta3.grid(row = 1, column = 2)

    boton1 = tk.Button(root, text= "Open XML", padx = 10)
    boton1.grid(row = 2, column = 1)

    boton2 = tk.Button(root, text= "Save XML", padx = 12)
    boton2.grid(row = 3, column = 1)

    boton3 = tk.Button(root, text= "Clear", padx = 26)
    boton3.grid(row = 4, column = 1)

    boton4 = tk.Label(root, text = "    Developer    ", bg= '#8DB6CD')
    boton4.grid(row = 5, column = 1)

    boton5 = tk.Button(root, text= "Info.", padx = 29, command = info)
    boton5.grid(row = 6, column = 1)

    boton6 = tk.Button(root, text= "Exit", padx = 28)
    boton6.grid(row = 7, column = 1)

    boton7= tk.Button(root, text= "Drons", padx = 26)
    boton7.grid(row = 2, column = 2)

    boton8= tk.Button(root, text= "Systems", padx = 20)
    boton8.grid(row = 3, column = 2)

    boton9= tk.Button(root, text= "Messages", padx = 16)
    boton9.grid(row = 4, column = 2)

    boton10= tk.Label(root, text = "          Help          ", bg= '#8DB6CD')
    boton10.grid(row = 5, column = 2)

    boton11= tk.Button(root, text= "User help", padx = 16)
    boton11.grid(row = 6, column = 2)

    root.mainloop()

menu()