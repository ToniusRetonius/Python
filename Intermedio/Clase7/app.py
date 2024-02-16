import tkinter as tk
from tkinter import ttk

##################################
def presionado():
    caja_saludo.delete(0,tk.END)
    nombre = caja.get()
    frase = "Hola " + nombre
    caja_saludo.insert(0,frase)





##################################
""" Para crear la app de escritorio creo la venta primero instanciando el objeto Tk(). Le doy un titulo y le configuro un tama;o """
ventana = tk.Tk()
ventana.title("App")
ventana.config(width=300, height=300)

boton = tk.Button(text='Hola mundo!', command=presionado)
boton.place(x=20, y=20)

caja = tk.Entry()
caja.place(x=20, y=100)

caja_saludo = tk.Entry()
caja_saludo.place(x=20, y=160)

etiqueta =tk.Label(text="Ingrese su nombre: ")
etiqueta.place(x=20, y=70)



""" creo el metodo .mainloop() que crea un bucle sobre los widgets generados entre la creacion de la ventana y el mainloop(). Esto es para que se muestren constantemente """
ventana.mainloop()

""" 
DIFERENCIA ENTRE TK Y TTK
ttk cambia el dise;o (mas nuevo) 

EJEMPLO:

b1 = tk.Button(text="Hola")
b1.place(x=20, y=20)

b2 = ttk.Button(text="Hola")
b2.place(x=20, y=60) 
"""