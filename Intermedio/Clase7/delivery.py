import tkinter as tk
import os
from tkinter.constants import END
import requests
from tkinter import ttk
from tkinter import messagebox
from openpyxl import workbook
from openpyxl import load_workbook

#######################################

def guardar(orden):
    ws = wb.active
    ws.append(orden)
    wb.save(filename="empanadas.xlsx")

    f = open("datostarde.csv", "a")
    f.write(orden[0] + "," + str(orden[1]) + "," + str(orden[2]) + "," + str(orden[3]) + ","  + str(orden[4]) + "\n")
    f.close()

def validar(dato):
    try:
        dato = int(dato)
    except ValueError:
        dato = -1
    return dato

def borrar():
    e_soja.delete(0,tk,END)
    e_jyq.delete(0,tk,END)
    e_humita.delete(0,tk,END)
    cliente.delete(0,tk,END)

def pedido():
    cant_soja = e_soja.get()
    cant_soja = validar(cant_soja)
    cant_jyq = e_soja.get()
    cant_jyq = validar(cant_jyq)
    cant_humita = e_soja.get()
    cant_humita = validar(cant_humita)
    cant_soja = e_soja.get()
    cant_soja = validar(cant_soja)

    cant_unidad = costos()
    
    if cant_soja >=0 and cant_jyq >= 0 and cant_humita >=0:
        cliente = nombre_cliente.get()

        if cliente:
            respuesta = messagebox.askyesno(title="Pregunta", message="Confirma el pedido?")
            
            if respuesta:
                costo_total = (cant_soja + cant_jyq + cant_humita) * cant_unidad
                gustos = [cliente, cant_soja, cant_jyq, cant_humita, costo_total]

                ## guardar ##
                guardar(gustos)
                messagebox.showinfo(title="Informacion", message="Pedido exitoso")
                borrar()
            else:
                messagebox.showinfo(title="Informacion", message="Pedido en pausa")
        else:
            messagebox.showwarning(title="Advertencia", message="Error, ingrese nombre del cliente")    
    else:
        messagebox.showwarning(title="Advertencia", message="Error, ingrese datos validos")

def cancelar_pedido():
    respuesta = messagebox.askyesno(title="Pregunta", message="Desea cancelar el pedido?")
    
    if respuesta:
        borrar()

def comprobarArchivo():
    existe = os.path.exists("empanadas.xlsx")

    if existe:
        wb = load_workbook(filename="empanadas.xlsx")
        ws = wb.active
    else:
        wb = workbook()
        ws = wb.active
        titulo = ["Nombre","Soja","J y Q","Humita","Total"]
        ws.append(titulo)
        wb.save(filename="empanadas.xlsx")

        f = open("datostarde.csv", "a")
        f.write("Nombre,Soja,JyQ, Humita, Total\n")
        f.close()
    return wb

def costos():
    r = requests.get("https://www.dolarsi.com/api/api.php?type=cotizador")
    value = r.json()[0]["casa"]["venta"]
    dolar = float(value.replace(",", "."))
    costo = round(dolar/10) * 10
    return costo


#######################################
#####################

wb = comprobarArchivo()

#####################

ventana = tk.Tk()
ventana.config(width=400, height=400)
ventana.title("Delivery")

## ETIQUETAS ##
bienvenido = tk.Label(text="------ PEDIDOS ------")
bienvenido.place(x=140, y=20)

soja = tk.Label(text="Ingrese cantidad de empanadas de soja: ")
soja.place(x=50, y=90)

jyq = tk.Label(text="Ingrese cantidad de empanadas de J y Q: ")
jyq.place(x=50, y=150)

humita = tk.Label(text="Ingrese cantidad de empanadas de Humita: ")
humita.place(x=50, y=210)

nombre_cliente = tk.Label(text="Nombre del cliente: ")
nombre_cliente.place(x=50, y=280)

## CAJAS ##
e_soja = tk.Entry()
e_soja.place(x=230, y=90)

e_jyq = tk.Entry()
e_jyq.place(x=230, y=150)

e_humita = tk.Entry()
e_humita.place(x=230, y=210)

cliente = tk.Entry()
cliente.place(x=230, y=280)

## BOTONES ## 
btn_pedido = tk.Button(text="Hacer pedido", command=pedido)
btn_pedido.place(x=270, y=330, height=40, width=100)

btn_cancelar = tk.Button(text="Cancelar pedido", command=cancelar_pedido)
btn_cancelar.place(x=150, y=330, height=40, width=100)

btn_info = tk.Button(text="Info")
btn_info.place(x=30, y=330, height=40, width=100)

ventana.mainloop()