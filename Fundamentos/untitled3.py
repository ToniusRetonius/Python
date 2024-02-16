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
