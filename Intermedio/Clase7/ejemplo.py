import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
""" 
creo una lista >>>
lista = tk.Listbox()
lista.insert(0, "Python", "C", "C++", "Java")
lista.place(x=10, y=10)
"""

""" 
creo una lista desplegable >>>
lista_desplegable = ttk.Combobox(
 values=[
    "Visual Basic",
    "Python",
    "C",
    "C++",
    "Java"
 ]
)
lista_desplegable.place(x=10, y=10)
"""

""" 
creo una barra de menu >>>
##########
def nuevo():
    print("Nuevo archivo.")

def acerca_de():
    print("Acerca de:")

##########

ventana_principal = tk.Tk()
ventana.title("Mi primera aplicación")

barra_de_menu = tk.Menu()

menu_archivo = tk.Menu(barra_de_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo)

menu_ayuda = tk.Menu(barra_de_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de...",command=acerca_de)

barra_de_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_de_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

ventana.config(width=300, height=200, menu=barra_de_menu)
"""

ventana.mainloop()
