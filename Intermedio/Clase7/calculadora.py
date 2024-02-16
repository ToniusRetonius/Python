import tkinter as tk
import sys
from tkinter import ttk
from tkinter import messagebox

#################################

def convertir(valor):
    try:
        valor = float(valor)
    except ValueError:
        valor = "Error"
    return valor

def sumar():
    """ para borrar resultados anteriores utilizo .delete()"""
    c_tres.delete()
    a = c_uno.get()
    a = convertir(a)
    b = c_dos.get()
    b = convertir(b)

    if a != "Error" and b != "Error":
        c = a + b 
    else:
        c = "Error"

        """ Para alertar al usuario utilizamos messagebox """
        messagebox.showerror(title="Error", message="Hay un problema con los datos")
    
    """ .insert( posicion inicial , posicion final)  """
    c_tres.insert(0,c)

def restar():
    """ para borrar resultados anteriores utilizo .delete()"""
    c_tres.delete()
    a = c_uno.get()
    a = convertir(a)
    b = c_dos.get()
    b = convertir(b)

    if a != "Error" and b != "Error":
        c = a - b 
    else:
        c = "Error"

        """ Para alertar al usuario utilizamos messagebox """
        messagebox.showerror(title="Error", message="Hay un problema con los datos")
    
    """ .insert( posicion inicial , posicion final)  """
    c_tres.insert(0,c)

def multiplicar():
    """ para borrar resultados anteriores utilizo .delete()"""
    c_tres.delete()
    a = c_uno.get()
    a = convertir(a)
    b = c_dos.get()
    b = convertir(b)

    if a != "Error" and b != "Error":
        c = a * b 
    else:
        c = "Error"

        """ Para alertar al usuario utilizamos messagebox """
        messagebox.showerror(title="Error", message="Hay un problema con los datos")
    
    """ .insert( posicion inicial , posicion final)  """
    c_tres.insert(0,c)

def dividir():
    """ para borrar resultados anteriores utilizo .delete()"""
    c_tres.delete()
    a = c_uno.get()
    a = convertir(a)
    b = c_dos.get()
    b = convertir(b)

    if a != "Error" and b != "Error" and b != 0 :
        c = a / b 
    else:
        c = "Error"
        
        """ Para alertar al usuario utilizamos messagebox """
        messagebox.showerror(title="Error", message="Hay un problema con los datos")
    
    """ .insert( posicion inicial , posicion final)  """
    c_tres.insert(0,c)

def salir():
    r = messagebox.askokcancel(title="Salir", message="Esta seguro que desea salir?")
    if r:
        sys.exit()

def informar():
    messagebox.showinfo(title="Informacion", message="Calculadora creada con Python")

#################################

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.config(width=300, height=300)

label_1 = tk.Label(text="Dato 1")
label_2 = tk.Label(text="Dato 2")
label_3 = tk.Label(text="Resultado")

label_1.place(x=20, y=10)
label_2.place(x=160, y=10)
label_3.place(x=90, y=160)

c_uno = tk.Entry()
c_dos = tk.Entry()
c_tres = tk.Entry()

c_uno.place(x=20, y=40)
c_dos.place(x=160, y=40)
c_tres.place(x=90, y=190)

btn_suma = tk.Button(text=" + ", command=sumar)
btn_resta = tk.Button(text=" - ", command=restar)
btn_multiplicacion = tk.Button(text=" * ", command=multiplicar)
btn_dividir = tk.Button(text=" / ", command=dividir)

btn_salir = tk.Button(text="SALIR", command=salir)
btn_info = tk.Button(text="INFO", command=informar)

btn_suma.place(x=20, y=100)
btn_resta.place(x=100, y=100)
btn_multiplicacion.place(x=180, y=100)
btn_dividir.place(x=260, y=100)

btn_salir.place(x=40, y=230, width=100, height=40)
btn_info.place(x=160, y=230, width=100, height=40)


ventana.mainloop()