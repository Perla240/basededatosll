import tkinter as tk
from tkinter import *

# Crear la ventana principal 
ventana = tk.Tk()
ventana.title("Sistema")
ventana.resizable(False, False)

# Crear un frame dentro de la ventana principal
frame = tk.Frame(ventana, height=250, width=350, bg="white")
frame.pack(padx=95, pady=85)

# Agregar un campo de texto para ingresar el nombre del cliente
etiqueta_cliente = tk.Label(frame, text="Nombre del Cliente:")
etiqueta_cliente.pack()

entrada_cliente = tk.Entry(frame)
entrada_cliente.pack()

# Función para manejar la confirmación de venta
def confirmar_venta():
    nombre = entrada_cliente.get()
    if nombre:
        print(f"Venta realizada para: {nombre}")
    else:
        print("Por favor ingrese un nombre de cliente")

# Agregar un botón para confirmar la venta
boton_confirmar = tk.Button(frame, text="Confirmar Venta", command=confirmar_venta)
boton_confirmar.pack(pady=10)

# Iniciar el bucle principal de la ventana 
ventana.mainloop()
