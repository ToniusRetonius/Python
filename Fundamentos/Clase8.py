### CLASE 8 ###

    # Aplicaciones de escritorio
    # tkinter es una libreria que contiene herramientas para
    # crear aplicaciones de escritorio (widgets)
import tkinter as tk

def saludar():
    print("Hola mundo!")

def mostrar_ingreso():
    # .get me devuelve en formato string 
    entry = caja.get()
    print(entry)

def cerrar_app():
    ventana.destroy()

    # Ventana es la instancia de la clase Tk
ventana = tk.Tk()
ventana.title("Principal - Curso de Python")
    # .config (width= value px , height=value px, 
ventana.config(width=800, height=800)

    # Etiqueta
etiqueta = tk.Label(text="Ingrese su nombre: ")
    # .place(x=20, y=30) posicion x coordenadas
etiqueta.place(x=20, y=30)

    # Boton
boton = tk.Button(text="Aceptar")
boton.place(x=20, y=150)

    # Caja
caja = tk.Entry()
caja.place( x=150, y=150, width=80, height=30)

    # Cuando creo el objeto, dentro de sus atributos le aplico
    # <<< command = nombre de la funcion >>>
boton_txt = tk.Button(text="Ver ingreso", command=most_ingreso)
boton_txt.place( x=250, y=150, width=70 , height=80 )

boton_salir = tk.Button(text="Ver ingreso", command=cerrar_app)
boton_salir.place( x=280, y=190, width=70 , height=80 )

    # Todo lo que quiero que se vea tiene que ir por arriba
    # de la funcion .mainloop
ventana.mainloop()


### LABORATORIO ###
import tkinter as tk

ventana = tk.Tk()

nombre = tk.Label(text="Imgrese su nombre: ")
nombre.place(x=10, y=10)
name = tk.Entry()
name.place(x=10, y=30)

apellido = tk.Label(text="Ingrese su apellido: ")
apellido.place(x=10, y=60)
last_name = tk.Entry()
last_name.place(x=10, y=80)

edad = tk.Label(text= "Ingrese su edad: ")
edad.place(x=10, y=110)
age = tk.Entry()
age.place(x=10, y=130)

boton = tk.Button(text="Aceptar")
boton.place(x=10, y=150)
ventana.mainloop()


### LABORATORIO ###
import tkinter as tk

def sumar():
    numero1 = int(num_uno.get())
    numero2 = int(num_dos.get())
    suma = int((numero1 + numero2))
    print(suma)

def sustraccion():
    numero1 = int(num_uno.get())
    numero2 = int(num_dos.get())
    resta = int((numero1 - numero2))
    print(resta)
    
def multiplicar():
    numero1 = int(num_uno.get())
    numero2 = int(num_dos.get())
    producto = int((numero1 * numero2))
    print(producto)

def division():
    numero1 = int(num_uno.get())
    numero2 = int(num_dos.get())
    cociente = int((numero1 / numero2))
    print(cociente)

ventana = tk.Tk()

num1 = tk.Label(text="Ingrese un numero: ")
num1.place(x=10, y=10)
num_uno = tk.Entry()
num_uno.place(x=10, y=30)

num2 = tk.Label(text="Ingrese otro numero: ")
num2.place(x=10, y=60)
num_dos = tk.Entry()
num_dos.place(x=10, y=80)

boton_suma = tk.Button(text="Sumar", command=sumar)
boton_suma.place(x=10, y=110)

boton_producto = tk.Button(text="Multiplicar", command=multiplicar)
boton_producto.place(x=10, y=150)

boton_sustraccion = tk.Button(text="Restar", command=sustraccion)
boton_sustraccion.place(x=90, y=110)

boton_division = tk.Button(text="Dividir", command=division)
boton_division.place(x=90, y=150)

ventana.mainloop()
